import employee_info

def test_get_employees_by_age():
    age_lower_limit = 24
    age_upper_limit = 31

    test_result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}]

    result = employee_info.get_employees_by_age_range(age_lower_limit,age_upper_limit)
    assert result == test_result

def test_calculate_average_salary():
    test_result = 60167
    result = employee_info.calculate_average_salary()

    assert result == test_result

def test_get_employees_by_dept():
    dept = "Sales"

    test_result = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]

    result = employee_info.get_employees_by_dept(dept)
    assert result == test_result