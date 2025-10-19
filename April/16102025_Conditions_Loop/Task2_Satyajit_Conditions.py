"""Q2 In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

Test Passed – Title matches
True - why > Strip and convert them into the lowercase = both of them are equal. """


expected_title = "Dashboard"
actual_title=input("Enter the title\n").strip()
if actual_title ==expected_title :
    print("✅ Test Passed – Title matches")
else:
    print("Title are not matching")



