def sum_of_numbers(*args):
    
    return sum(args)


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = sum_of_numbers(*numbers)
print("Sum:", result)
