"""Q1 - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not."""

statuscode =int(input("Enter the Status Code\n").strip())
if statuscode == 200:
    print("✅ Passed API Request")
elif statuscode == 404:
    print("❌ Failed API Request")
else:
      print("Please enter a valid status code")



