from django.db import models


class TruckCategory(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Light Duty", "Heavy Duty", or "Dayun", "Dongfeng"
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Truck Categories"

    def __str__(self):
        return self.name


class TruckModel(models.Model):
    name = models.CharField(max_length=150)  # e.g., "Dayun 4 Tonne Truck", "Dongfeng EV45"
    category = models.ForeignKey(TruckCategory, on_delete=models.CASCADE, related_name='trucks')
    tagline = models.CharField(max_length=255, blank=True)
    
    # Primary Card Thumbnail Image
    main_image = models.ImageField(upload_to='trucks/main/', blank=True, null=True)
    
    # Dedicated Quick-Access View Fields
    interior_image = models.ImageField(upload_to='trucks/interior/', blank=True, null=True, help_text="Cabin / Interior view photo")
    exterior_image = models.ImageField(upload_to='trucks/exterior/', blank=True, null=True, help_text="Full exterior vehicle photo")
    
    brochure_pdf = models.FileField(upload_to='brochures/', blank=True, null=True)
    
    # Core Specs
    range_km = models.CharField(max_length=50, help_text="e.g. 210 km or 250-350 km")
    payload_capacity_kg = models.IntegerField(help_text="Payload in KG, e.g. 7200")
    battery_capacity_kwh = models.DecimalField(max_digits=6, decimal_places=2, help_text="e.g. 98.04 or 105.28")
    fast_charge_time = models.CharField(max_length=50, default="2 hrs (DC Fast)")
    
    # Additional Detailed Technical Specs from Catalogues
    dimensions = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. 6250mm x 2350mm x 3124mm")
    wheelbase = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 3300mm")
    motor_peak_power = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 130 kW")
    motor_torque = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 850 Nm")
    max_speed = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 90 km/h")
    drive_mode = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 4x2 / 4x4")
    charging_port = models.CharField(max_length=50, default="CCS2")
    
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TruckImage(models.Model):
    """
    Gallery model allowing unlimited interior/exterior photos per truck.
    """
    IMAGE_TYPES = (
        ('exterior', 'Exterior View'),
        ('interior', 'Interior / Cabin'),
        ('spec', 'Technical Diagram / Spec'),
    )

    truck = models.ForeignKey(TruckModel, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='trucks/gallery/')
    caption = models.CharField(max_length=150, blank=True, help_text="e.g. Digital Dashboard Display")
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPES, default='exterior')

    def __str__(self):
        return f"{self.truck.name} - {self.get_image_type_display()}"


class QuoteRequest(models.Model):
    full_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    truck_model = models.ForeignKey(TruckModel, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.truck_model}"