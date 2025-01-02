
def second_maximum(numbers):
    numbers = list(set(numbers))  # Remove duplicates
    numbers.sort()  # Sort the list
    if len(numbers) < 2:  # Check if the list has less than 2 elements
        return None
    return numbers[-2]  # Return the second last element (second maximum)

n = int(input())
numbers = list(map(int, input().split()))

result = second_maximum(numbers)
if result is not None:
    print(result)
else:
    print("No second maximum")


