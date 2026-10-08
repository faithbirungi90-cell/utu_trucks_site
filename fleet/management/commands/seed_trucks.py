from decimal import Decimal
from django.core.management.base import BaseCommand
from fleet.models import TruckCategory, TruckModel


class Command(BaseCommand):
    help = 'Seeds database with Dayun and Dongfeng truck categories and models'

    def handle(self, *args, **options):
        # 1. Clear existing data to avoid duplicates
        TruckModel.objects.all().delete()
        TruckCategory.objects.all().delete()

        # 2. Create the 3 Truck Categories
        light_comm = TruckCategory.objects.create(
            name='Light Commercial', 
            slug='light-commercial'
        )
        med_duty = TruckCategory.objects.create(
            name='Medium Duty', 
            slug='medium-duty'
        )
        heavy_duty = TruckCategory.objects.create(
            name='Heavy Duty', 
            slug='heavy-duty'
        )

        # 3. Create all 8 Truck Models
        trucks = [
            {
                'category': light_comm,
                'name': 'Dongfeng EV45 (2.5 Tonne)',
                'tagline': 'Compact 3-seater electric delivery truck.',
                'range_km': '350 km',
                'payload_capacity_kg': 2480,
                'battery_capacity_kwh': Decimal('81.00'),
                'fast_charge_time': '2 hrs',
                'dimensions': '5995mm by 2180mm by 2250m',
                'wheelbase': '3308mm',
                'motor_peak_power': '120 kW',
                'motor_torque': '320 Nm',
                'max_speed': '90 km/h',
                'drive_mode': '4x2',
                'charging_port': 'CCS2',
                'price': 'Contact for price',
                'main_image': 'fleet/images/2.5T_dongfeng.png',
            },
             {
                'category': light_comm,
                'name': 'Dayun 4 Tonne Truck',
                'tagline': 'Built for urban distribution with 7.2T loading capability.',
                'range_km': '250 km',
                'payload_capacity_kg': 7200,
                'battery_capacity_kwh': Decimal('98.05'),
                'fast_charge_time': '2 hrs (DC Fast)',
                'dimensions': '6250mm x 2350mm x 3310mm',
                'wheelbase': '3300mm',
                'motor_peak_power': '130 kW',
                'motor_torque': '850 Nm',
                'max_speed': '90 km/h',
                'drive_mode': '4x2',
                'charging_port': 'CCS2',
                'price': 'Contact for price',
                'main_image': 'fleet/images/4T_dayun.png',
            },
            {
                'category': light_comm,
                'name': 'Dongfeng CL L2 (4.5 Tonne)',
                'tagline': 'Refrigerated / cargo EV truck for urban logistics.',
                'range_km': '200 km',
                'payload_capacity_kg': 2200,
                'battery_capacity_kwh': Decimal('86.00'),
                'fast_charge_time': 'Fast Charging',
                'dimensions': '6300mm by 2150mm by 3150m',
                'wheelbase': '3360mm',
                'motor_peak_power': '115 kW',
                'motor_torque': '325 Nm',
                'max_speed': '89 km/h',
                'drive_mode': '4x2',
                'charging_port': 'CCS2',
                'price': 'Contact for price',
                'main_image': 'fleet/images/4.5T_dongfeng.png',
            },
            {
                'category': med_duty,
                'name': 'Dayun 7.5 Tonne Truck',
                'tagline': 'Versatile 7.2T capacity EV truck for regional transport.',
                'range_km': '250 km',
                'payload_capacity_kg': 7200,
                'battery_capacity_kwh': Decimal('98.00'),
                'fast_charge_time': '2 hrs (DC Fast)',
                'dimensions': '6250mm x 2350mm x 3310mm',
                'wheelbase': '3300mm',
                'motor_peak_power': '130 kW',
                'motor_torque': '850 Nm',
                'max_speed': '90 km/h',
                'drive_mode': '4x2',
                'charging_port': 'CCS2',
                'price': 'Contact for price',
                'main_image': 'fleet/images/default-truck.png'
            },
            {
                'category': med_duty,
                'name': 'Dongfeng MNCL L2 (8.5 Tonne)',
                'tagline': 'Medium-duty electric logistics vehicle.',
                'range_km': '200 km',
                'payload_capacity_kg': 8500,
                'battery_capacity_kwh': Decimal('100.00'),
                'fast_charge_time': 'Fast Charging',
                'dimensions': '7300mm x 2150mm x 3150 mm',
                'wheelbase': '3360mm',
                'motor_peak_power': '115 kW',
                'motor_torque': '325 Nm',
                'max_speed': '89 km/h',
                'drive_mode': '4x2',
                'charging_port': 'CCS2',
                'price': 'Contact for price',
                'main_image': 'fleet/images/8.5T_dongfeng.png',
            },

            {
                'category': heavy_duty,
                'name': 'Dayun 10 Tonne Truck',
                'tagline': 'High-capacity 10,000kg payload commercial logistics vehicle.',
                'range_km': '200 km',
                'payload_capacity_kg': 10000,
                'battery_capacity_kwh': Decimal('105.28'),
                'fast_charge_time': '2 hrs (DC Fast)',
                'dimensions': '6250mm x 2350mm x 3310mm',
                'wheelbase': '4700mm',
                'motor_peak_power': '150 kW',
                'motor_torque': '1050 Nm',
                'max_speed': '70 km/h',
                'drive_mode': '4x2',
                'charging_port': 'CCS2',
                'price': 'Contact for price',
                'main_image': 'fleet/images/5_step_truck.png',
            },
            {         
                'category': heavy_duty,
                'name': 'Dongfeng M3EV (12 Tonne)',
                'tagline': 'Heavy-duty EV chassis with 1000Nm motor torque',
                'range_km': '200 km',
                'payload_capacity_kg': 12000,
                'battery_capacity_kwh': Decimal('210.00'),
                'fast_charge_time': '2 hrs (DC Fast)',
                'dimensions': '9890mm x 2495mm x 2950 mm',
                'wheelbase': '3360mm',
                'motor_peak_power': '115 kW',
                'motor_torque': '325 Nm',
                'max_speed': '89 km/h',
                'drive_mode': '4x2',
                'charging_port': 'CCS2',
                'price': 'Contact for price',
                'main_image': 'fleet/images/12T_dongfeng.png',
            },
            {
                'category': heavy_duty,
                'name': 'Dayun N6H 18 Tonne Truck',
                'tagline': 'Heavy-duty zero-emission cargo truck for heavy haulage.',
                'range_km': '250 km',
                'payload_capacity_kg': 7400,
                'battery_capacity_kwh': Decimal('230.00'),
                'fast_charge_time': '1 hr (DC Fast)',
                'dimensions': '6250mm x 2350mm x 3310mm',
                'wheelbase': '6200mm',
                'motor_peak_power': '165 kW',
                'motor_torque': '1000 Nm',
                'max_speed': '80 km/h',
                'drive_mode': '4x2',
                'charging_port': 'CCS2',
                'price': 'Contact for price',
                'main_image': 'fleet/images/18T.png',
            },

        ]

        for item in trucks:
            TruckModel.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully seeded categories and truck models!'))