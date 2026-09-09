valid = True 

name = str(input("Enter student name: ")) 

if name == "": print("Invalid Answer. Name must not be blank. Put a proper student name.") valid = False age = int(input("Enter your age(from 11-18 only): ")) if age < 11 or age > 18: print("Age must be from 11 to 18") valid = False grade_level = int(input("Enter your grade level(from 7-12 only): ")) if grade_level < 7 or grade_level > 12: print("Invalid grade level.") valid = False email = str(input("Enter your email adress (template: student@brc.pshs.edu.ph): ")) if "@" not in email or "." not in email: print("Invalid Email address. @ and . is required.") valid = False registration_code = str(input("Enter your registration code: ")) if len(registration_code) > 6 or len(registration_code) < 6: print("The registration code must contain exactly 6 characters.") valid = False if valid: print("------------------------------") print(" REGISTRATION ACCEPTED ") print("------------------------------") print(f"Student: {name}") print(f"Age: {age}") print(f"Grade Level: {grade_level}") print(f"Email: {email}") print(f"Registration Code: {registration_code}") else: print("REGISTRATION NOT ACCEPTED")

