# Function to format employee ID
def format_employee_id(emp_number):
    return f"DL-EMP-{emp_number:05}"


employee_number = 15
formatted_id = format_employee_id(employee_number)
print("Formatted Employee ID:", formatted_id)
