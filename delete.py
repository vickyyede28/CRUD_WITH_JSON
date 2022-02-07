# import os,json
# import delete

# def delete():
#     if (os.path.exists("win.json")):
#         with open("win.json","r") as p:
#             a=json.load(p)
#             s=+0
#             d=input("enter your del email:--  ")
#             for f in a:
#                 s=+1
#                 for g in f.values():
#                     if g==d:
#                         a.pop(s-1)
#                         with open("win.json","w") as j:
#                             json.dump(a,j,indent=4)
#     else:
#         with open("win.json","w") as k:
#             k.write("[]")


# delete()