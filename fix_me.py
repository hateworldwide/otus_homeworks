"""
docstring for pylint to fuck off - 1
"""

def calculate_average(nums):
    """docstring for pylint to fuck off - 2"""
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average

nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)