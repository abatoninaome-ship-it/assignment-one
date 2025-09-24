import array

# Sample data: List of student records
students = [
    {'id': 1, 'name': 'Alice', 'value': 85},
    {'id': 2, 'name': 'Bob', 'value': 78},
    {'id': 3, 'name': 'Charlie', 'value': 92},
    {'id': 4, 'name': 'David', 'value': 67},
    {'id': 5, 'name': 'Eve', 'value': 74}
]

# ----------------------------------
# Integers: Compute total, average, min, max
# ----------------------------------
values = [student['value'] for student in students]

total = sum(values)
average = total / len(values)
minimum = min(values)
maximum = max(values)

# ----------------------------------
# Strings: Formatted report using f-strings
# ----------------------------------
print(f"\n--- Marks Analyzer Report ---")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Minimum Marks: {minimum}")
print(f"Maximum Marks: {maximum}")

# ----------------------------------
# Booleans: Apply a threshold condition
# ----------------------------------
threshold = 75
status = "Above Standard" if average > threshold else "Below Standard"
print(f"Class Performance: {status}")

# ----------------------------------
# Lists: Modify, sort, display
# ----------------------------------
print("\nOriginal List of Students:")
for student in students:
    print(student)

# Add new student
students.append({'id': 6, 'name': 'Frank', 'value': 81})

# Remove a student based on condition (value < 70)
students = [s for s in students if s['value'] >= 70]

# Sort by value
students.sort(key=lambda x: x['value'])

print("\nModified and Sorted List of Students:")
for student in students:
    print(student)

# ----------------------------------
# Arrays: Fixed-size array and sum
# ----------------------------------
marks_array = array.array('i', values[:5])  # Store only first 5 marks
array_sum = sum(marks_array)
print(f"\nArray (fixed-size subset): {marks_array.tolist()}")
print(f"Sum of array elements: {array_sum}")
print(f"Compare with original list sum: {total}")

# ----------------------------------
# Dictionaries: Update, delete, compute total again
# ----------------------------------

# Update a record (e.g., change Bob's marks to 88)
for student in students:
    if student['name'] == 'Bob':
        student['value'] = 88

# Delete a record (e.g., delete David if exists)
students = [s for s in students if s['name'] != 'David']

# Recalculate total from updated records
updated_total = sum(student['value'] for student in students)
print(f"\nUpdated Total Marks: {updated_total}")
