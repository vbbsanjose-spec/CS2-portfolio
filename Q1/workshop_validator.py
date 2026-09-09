valid = True

name = str(input("Enter student name: "))

age = int(input("Enter your age(from 11-18 only): ")) 

grade_level = int(input("Enter your grade level(from 7-12 only): "))

email = str(input("Enter your email address (template: student@brc.pshs.edu.ph): ")) 

registration_code = str(input("Enter your registration code(6 characters only): ")) 

if name == "": 
  print("Invalid Answer. The name must not be blank. Put a proper student name.") 
  valid = False 

if age < 11 or age > 18:
  print("Age must be from 11 to 18.") 
  valid = False 

if grade_level < 7 or grade_level > 12:
  print("Invalid grade level. It must be from 7 to 12") 
  valid = False 

if "@" not in email or "." not in email: 
  print("Invalid Email address, because @ and . is required.")
  valid = False

if len(registration_code) > 6 or len(registration_code) < 6: 
  print("The registration code must contain exactly 6 characters.") 
  valid = False 

if valid:
  print("------------------------------") 
  print(" REGISTRATION ACCEPTED ")
  print("------------------------------")
  print(f"Student: {name}") 
  print(f"Age: {age}") 
  print(f"Grade Level: {grade_level}") 
  print(f"Email: {email}") 
  print(f"Registration Code: {registration_code}")

else:
  print("REGISTRATION NOT ACCEPTED")

  
