string_list = ["Python", "Dortmund", "Code"]

# Apply the list() function to each string in string_list
mapped_result = map(list, string_list)

# Convert the final map object into a list to print it
final_list = list(mapped_result)

print("List of lists:", final_list)