def computePower(x,y):
    result = 1
    for _ in range(y):
        result *=x
    return result
x = 2
y = 3
print(computePower(x,y))

def temperatureRange(readings):
    return (min(readings), max(readings))
readings = [15, 14, 17, 20, 23, 28, 20]
print(temperatureRange(readings))

def isweekend(day):
    return day ==6 or day ==7
day = 6
print(isweekend(day))

day = 1
print(isweekend(day))



def fuel_efficiency(distance, fuel):
    return round(distance / fuel, 2)
distance = 70
fuel = 21.5
print(fuel_efficiency(distance, fuel))

def decodeNumbers(n):
    last_digit = n % 10
    remaining_number = n // 10
    num_digits = len(str(remaining_number))
    result = last_digit * (10**num_digits) + remaining_number
    return result
n = 12345
print(decodeNumbers(n))

def find_max_with_for_loops(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value
nums = [2024, 98, 131, 2, 3, 72]
print(find_max_with_for_loops(nums))

def find_min_with_for_loops(nums):
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value
nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loops(nums))

def find_min_with_while_loop(nums):
    min_value = nums[0]
    i = 1
    while i <len(nums):
        if nums[i] < min_value:
            min_value = nums[i]
        i += 1
    return min_value
print(find_min_with_while_loop(nums))

def find_max_with_while_loops(nums):
    max_value = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > max_value:
            max_value = nums[i]
        i += 1
    return max_value 
nums = [2024, 98, 131, 2, 3, 72] 
print(find_max_with_while_loops(nums))  

def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else: 
                consonant_count +=1
    return (vowel_count, consonant_count)
text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))

def digital_root(num):
    num = abs(num)
    digit_sum = 0 

    while num > 0:
        digit_sum += num % 10
        num //= 10 
    return digit_sum 
num = 2468
print(digital_root(num))
num = 3    
