def count_digit_one(n):
    count = 0
    factor = 1
    i = 1

    while i <= n:
        divisor = i * 10
        count += (n // divisor) * i + min(max(n % divisor - i + 1, 0), i)
        i *= 10

    return count

# Take user input
user_input = int(input("Enter a non-negative integer (n): "))

# Calculate and print the result
result = count_digit_one(user_input)
print(f"Input: {user_input}\nOutput: {result}")

