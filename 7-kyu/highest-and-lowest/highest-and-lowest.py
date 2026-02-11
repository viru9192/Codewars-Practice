def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    small = min(nums)
    large = max(nums)
    return f"{large} {small}"