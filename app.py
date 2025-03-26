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
#   intervar is a variable that takes the value of each element in the list in each iteration of the loop.
#   In the first iteration, intervar is 3, in the second iteration, intervar is 41, and so on.
#   The loop continues until all elements in the list have been exhausted.
#   The variable largest is used to keep track of the largest number found so far.
#   In each iteration, the current value of intervar is compared with the value of largest.
#   If intervar is greater than largest, then largest is updated to the value of intervar.
#   The loop continues until all elements in the list have been exhausted.
#   The value of largest is printed out after the loop has finished executing.

#  IN THE PROGRAM__ THE CONDITION IS intervar < smallest.

		