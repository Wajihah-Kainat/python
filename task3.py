# 1. Convert an integer to a floating-point number.
num_int = 25
converted_to_float = float(num_int)
print("1. Integer to Float:", converted_to_float, type(converted_to_float))

# 2. Convert a floating-point number to an integer[cite: 1].
num_float = 9.99
converted_to_int = int(num_float)
print("2. Float to Integer:", converted_to_int, type(converted_to_int)) 
# Note: Converting float to int just chops off the decimal, it doesn't round!

# 3. Convert an integer to a string[cite: 1].
converted_to_str = str(num_int)
print("3. Integer to String:", converted_to_str, type(converted_to_str))

# 4. Convert a string containing a number to an integer[cite: 1].
string_num = "100"
str_to_int = int(string_num)
print("4. String to Integer:", str_to_int, type(str_to_int))

# 5. Convert an integer to a Boolean[cite: 1].
# In Python, 0 is False, and any other number is True.
converted_to_bool = bool(num_int)
print("5. Integer to Boolean:", converted_to_bool, type(converted_to_bool))