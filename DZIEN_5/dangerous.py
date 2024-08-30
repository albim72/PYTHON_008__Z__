import os
import subprocess

#funkcja eval()
user_input = "2+6"
print(user_input)
result = eval(user_input)
print(result)

#__import__('os').system('rm -rf /')

print("______________________________________")
def calc_persistance(l):
    return 4*l
def calc_area(l):
    return l**2

expr = input("podaj nazwę i parametry funkcji: ")
for l in range(5,55,5):
    if expr == "calc_persistance(l)":
        print(f'długosc boku działki = {l} m-> obwód -> {eval(expr)} m')
    elif expr == "calc_area(l)":
        print(f'długosc boku działki = {l} m -> pole działki -> {eval(expr)} m2')
    else:
        print("niewłaściwa nazwa funkcji lub prametrów...")
        break


#funkcja exec
mojkod = """
a=5
b=9
wynik = a+b**3
print(f'wynik = {wynik}')
"""
print(mojkod)
exec(mojkod)

cd = input("pisz co chcesz... ")
exec(cd)

user_input = "ls -la"
subprocess.run(user_input,shell=True)
