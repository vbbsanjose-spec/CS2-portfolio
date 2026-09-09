# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator
**Name:**   Vince Bryll B. Sa Jose
**Section:** Dahlia
**Quarter:** 1

## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements

| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | text | Presence validation|""(blank)|Name must not be blank |Please enter a proper name|
| Age | whole number| Data Type & Acceptable Value Validation| abc or -5| age must be a number from 11 to 18| Please enter a valid age from 11 to 18.|
| Grade Level | whole number| Acceptable Value Validation | 13 | Grade level must be between 7 and 12. | Please enter a grade level from 7 to 12.|
| Email Address | text in email format| Pattern Validation|
student@email | Email must contain @ and .| Please enter a valid email address.|
| Registration Code | text with 6 characters| Length Validation| ABC12| Registration code must contain exactly 6 characters.| Registration code must be exactly 6 characters.|
---
## Validation Questions
### 1. Why should the student name not be blank?
> A student name is required so the program can identify the student and avoid having incomplete information.
### 2. Why should age be checked for both data type and range?
> Checking the data type stops the program from crashing if someone types letters instead of numbers. Checking the range ensures the age is realistic and not a negative number.
### 3. Why should grade level only accept specific values?
> Limiting the grade level to specific values prevents invalid entries and ensures that the information matches the available grade levels.
### 4. What format requirements did you use for the email address?
> The email address should contain an “@” and "." symbol.
### 5. What length requirement did you use for the registration code?
> The registration code must have a specific number of characters, which is 6, to ensure that it follows the required format and helps prevent invalid codes.
---
# Part B - Program Design
## Pseudocode

```text
START

Set "valid" to TRUE

INPUT student name

Enter age
Enter grade level
Enter email address
Enter registration code

IF name is blank THEN
DISPLAY "Invalid Answer. The name must not be blank."
Set "valid" to FALSE
END IF

IF age is less than 11 OR age is greater than 18 THEN
DISPLAY "Age must be from 11 to 18"
Set "valid" to FALSE
END IF

IF grade level is less than 7 OR grade level is greater than 12 THEN
DISPLAY "Invalid grade level."
Set "valid" to FALSE
END IF

IF email does not contain "@" OR email does not contain "." THEN
DISPLAY "Invalid Email address. @ and . is required."
Set "valid" to FALSE
END IF

IF length of registration code is not equal to 6 THEN
DISPLAY "The registration code must contain exactly 6 characters."
Set "valid" to FALSE
END IF

IF "valid" is TRUE THEN
DISPLAY "REGISTRATION ACCEPTED"
DISPLAY student name
DISPLAY age
DISPLAY grade level
DISPLAY email
DISPLAY registration code
ELSE
DISPLAY "REGISTRATION NOT ACCEPTED"
END IF

END
```


# Part C - Program Implementation
## Programming Language
> I used python as my programming language 
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
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
  print("Age must be from 11 to 18") 
  valid = False 

if grade_level < 7 or grade_level > 12:
  print("Invalid grade level.") 
  valid = False 

if "@" not in email or "." not in email: 
  print("Invalid Email address. @ and . is required.")
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

```

---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> I used the presence validation in asking for the name of the student.
### Data Type Validation
Explain where you used data type validation.
> I used data type validation for the age and grade level to make sure the input is a number.
### Range Validation
Explain where you used range validation.
> I used range validation for the age and grade level to make sure they are within the allowed range.

### Acceptable Value Validation
Explain where you used acceptable value validation.
> I used acceptable value validation for the grade level, allowing only grades 7 to 12.
### Pattern Validation
Explain the simple pattern rule you used.
> I used pattern validation for the email, checking if it contains "@" and ".".
### Length Validation
Explain the length rule you used.
> I used length validation for the registration code, making sure it has exactly 6 characters.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | | |PASS|
| 2 | Blank student name | Presence | | |PASS|
| 3 | Age = `fourteen` | Data type | | | PASS|
| 4 | Age = `11` | Minimum boundary | | | PASS|
| 5 | Age = `18` | Maximum boundary | | |PASS|
| 6 | Age = `10` | Range | | | PASS|
| 7 | Grade Level = `13` | Acceptable value | | |PASS|
| 8 | Email = `studentpshs.edu.ph` | Pattern | | |PASS|
| 9 | Registration Code = `ABC` | Length | | | PASS|
| 10 | Registration Code = `CS2026` | Valid length | | | PASS|
Write **PASS** when the actual output matches the expected output.
Write **FAIL** when it does not.
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Write the input here.

```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 2
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 3
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**

```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> A program should validate input before processing it to make sure the information entered is correct, complete, and follows the required format. This helps prevent errors and makes the program more reliable.
### 2. What is the difference between input validation and output verification?
> Input validation checks whether the data entered by the user is valid before the program processes it. Output verification checks whether the program produces the correct result after processing the input.
### 3. Which validation technique was easiest for you to implement? Why?
> Presence validation was the easiest for me to implement because I only needed to check if the name part was left blank.
### 4. Which validation technique was most challenging? Why?
> Pattern validation was the most challenging because I needed to make sure that the input in the email address must follow a specific format.
### 5. How did testing invalid inputs help you improve your program?
> Testing invalid inputs helped me find errors and weaknesses in my program. It allowed me to improve the validation so that the program could properly handle incorrect or unexpected data.
---

