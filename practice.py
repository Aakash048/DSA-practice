#=====Two sum ======

numbers = [55, 23, 78, 12, 34, 90, 67, 45, 89, 10]
target = 100

def find_pair(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return numbers[i], numbers[j]
    return None

result = find_pair(numbers, target)
if result:
    print(f"Pair found: {result[0]} and {result[1]}")
else:
    print("No pair found.")