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
