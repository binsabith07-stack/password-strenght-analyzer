import random
import string

def check_password(password):
    score = 0

    # Check lenght
    if len(password) >= 8:
        score += 1

    # Check uppercase letter
    if any(char .isupper() for char in password):
        score += 1

    # Check lowercase letter
    if any (char .islower()for char in password):
        score += 1

    # Check number
    if any(char.isdigit() for char in password):
        score += 1

    # Check special character
    if any(char in "!@#$%^&*" for char in password):
        score += 1

    # Check repeated characters
    if len(set(password)) == len(password):
        score += 1

    return score


def suggest_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ""

    for i in range(10):
        password += random.choice(characters)

    return password


print("================================")
print("     PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter your password: ")

score = check_password(password)

print("\nPassword Analysis")
print("-----------------")
print("Password length:", len(password))

if len(password) < 8:
    print("✗ Password should contain at least 8 characters")
else:
    print("✓ Good password length")

if any(char.isupper() for char in password):
    print("✓ Contains uppercase letter")
else:
    print("✗ Add an uppercase letter")

if any(char.islower() for char in password):
    print("✓ Contains lowercase letter")
else:
    print("✗ Add a lowercase letter")

if any(char.isdigit() for char in password):
    print("✓ Contains a number")
else:
    print("✗ Add a number")

if any(char in "!@#$%^&*" for char in password):
    print("✓ Contains special character")
else:
    print("✗ Add a special character")

if len(set(password)) == len(password):
    print("✓ No repeated characters")
else:
    print("✗ Password contains repeated characters")


print("\nStrength:")

if score <= 2:
    print("WEAK")
elif score <= 4:
    print("MEDIUM")
else:
    print("STRONG")


print("\nSuggested stronger password:")
print(suggest_password())# Auto detect text files and perform LF normalization
* text=auto
