# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Attempt to divide
        result = num / denom

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

    return f"The result of the division is {result:.2f}"
