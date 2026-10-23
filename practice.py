
# This code finds two numbers in a list that add up to a target value (100 in this case) and prints their indices. It uses a dictionary to keep track of the numbers seen so far and their corresponding indices. If a complement (the number needed to reach the target) is found in the dictionary, it prints the indices of the two numbers. If no such pair exists, it prints "No pair found."
#time complexity is O(n) and space complexity is O(n)


numbers = [55, 23, 78, 12, 34, 90, 67, 45, 89, 10]
target = 100

# Dictionary to store {number: index}
seen = {}
pair_found = False

for i, num in enumerate(numbers):
    complement = target - num
    
    # If the complement is already in our dictionary, we found a pair!
    if complement in seen:
        print(f"the number is: {seen[complement]},{i}")
        pair_found = True
        break  # Exit early since we found the best/first pair
    
    # Otherwise, save the current number and its index
    seen[num] = i

if not pair_found:
    print("No pair found.")
