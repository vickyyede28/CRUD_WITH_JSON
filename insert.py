# import insert
# import os
# import json
# def insert():
#     if (os.path.exists("win.json")):
#         with open("win.json","r") as q:
#             b=json.load(q)
#             w={}
#             w["name"]=input("enter your name:--")
#             w["email"]=input("enter your email:--")
#             w["password"]=input("enter your password:--")
#             w["mobile"]=int(input("enter your mobile:--"))
#             b.append(w)
#             with open("win.json","w") as e:
#                 json.dump(b,e,indent=4)
#     else:
#         with open("win.json","w") as r:
#             r.write("[]")
# insert() 


