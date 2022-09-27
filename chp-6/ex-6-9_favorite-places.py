favorite_places = {
    'gabriel':{
        'city' : ['lybia', 'paris', 'canada']
    },
    'dumaga' :{
        'city':['canada', 'japan', 'korea']
    },
    'success':{
        'city':['japan', 'korea', 'canada']
    }
}
for fav, city in favorite_places.items():
    print(fav)
    fave = f"{city['city']}"
    print(fave)