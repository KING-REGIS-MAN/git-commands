n = 2
while n < 10:  # Change condition to n < 10
    if n % 2 == 0:
        print(n)
    n = n + 1  # Increment n in each loop iteration
# Output: 2 4 6 8.
#friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'George', 'Harry', 'Isabel', 'Jack', 'Kylie', 'Lily']
#for friend in friends:
#    print('Happy New Month:', friend)
#    print('Done! BABY')
    
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total:', total)
# Output: 154

smallest = None
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
print('Smallest:', smallest)
# Output: 3

largest = None
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
print('largest:', largest)
		