def kw_function(**kwargs):
    print(kwargs)

kw_function(a=1,b=5,h=16)


#przypapdek 1
def create_user_profile(**kwargs):
    profile = {
        "username":"Guest",
        "email":"guest1@example.com",
        "age":None,
        "is_active":True,
        "is_admin":False
    }
    profile.update(kwargs)
    return profile
user_profile = create_user_profile(username="Jan Nowak",email="janek2@gmail.com",
                                   age=45,city="Kraków")
print(user_profile)
