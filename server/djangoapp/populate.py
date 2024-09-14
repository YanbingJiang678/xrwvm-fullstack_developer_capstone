import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')

import django
django.setup()

from django.utils.dateparse import parse_date
from djangoapp.models import CarMake, CarModel

def initiate():
    # Create CarMake instances
    car_make_data = [
        {"name": "Nissan", "description": "Japanese car manufacturer"},
        {"name": "Mercedes-Benz", "description": "German car manufacturer"},
        {"name": "Audi", "description": "German car manufacturer"},
        {"name": "Kia", "description": "South Korean car manufacturer"}
    ]

    car_make_instances = []
    for make in car_make_data:
        car_make = CarMake(name=make["name"], description=make["description"])
        car_make.save()
        car_make_instances.append(car_make)

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]}
    ]

    for model in car_model_data:
        car_model = CarModel(
            name=model["name"],
            type=model["type"],
            year=parse_date(f"{model['year']}-01-01"),
            car_make=model["car_make"]
        )
        car_model.save()

if __name__ == '__main__':
    print("Starting population script...")
    populate()
    print("Population script completed.")