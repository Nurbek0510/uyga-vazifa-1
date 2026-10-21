ism = input("Ism: ")
familiya = input("Familiya: ")

username = ism[:3] + "_" + familiya[:3]
username = username.lower()

print("Username:", username)