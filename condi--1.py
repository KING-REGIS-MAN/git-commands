# Accept time from the user in 24-hour format
time = int(input("Enter the time in 24-hour format (0-23): "))

# Check the time and greet the user accordingly
if 5 <= time < 12:
    print("Good Morning!")
elif 12 <= time < 17:
    print("Good Afternoon!")
elif 17 <= time < 21:
    print("Good Evening!")
elif (21 <= time <= 23) or (0 <= time < 5):
    print("Good Night!")
else:
    print("Invalid time! Please enter a value between 0 and 23.")
# Output: Good Morning!
# Output: Good Afternoon!
# Output: Good Evening!
# Output: Good Night!
# Output: Invalid time! Please enter a value between 0 and 23.