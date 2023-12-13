try:
    integer=int(input("enter a number"))
    if integer<90 or integer>120:
        raise ValueError("Abnormal Condition")
    else:
        print("input is in range between 90 and 120")
except ValueError as e:
        print("Value error",e)
        
