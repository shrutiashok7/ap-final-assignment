class InvalidRollException(Exception):
    def __init__(self, message="Invalid roll number format"):
        self.message = message
        super().__init__(self.message)

def fee(base_fee, roll_number):
    if len(roll_number) != 7:
        raise InvalidRollException("Roll number must be 7 characters long")
    
    valid_departments = ["DS", "CS", "EE", "ME", "CE"]
    department = roll_number[0:2]
    
    if department not in valid_departments:
        raise InvalidRollException("Invalid department code")
    
    try:
        admission_year = int(roll_number[2:4])
        program_type = int(roll_number[4:5])
        roll_id = int(roll_number[5:7])
    except ValueError:
        raise InvalidRollException("Invalid numerical values in roll number")
    
    if program_type != 1 and program_type != 2:
        raise InvalidRollException("Program type must be 1 (B.Tech) or 2 (M.Tech)")
    
    admission_year += 2000
    current_year = 2023
    
    if admission_year > current_year:
        raise InvalidRollException("Admission year cannot be in the future")
    
    program_duration = 4 if program_type == 1 else 2
    graduation_year = admission_year + program_duration
    
    if graduation_year <= current_year:
        years_to_pay = program_duration
    else:
        years_to_pay = current_year - admission_year + 1
    
    total_fee = 0
    current_fee = base_fee
    
    for year in range(years_to_pay):
        total_fee += current_fee
        current_fee += current_fee * 0.1
    
    return int(total_fee)

def main():
    test_cases = [
        (100000, 'CS20143'),
        (100000, 'DS18243'),
        (100000, 'EE16243')
    ]
    
    for base, roll in test_cases:
        try:
            result = fee(base, roll)
            print(f"fee({base}, '{roll}') -> {result}")
        except InvalidRollException as e:
            print(f"fee({base}, '{roll}') -> {e.__class__.__name__}")

if __name__ == "__main__":
    main()