# # Dictionary (Map) in py
# dict = {1: 'one', 2: 'two', 3: 'three'}
# for e in dict:
#     print(e, dict[e], type(dict[e]))

# Dictionary app
# {
#     word:{
#         eng:str
#         uz:str,
#         isFavorite:bool,
#
#     }
#     likedWord {
#         eng:str
#         uz:str,
#     }
#     totalWord:int
# }
#
# Dictionary da key 1 marotaba ishlatilinadi

dict = {"students": {"azamov": {"name": "Saikou", "age": 18, }, "jack": {"name": "Jack", "age": 18}}}
for e in dict:
    for v in dict[e]:
        print(f"Student Name: {dict[e][v]['name']} | Age: {dict[e][v]['age']}")

# for key in dict:
# Dict bilan default for yozsak bizga keyni qaytaradi
# shuning uhcun key,value qilib foydalanishimiz kerak
#  yani for key,value in dict: kabi
dict['azamov']={'name':'Saikou','age':18}
print(dict)