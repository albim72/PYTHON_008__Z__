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

#przykład 2 - -przekazywanie argumentów do innych funkcji

def print_info(name,age,**kwargs):
    print(f"name: {name}, age: {age}")
    if kwargs:
        print("Dodatkowa informacja:")
        for key,value in kwargs.items():
            print(f"{key}: {value}")

def user_datails(**kwargs):
    print_info(**kwargs)

user_datails(name="Alicja", age=25, location="Sopot", profession="inżynier sieci")
user_datails(name="Leon",age=23, location="Opole")
