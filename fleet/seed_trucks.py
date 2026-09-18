import os
import sys
import django
from pathlib import Path

# Add project root directory (utu_trucks_site) to Python search path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'utu_website.utu_website.settings')
django.setup()

from fleet.models import TruckCategory, TruckModel

def run_seed():
    print("Seeding Commercial Truck Data...")

    # 1. Create or Get Categories
    dayun_cat, _ = TruckCategory.objects.get_or_create(
        slug='dayun',
        defaults={'name': 'Dayun'}
    )
    
    dongfeng_cat, _ = TruckCategory.objects.get_or_create(
        slug='dongfeng',
        defaults={'name': 'Dongfeng'}
    )

    # 2. Truck Data
    trucks_data = [
        # --- DAYUN MODELS ---
        {
            "category": dayun_cat,
            "name": "Dayun 4 Tonne Electric Light Truck",
            "tagline": "Efficient Urban & Regional Delivery Commercial EV",
            "range_km": "210 km",
            "payload_capacity_kg": 4000,
            "battery_capacity_kwh": 81.14,
            "fast_charge_time": "1.5 - 2 hrs (DC Fast)",
            "dimensions": "5995mm x 2150mm x 3150mm",
            "wheelbase": "3308mm",
            "motor_peak_power": "115 kW",
            "motor_torque": "330 Nm",
            "max_speed": "90 km/h",
            "drive_mode": "4x2",
            "charging_port": "CCS2",
            "featured": True,
        },
        {
            "category": dayun_cat,
            "name": "Dayun 7.5 Tonne Electric Medium Truck",
            "tagline": "Heavy Duty Distribution with Maximum Efficiency",
            "range_km": "250 - 300 km",
            "payload_capacity_kg": 7500,
            "battery_capacity_kwh": 105.28,
            "fast_charge_time": "2 hrs (DC Fast)",
            "dimensions": "6995mm x 2300mm x 3300mm",
            "wheelbase": "3800mm",
            "motor_peak_power": "160 kW",
            "motor_torque": "800 Nm",
            "max_speed": "90 km/h",
            "drive_mode": "4x2",
            "charging_port": "CCS2",
            "featured": True,
        },
        {
            "category": dayun_cat,
            "name": "Dayun 10 Tonne Electric Heavy Truck",
            "tagline": "High Payload & Long-Range Regional Logistics",
            "range_km": "280 - 350 km",
            "payload_capacity_kg": 10000,
            "battery_capacity_kwh": 162.28,
            "fast_charge_time": "2 hrs (DC Fast)",
            "dimensions": "7995mm x 2500mm x 3450mm",
            "wheelbase": "4500mm",
            "motor_peak_power": "200 kW",
            "motor_torque": "1000 Nm",
            "max_speed": "85 km/h",
            "drive_mode": "4x2",
            "charging_port": "CCS2",
            "featured": False,
        },

        # --- DONGFENG MODELS ---
        {
            "category": dongfeng_cat,
            "name": "Dongfeng EV45 Electric Light Commercial Vehicle",
            "tagline": "The Ultimate Last-Mile Delivery Workhorse",
            "range_km": "220 - 260 km",
            "payload_capacity_kg": 4500,
            "battery_capacity_kwh": 81.14,
            "fast_charge_time": "1.5 hrs (DC Fast)",
            "dimensions": "5995mm x 2100mm x 2950mm",
            "wheelbase": "3300mm",
            "motor_peak_power": "120 kW",
            "motor_torque": "320 Nm",
            "max_speed": "90 km/h",
            "drive_mode": "4x2",
            "charging_port": "CCS2",
            "featured": True,
        },
        {
            "category": dongfeng_cat,
            "name": "Dongfeng Rich 6 EV Pickup",
            "tagline": "Versatile 4x4 Commercial & Utility Electric Pickup",
            "range_km": "350 km",
            "payload_capacity_kg": 1200,
            "battery_capacity_kwh": 67.90,
            "fast_charge_time": "45 min (30%-80% DC)",
            "dimensions": "5290mm x 1850mm x 1790mm",
            "wheelbase": "3050mm",
            "motor_peak_power": "120 kW",
            "motor_torque": "420 Nm",
            "max_speed": "110 km/h",
            "drive_mode": "4x2 / Rear Drive",
            "charging_port": "CCS2",
            "featured": False,
        },
        {
            "category": dongfeng_cat,
            "name": "Dongfeng EM26 Electric Cargo Van",
            "tagline": "High-Volume Urban Delivery EV Van",
            "range_km": "220 km",
            "payload_capacity_kg": 1500,
            "battery_capacity_kwh": 41.86,
            "fast_charge_time": "1 hr (DC Fast)",
            "dimensions": "4865mm x 1715mm x 2060mm",
            "wheelbase": "3050mm",
            "motor_peak_power": "60 kW",
            "motor_torque": "220 Nm",
            "max_speed": "100 km/h",
            "drive_mode": "4x2",
            "charging_port": "CCS2",
            "featured": False,
        },
    ]

    for truck in trucks_data:
        obj, created = TruckModel.objects.update_or_create(
            name=truck["name"],
            defaults=truck
        )
        action = "Created" if created else "Updated"
        print(f"[{action}] {obj.name}")

    print("\nDatabase seeding completed successfully!")

if __name__ == '__main__':
    run_seed()