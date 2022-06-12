def grades_info(number):
    if number < 3:
        return "Fail"
    elif number < 3.5:
        return "Poor"
    elif number < 4.5:
        return "Good"
    elif number < 5.5:
        return "Very Good"
    else:
        return "Excellent"


number = float(input())
print(grades_info(number))
