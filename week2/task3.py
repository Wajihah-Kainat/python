original_list = [
    {'make': 'Google', 'model': 216, 'color': 'Black'}, 
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# The lambda function tells the sort method to look specifically at the 'color' key
sorted_list = sorted(original_list, key=lambda x: x['color'])

print("Sorting the List of dictionaries:", sorted_list)