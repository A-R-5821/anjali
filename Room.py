first_name = input("Enter your first_name")
first_name = first_name.capitalize()
if first_name[0]=='A' or first_name[0]=='B':
    print("""Room AB is alotted to you
          Thankyou for coming""")
elif first_name[0]=='C':
    print("""Room CD is alotted to you
          Thankyou for coming""")
else :
    last_name=input("Enter your last_name")
    last_name=last_name.capitalize()
    if last_name[0]=='Z':
        print("""Room Z is alotted to you
          Thankyou for coming""")
    else:
        print("Go To OTHER Room")
