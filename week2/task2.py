s1 = "Wajihah2004"

digits = [int(char) for char in s1 if char.isdigit()]

if len(digits) > 0:
    total_sum = sum(digits)
    average = total_sum / len(digits)
    print(f"Sum: {total_sum}, Average: {average}")
else:
    print("No digits found.")