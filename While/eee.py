while(True):
    name=input("Enter a name: ")
    if(name=="idan"):
        print("Hello idan")
        break
    elif(name=="ben"):
        continue
    else:
        print("Where is idan?")
    number=int(input("Enter a number:"))
    print(number*4)

print("Bye Bye...")
