import json,os
# def read():
#     if (os.path.exists("win.json")):
#         with open("win.json","r") as n:
#             m=json.load(n)
#             e=input("which data your want to read for that \n enter your name:- ")
#             for i in m:
#                 for h in i.values():
#                     if e==h:
#                         print(i)
#                 with open ("win.json","w") as a:
#                     json.dump(m,a,indent=4)
#     else:
#         with open ("win.json","w") as k:
#             k.write("[]")
# read()