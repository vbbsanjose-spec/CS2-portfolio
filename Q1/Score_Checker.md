# Part 1

## Input
The program, score checker, needs the student’s score as its input 


## Boundaries
The minimum value = 0
The maximum value = 100


## Possible Outputs
*The outputs that the program can show are the following:*
You have an Invalid Score
Your score Needs Improvement
Your score is Satisfactory
Your score is Very satisfactory
Your score is Outstanding


## Selection Patterns
**Boundary Condition**
Boundary condition will be used when the student gives a score below 0 or above 100.
Condition: 0  > score or score > 100


**Multiple Decision Paths**
The score must be validated first if it surpassed the boundaries, if not,
it will be then classified based on how high their value is



# Part 2

**The** ***flowchart*** **of the program**
![Score Checker Flowchart](./Score_Checker_Flowchart_20260906_202744_0000.png)



# Part 3

**The** ***pseudocode*** **of the program**

START 

INPUT the student’s score

IF score < 0 OR score > 100 THEN
PRINT “Invalid Score”

ELSE IF score >= 90 THEN
PRINT “Outstanding”

ELSE IF score >= 80 THEN
PRINT “Very satisfactory” 

ELSE IF score >= 75 THEN
PRINT “Satisfactory”

ELSE 
PRINT “Needs Improvement”

END

