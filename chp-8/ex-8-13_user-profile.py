def build_profile(first, last, **my_info):
    my_info['first name'] = first
    my_info['last name'] = last
    return my_info
my_profile = build_profile('success', 'Nwaoha',
location='gwarimpa',
age = '15')
print(my_profile)