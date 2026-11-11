#Contains basic input and output
fn= input("Enter first name: ")
ln= input("Enter last name: ")
s= input("Enter section: ")
fs= input("Enter favorite subject: ")

fullname= f"{fn} {ln}".title()
nc= f"{fullname}".upper()
section= f"{s}".upper()
favsub= f"{fs}".upper()
cc= len(fullname)


#Final Output

print(" ")
print("Formatted Output:")
print(f"Name: {fullname}")
print(f"Name Code: {nc}")
print(f"Section: {section}")
print(f"Favorite Subject: {favsub}")
print(f"Character Count: {cc}")
