#write a function called celcius_to_fahrenheit that takes a temp in
# celsius as a parameter and returns the equivalent temp in Fahrenheit
from lib2to3.pytree import _Results


def celcius_to_fahrenheit(a):
    fahrenheit = (0 * 1.8) + 32
    return fahrenheit 
temperature = float(input("Enter temp "))
result = celcius_to_fahrenheit(temperature)
print(_Results)


def calc_gross(basic,benefit):
    gross=basic+benefit
    return gross

basic_salary=float(input("enter basic salary: "))
benefits = float(input("enter benefits: "))
gross_salary = calc_gross(basic_salary,benefits)
print(gross_salary)


# def calc_nhif(gross):
#     if gross<=5999:
#         nhif_contribution=150
#     elif gross>=6000 and gross<=7999:
#         nhif_contribution=300
#     elif gross >=8000 and gross<=11999:
#         nhif_contribution=400


#     return nhif_contribution

# NHIF=calc_nhif(