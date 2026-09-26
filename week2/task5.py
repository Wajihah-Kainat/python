# Creating the dictionary mapping event names to their dates
dortmund_events = {
    "Dortmund Chess Tournament": "10th August 2026",
    "Night of Museums": "19th September 2026",
    "Westfalenpark Light Festival": "19th September 2026",
    "Christmas Market Opening": "17th November 2026"
}

target_date = "19th September 2026"

print(f"Events on {target_date}:")

# We use the items() method to return the dictionary's items in (key, value) format[cite: 10]
for event, date in dortmund_events.items():
    if date == target_date:
        print("-", event)