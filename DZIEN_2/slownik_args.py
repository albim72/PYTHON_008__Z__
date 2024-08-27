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

#przykład 3- dekroatory przyjmujące argumenty

def logging_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Wołana funckja: {func.__name__} z argumentami {args} i argumentami słownikowymi: {kwargs}")
        return func(*args,**kwargs)
    return wrapper

@logging_decorator
def add(a,b,**kwargs):
    result =  a*2+b*3
    for key,value in kwargs.items():
        print(f"procesowanie dodatkowego argumentu {key} z wartością: {value}")
        if key == 'add_to_result':
            result += value
        elif key == 'multiply_result':
            result *= value
    return result

result = add(2,3)
print(result)

result_with_kwargs = add(2,3,add_to_result = 7)
print(result_with_kwargs)

result_multiply = add(2,3,add_to_result=7,multiply_result=2)
print(result_multiply)

result_m2 = add(2,3,multiply_result=2)
print(result_m2)

result_x = add(2,3,blabla=12)
print(result_x)

result_multiply_2 = add(2,3,multiply_result=2,add_to_result=7)
print(result_multiply_2)
