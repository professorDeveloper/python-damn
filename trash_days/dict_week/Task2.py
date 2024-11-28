# Task2
# Country & Capital Sorted
country = {"America":"Washington","UK":"London","Uzbekistan":"Tashkent","Russian":"Moscow","China":"Pekin","Japan":"Tokyo","Korea":"Seoul"}
capital_list = list(country.values())
capital_list.sort()
print("======= Capitals Sorted List =======")
for capital_country in capital_list:
    print(capital_country)
country_list = list(country.keys())
country_list.sort()
print()
print("======= Countries Sorted List =======")
for country_country in country_list:
    print(country_country)
# Done