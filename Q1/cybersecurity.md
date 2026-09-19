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
> It creates a sense of urgency by saying that the account will be disabled
> It asks the student to click an unfamiliar link
> It requires sensitive login info such as username and password
> The message may come from an anonymous and suspicious sender
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
| Student Name | | |
| Section | | |
| Club Choice | | |
| School Email | | |
| Attendance Status | | |
| Password | | |
| OTP | | |
| Home Address | | |

| Parent Bank Account | | |
---
## Privacy Question
Why is it safer to collect only information that the program actually needs?
> Write your answer here.
---
# Part C - Security-Focused Validation Rules
Complete the table before writing your program.
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Student Name | | | | | |
| Section | | | | | |
| Club Choice | | | | | |
| School Email | | | | | |
| Attendance Status | | | | | |
---
## Secure Data Capture Questions
### 1. What should your program accept?
> Write your answer here.
### 2. What should your program reject?
> Write your answer here.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> Write your answer here.
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
# Paste your final program here.
```
---
## Security Practices Applied
### Required Input
> Explain how you handled blank input.
### Allowed Values
> Explain which fields accept only predefined values.
### Format Check
> Explain your simple email validation rule.
### Error Messages
> Explain why clear error messages are useful.
### Data Minimization
> Explain what information you intentionally did NOT collect and why.
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
