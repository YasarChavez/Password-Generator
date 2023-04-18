import random
import time
# Welcome message.
print("Welcome to Password Generator!")
print("Made with love by YasarChavez")
print("https://github.com/YasarChavez")
print("")
# Generate password with given length.
length = int(input("Enter the length of password: "))
password = ""
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
    print("Your password have more tha 8 digits and is not only letters")
    print("Password saved to password.txt")
    with open("password.txt", "w") as f:
        f.write(password)
        f.close()
else :
    print(" ")
    print("Weak password!")
    print("Please generate a strong password with more than 8 digits.")
    print("Password saved to password.txt")
    with open("password.txt", "w") as f:
        f.write(password)
        f.close()
# Wait 10 seconds before closing.
print(" ")
print("Program will close in 5 seconds.")
time.sleep(5)
# Close the program.
exit()