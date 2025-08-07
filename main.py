def average(nums):
    """Calculate the average of a list of nums."""
    if not nums:
        return 0
    return sum(nums) / len(nums)

def median(nums):
    """Calculate the median of a list of integers."""
    n = len(nums)
    if n == 0:
        return 0
    nums_sorted = sorted(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums_sorted[mid - 1] + nums_sorted[mid]) / 2
    else:
        return nums_sorted[mid]

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm says hello')
    numbers = [10, 20, 30, 40, 50]
    # avg = average(numbers)
    # print(f'The average of {numbers} is {avg}')
    med = median(numbers)
    print(f'The median of {numbers} is {med}')