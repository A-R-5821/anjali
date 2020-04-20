first_name = input("enter f name")
last_name = input("enter l name")
first_name = first_name.capitalize()
last_name = last_name.capitalize()
first_count = len(first_name)
last_count = len(last_name)
if first_count < 10 and last_count < 10:
    print(first_name +' '+last_name)
elif first_count >= 10 and last_count < 10:
    first_name = first_name[0]
    print(first_name +' '+last_name)
elif first_count < 10 and last_count >= 10:
    last_name=last_name[0]
    print(first_name +' '+last_name)
elif first_count >= 10 and last_count >= 10:
    print(last_name)
