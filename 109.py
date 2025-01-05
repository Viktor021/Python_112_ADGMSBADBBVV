email = input("Enter Your Email: ")

email = email.strip()

slicer_index = email.index("@")

username = email[:slicer_index]
domain_name = email[slicer_index+1:]

print("Your user name is ", username, " and your domain is ", domain_name)