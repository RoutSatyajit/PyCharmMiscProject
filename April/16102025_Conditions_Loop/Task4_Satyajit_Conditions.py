"""Q4- Check if the user can log in based on correct username and password.

username = "admin"
password = "1234"
O/p
✅ Login Successful
For the Fail condition Other O/P = ❌ Invalid Credentials """


username=input("Enter the username\n").strip()
password=input("Enter the password\n")

if username == "admin" and password == "1234":
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")



