def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total+=num   # Style issue: missing spaces
    return total     # No type hints

def process_data(data=None):   # Potential bug: mutable default
    if data:
        return data.process()   # No error handling