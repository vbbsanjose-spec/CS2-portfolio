# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** Vince Bryll B. San Jose
**Section:** Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and appropriate input.
---
# Part A - Cybersecurity Threat Analysis
## Assigned Case

**Case Number:**
**Case Title:** Fake Login Alert
> A message claims that the student's account will be disabled and asks them to click a link and enter their
username and password.
---
### 1. What cybersecurity threat is shown?
> The cybersecurity threat being illustrated here is Phishing, where an attacker uses a fake message in order to get an individual's login  information.
### 2. What warning signs make the situation suspicious?
> Signs that make the situation suspicious:
> - It creates a sense of urgency by saying that the account will be disabled
> - It asks the student to click an unfamiliar link
> - It requires sensitive login info such as username and password
> - The message may come from an anonymous and suspicious sender
### 3. What may be affected?
> - Data - The attacker asks for the student's login information which can be invased and leaked.
> - Account - The student's account could be taken over.
> - Application - School applications connected to the account could be accessed.
> - Device - A malicious link could potentially lead to harmful downloads or other attacks.
> - Network - A compromised account or device could create additional security risks on the school network.
> - Financial information - While the fake login message may not directly request financial information, an attacker who gains access to an account could potentially use the account to target other information or services.
### 4. What information could be exposed or misused?
> The student's username and password could be stolen. If the attacker successfully accesses the school account, they may also gain access to information stored in that account.
### 5. What should the user do to reduce the risk?
> - The student should:
> - Not click the suspicious link.
> - Not enter their username or password into the linked page.
> - Verify the message using an official school channel.
> - Report the suspicious message to the appropriate teacher, school administrator, or IT personnel.
> - Delete or safely ignore the message after reporting it.
> - If credentials were already entered, immediately report the incident and change the affected password through the official school system.
---
# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.
| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | Collect | It gives the registration system an proper way to identify the student|
| Section | Collect | It also provides easier process of identifying a student|
| Club Choice | Collect | The whole point of the system is to collect the preferred club of each student |
| School Email | Collect | So the system can have contact with the student |
| Attendance Status | Collect | To record the student's attendance status.|
| Password | Do not collect | It is not needed and a system member may invade the account of the student|
| OTP | Do not collect | An OTP is authentication information and is unnecessary for this activity. |
| Home Address | Do not collect | Financial information is unrelated to club registration and is highly sensitive. |
| Parent Bank Account | Do not collect | 	Not needed and is sensitive information. |
---
## Privacy Question
Why is it safer to collect only information that the program actually needs?
> Because collecting unnecessary information will not contribute anything to the system. In addition to that, these nonessential information can be dangerous when shared to someone that may have possibly bad intensions with it. Finally, collecting more data can be hassle and messy when organizing.
---
# Part C - Security-Focused Validation Rules

| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | A non-blank student name | Missing registration information | [blank] or blank input | Remove surrounding spaces and require at least one character | Student Name is required |
| Section | Ilang-ilang, Rosal, Sampaguita, or Dahlia (teacher approved)| Wrong section | Lily | Must be an approved section | Please enter a valid section |
| Club Choice | 	Robotics, Science, Mathematics, or Programming| Wrong club | Gaming | Must be an approved club| Please enter a valid club|
| School Email | 	Email with @ and . | Wrong email | vbbsanjose.brc.pshs.eduph | 	Must contain @ and .| 	Please enter a valid school email. |
| Attendance Status | Present, Absent, or Late | Wrong attendance | Secret |  Must be a valid status | 	Please choose a valid attendance status.|
---
## Secure Data Capture Questions
### 1. What should your program accept?
> It should accept a valid name, section, club, school email, and attendance status.
### 2. What should your program reject?
> It should reject blank names and invalid sections, clubs, emails, and attendance statuses.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> It contributes to the efficiency of the program by preventing incorrect information from being accepted into the program.
---
# Part D - Secure Program Implementation
## Program
Create a simple **PSHS Club Registration System**.
The program should collect only:
- Student Name
- Section
- Club Choice
- School Email

- Attendance Status
It should **not request passwords, OTPs, banking information, or unnecessary personal information**.
---
## Source Code File
[`secure_registration.py`](secure_registration.py)
---
## Final Code
```python
# # PSHS Secure Club Registration System

valid_sections = ["Sapphire", "Emerald", "Jade", "Diamond", "Ilang-ilang", "Dahlia", "Rosal", "Sampaguita", "Beryllium", "Platinum", "Magnesium", "Silicon", "Gluon", "Electron", "Proton", "Photon", "Graviton", "Biology", "Physics", "Bio-Chemistry", "Chemistry"]
valid_clubs = ["Robotics", "Science", "Mathematics", "Programming"]
valid_attendance = ["Present", "Absent", "Late"]


student_name = input("Student Name: ").strip().title()

while student_name == "":
    print("Student name is required.")
    student_name = input("Student Name: ").strip().title()


section = input("Section: ").strip().title()

while section not in valid_sections:
    print("Please choose a valid section.")
    section = input("Section: ").strip().title()


club = input("Club Choice: ").strip().title()

while club not in valid_clubs:
    print("Please choose a valid club.")
    club = input("Club Choice: ").strip().title()


email = input("School Email: ").strip().title()

while "@" not in email or "." not in email:
    print("Please enter a valid school email.")
    email = input("School Email: ").strip().title()


attendance = input("Attendance Status: ").strip().title()

while attendance not in valid_attendance:
    print("Please choose a valid attendance status.")
    attendance = input("Attendance Status: ").strip().title()


print("--------------------------------")
print("REGISTRATION ACCEPTED")
print("--------------------------------")
print("Student:", student_name)
print("Section:", section)
print("Club:", club)
print("Email:", email)
print("Attendance:", attendance)

```
---
## Security Practices Applied
### Required Input
> The student name is checked after removing surrounding spaces. If the input is blank, the program displays an error message and asks for the name again.
### Allowed Values
> The program uses lists for the accepted inputs. The while conditions check if the input is acceptable, and it includes .title() and .strip().
### Format Check
> The program makes the student re-enter an email account when @ and . is missing.
### Error Messages
> Clear error messages helps the students clearly understand their mistake their input
### Data Minimization
> The program only collects information needed for the club registration. It does not collect passwords, OTPs, home addresses, or banking information, because of safety and managing issues.
---
# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | | | |
| 2 | Blank student name | | | |
| 3 | Invalid section | | | |

| 4 | Invalid club choice | | | |
| 5 | Email missing `@` | | | |
| 6 | Email missing `.` | | | |
| 7 | Invalid attendance status | | | |
| 8 | Different valid inputs | | | |
Use:
- **PASS** if the actual result matches the expected result.
- **FAIL** if it does not.
---
# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> Write your answer here.
### 2. How can users reduce the risk of phishing or suspicious messages?
> Write your answer here.
### 3. How can validation rules improve the security of user input?
> Write your answer here.
### 4. Why should a program avoid collecting unnecessary personal information?
> Write your answer here.
### 5. How did SG7's input validation concepts become security practices in SG8?
> Write your answer here.
---
