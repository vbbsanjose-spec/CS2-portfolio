# ~~~~ THE CODE ~~~~
```python
# Student Performance Evaluator

#Ask for inputs
score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))
completed_tasks = int(input("Enter number of completed tasks: "))

#Making functions
def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def get_performance(average):
  if average >= 85:
    return "Mastery"
  elif average >= 70:
    return "Developing"
  else:
    return "Needs Review"
    
def is_eligible(average, completed_tasks):
  if average >= 85 and completed_tasks >= 3:
    return True
  else:
    return False

#using/making variables for the functions
average = calculate_average(score1, score2, score3)
performance =  get_performance(average)
eligible =  is_eligible(average, completed_tasks)

#Display the outputsss
print(f"Average: {average:.2f}")
print(f"Performance: {performance}")
print(f"Eligible for challenge: {eligible}")
```
# ~~~~ DOCUMENTATION QUESTIONS ~~~~
## 1. Which function returns a number, which returns a string, and which returns a Boolean?
- calculate_average() returns a number (float) representing the average score.
- get_performance() returns a string, such as "Mastery", "Developing", or "Needs Review".
- is_eligible() returns a Boolean value, either True or False.
  
## 2. Explain how the average moves from calculate_average() into get_performance().
- it uses the function calculate_average() in order to identify the performance of the student.

## 3. What happens when a student has a high average but has completed fewer than three tasks?
- The student is not eligible for the practice challenge because both conditions must be satisfied: the average must be at least 85, and the student must have completed at least three tasks. If either condition is false, is_eligible() returns False.
  
## 4. Why is return more appropriate than simply printing the result inside each function?
- Using return is better because we can use the result later, while print() only displays it on the screen.

