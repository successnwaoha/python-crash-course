cities = {
    'abuja':{
        'country':'nigeria',
        'population':'123456',
        'fact':'the land is green'
    },
    'texas':{
        'country':'america',
        'population':'654321',
        'fact':'the land is red'
    },
    'mumbai':{
        'country':'india',
        'population':'543621',
        'fact':'the land is pink'
    }
}
for city, values in cities.items():
    print(f"{city.title()}: {values['country']}, {values['population']}, {values['fact']}")