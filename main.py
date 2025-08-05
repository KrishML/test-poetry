def average(nums):
    """Calculate the average of a list of nums."""
    if not nums:
        return 0
    return sum(nums) / len(nums)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm says hello')
    numbers = [10, 20, 30, 40, 50]
    avg = average(numbers)
    print(f'The average of {numbers} is {avg}')