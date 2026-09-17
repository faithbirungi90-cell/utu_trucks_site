from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import TruckCategory, TruckModel, QuoteRequest


def home(request):
    trucks = TruckModel.objects.all()
    featured_truck = TruckModel.objects.filter(featured=True).first() or trucks.first()

    return render(
        request,
        'fleet/home.html',
        {
            'trucks': trucks,
            'featured_truck': featured_truck,
        },
    )


def lineup(request):
    category_slug = request.GET.get('category')
    categories = TruckCategory.objects.all()
    trucks = TruckModel.objects.select_related('category').all()

    if category_slug:
        trucks = trucks.filter(category__slug=category_slug)

    return render(
        request,
        'fleet/lineup.html',
        {
            'categories': categories,
            'trucks': trucks,
            'selected_category': category_slug,
        },
    )


def truck_detail(request, pk):
    truck = get_object_or_404(TruckModel, pk=pk)
    related_trucks = TruckModel.objects.filter(category=truck.category).exclude(pk=pk)[:3]
    # Safely fetch related inline gallery images if available
    gallery_images = getattr(truck, 'images', None)
    if gallery_images is not None:
        gallery_images = gallery_images.all()

    return render(
        request,
        'fleet/truck_detail.html',
        {
            'truck': truck,
            'related_trucks': related_trucks,
            'gallery_images': gallery_images,
        },
    )


def technology(request):
    return render(request, 'fleet/technology.html')


def get_quote(request):
    trucks = TruckModel.objects.all()
    selected_truck_id = request.GET.get('truck_id')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        company_name = request.POST.get('company_name', 'N/A')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        truck_id = request.POST.get('truck_id')
        message = request.POST.get('message', 'None')

        truck_obj = (
            TruckModel.objects.filter(id=truck_id).first() if truck_id else None
        )

        # 1. Save to database
        QuoteRequest.objects.create(
            full_name=full_name,
            company_name=company_name,
            email=email,
            phone=phone,
            truck_model=truck_obj,
            message=message,
        )

        # 2. Build email notification
        truck_name = truck_obj.name if truck_obj else 'General Inquiry / Unspecified'
        subject = f"New Commercial Fleet Quote Request - {full_name}"
        email_body = f"""
New Quote Request Received:

Client Details:
- Name: {full_name}
- Company: {company_name}
- Email: {email}
- Phone: {phone}
- Requested Model: {truck_name}

Message / Notes:
{message}
        """

        # 3. Send email to Customer Care
        try:
            send_mail(
                subject=subject,
                message=email_body,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', email),
                recipient_list=['customercare@utucars.africa'],
                fail_silently=False,
            )
        except Exception as e:
            # Logs or ignores email failure so database entry is still saved smoothly
            pass

        messages.success(
            request,
            'Thank you! Your quote request has been sent to UTU Fleet Sales.',
        )
        return redirect('get_quote')

    return render(
        request,
        'fleet/quote.html',
        {
            'trucks': trucks,
            'selected_truck_id': selected_truck_id,
        },
    )