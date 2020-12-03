joke  = " I Am So Famous .... ... . . . When I Go To The Mall. . . . The Door Opens Itself."
punchline = "I am So Famous"

print(f"The joke is:{joke}")
input()
print(f"Puchline is:{punchline}")


password = "123"
pw = ""
count = 0
max_count = 5
auth = False

while pw != password:
    count = count + 1
    if count > max_count:
        break
    pw = input(f"{count}:What is the password?")
else:
    auth = True

print("Authorized "if auth else"Account Locked")        
     