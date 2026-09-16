import string

def check_password_strength(password):
    # Length validation rule (< 8 chars immediate fail risk)
    if len(password) < 8:
        return "Weak (Reason: Password must be at least 8 characters long)"
    
    # Pythonic checks using C-optimized built-ins and short-circuit execution
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    
    # Score calculation based on variety
    criteria_met = sum([has_upper, has_lower, has_digit, has_symbol])
    
    if criteria_met == 4 and len(password) >= 12:
        return "Strong"
    elif criteria_met >= 3 and len(password) >= 8:
        return "Medium"
    else:
        return "Weak (Reason: Needs a mix of uppercase, lowercase, numbers, and symbols)"

# Example usage:
user_input = input("Enter a password to evaluate: ")
print(f"Risk Classification: {check_password_strength(user_input)}")