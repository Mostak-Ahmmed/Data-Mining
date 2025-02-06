
# Lab TASK # 02

# Write a Python program which accepts a sequence of 
# comma-separated numbers from user and generate
# a list with those numbers.

nums = [int(i) for i in input("Enter comma-sep number: ").split(",")]
print("Generated list:", nums)
print("Type:", type(nums))
