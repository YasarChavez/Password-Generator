import random
import time
# Welcome message.
print("Welcome to Password Generator!")
print("Made with love by YasarChavez")
print("https://github.com/YasarChavez")
print("")
# Generate password with given length.
length = int(input("Choose the password length: "))
password = ""
# Ask password name
password_name = input("Choose a name for the password, for example *Facebook*: ")
for i in range(length):
    password += chr(random.randint(33, 126))
print(" ")
print("Your password is:")
print(password)

# Check if password is strong.
def check_password(password):
    if len(password) < 8:
        return False
    if password.isalpha():
        return False
    if password.isdigit():
        return False
    return True
# Save password to a file.
if check_password(password):
    print(" ")
    print("Strong password!")
    print("Your password have more than 8 digits and is not only letters")
    print(" ")
    print("Password saved to password.txt")
    with open("password.txt", "a") as f:
        f.write(password_name + ": " + password + "\n")
        f.close()
else :
    print(" ")
    print("Weak password!")
    print("Please generate a strong password with more than 8 digits.")
    print(" ")
    print("Password saved to password.txt")
    with open("password.txt", "w") as f:
        f.write(password_name + ": " + password + "\n")
        f.close()
# Wait 5 seconds before closing.
print(" ")
print("***************************************")
print("*Remember to keep your passwords safe!*")
print("***************************************")
print(" ")
print("Program will close in 10 seconds.")
time.sleep(10)

# Close the program.
exit()