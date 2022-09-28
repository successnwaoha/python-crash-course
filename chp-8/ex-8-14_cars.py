def car_info(manufacturer, car_model, **other_info):
    """Builds a car and adds it to a dictionary"""
    other_info['manufacrurer'] = manufacturer
    other_info['car_model'] = car_model
    return other_info
car = car_info('subaru', 'outback', 
color = 'blue',
tow_package = True)
print(car)