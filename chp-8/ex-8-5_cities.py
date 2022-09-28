def describe_city(city, country='Nigeria'):
    """Shows each city with the country its in"""
    print("{} is in {}".format(city, country))
describe_city('Abuja')
describe_city(city='Lagos')
describe_city(city='Texas', country='America')