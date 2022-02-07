# import update
# import json,os
# def update():
#     if (os.path.exists("win.json")):
#         with open("win.json","r") as r:
#             t=json.load(r)
#             m=int(input("enter your mobile "))
#             for y in t:
#                 for u in y.values():
#                     if m==u: 
#                         y["name"]=input("enter your new name:-- ")
#                         y["email"]=input("enter your new email:--")
#                         y["password"]=input("enter your new password:-- ")

#                         # t.append(y)
#                 with open("win.json","w") as i:
#                     json.dump(t,i,indent=4)
#     else:
#         with open("win.json","w") as o:
#             o.write("it is wrong")

# update()



















