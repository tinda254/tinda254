# Get user's name
name = input("What is your name? ")

# Get user's age as a string (input() always returns a string)
age_str = input("How old are you? ")

# Convert age to an integer (if using the age for calculations)
age = int(age_str)  # Assuming the user enters a valid integer

# Get user's location
location = input("Where do you live? ")

# Personalized message
message = f"Hello {name}, you are {age} years old and live in {location}."

print(message)
