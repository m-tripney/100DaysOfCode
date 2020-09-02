cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
    (original order)"""
    return ", ".join(cars["Jeep"])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [model[0] for model in cars.values()]


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
    'grep' string which defaults to 'trail' for this exercise,
    sort the resulting sequence alphabetically"""
    grepped = []
    for key, value in cars.items():
        for model in value:
            if grep.lower() in model.lower():
                grepped.append(model)
    return sorted(grepped)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
    sorted alphabetically"""
    for key, value in cars.items():
        value.sort()
    return cars
