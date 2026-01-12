def validate_data(data):
    """
   in this code we check int value . in python we written int value without quotes eg- (30) and here we written 25 in "" quotes.
   remember:-
   Without quotes → int → valid,
   With quotes → string → not int
    """
    invalid_entries = []

    for entry in data:
        age = entry.get("age")
        if not isinstance(age, int):
            invalid_entries.append(entry)

    return invalid_entries


if __name__ == "__main__":
    sample_data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": "25"}
    ]

    result = validate_data(sample_data)
    print("Invalid entries:", result)
