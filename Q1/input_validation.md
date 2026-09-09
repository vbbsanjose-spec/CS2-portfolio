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
Complete the table below before writing your program.
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Student Name | | | | | |
| Age | | | | | |
| Grade Level | | | | | |
| Email Address | | | | | |
| Registration Code | | | | | |
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
Before writing your program, create either a **flowchart or pseudocode** showing its logic.
## Flowchart
Insert your flowchart below.
![Workshop Validator Flowchart](workshop_validator_flowchart.png)
OR
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

Your design should show:
- user input
- validation decisions
- error messages
- accepted registration
- rejected registration.
---
# Part C - Program Implementation
## Programming Language
> Write the programming language used.
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
# Paste your final code here.
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
> Write your answer here.
### Pattern Validation
Explain the simple pattern rule you used.
> Write your answer here.
### Length Validation
Explain the length rule you used.
> Write your answer here.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | | | |
| 2 | Blank student name | Presence | | | |
| 3 | Age = `fourteen` | Data type | | | |
| 4 | Age = `11` | Minimum boundary | | | |
| 5 | Age = `18` | Maximum boundary | | | |
| 6 | Age = `10` | Range | | | |
| 7 | Grade Level = `13` | Acceptable value | | | |
| 8 | Email = `studentpshs.edu.ph` | Pattern | | | |
| 9 | Registration Code = `ABC` | Length | | | |
| 10 | Registration Code = `CS2026` | Valid length | | | |
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
> Write your answer here.
### 2. What is the difference between input validation and output verification?
> Write your answer here.
### 3. Which validation technique was easiest for you to implement? Why?
> Write your answer here.
### 4. Which validation technique was most challenging? Why?
> Write your answer here.
### 5. How did testing invalid inputs help you improve your program?
> Write your answer here.
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- `input_validation.md`
- `workshop_validator_flowchart.png` if a flowchart was used
