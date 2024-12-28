password = "bigbigbigcode"
typedpass = input("enter your password:")
if typedpass == password:
    print("access granted")
elif typedpass == "1234":
    print("only an idiot would have that as their password")
else:
    print("wrong password")
