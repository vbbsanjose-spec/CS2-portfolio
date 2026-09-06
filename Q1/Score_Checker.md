# Clean Decision Code Makeover: Student Score Checker 
**Name:** Vince Bryll B. San Jose
**Section:** Dahlia

# Activity Overview

In this activity, I improved a Student Score Checker program 
by applying proper coding standards and selection structures.

The program accepts a student score from 0 to 100 and
determines the appropriate classification 

The classifications are:

|Score | Classification |
|---: | --- |
| 90-100 | Outstanding |
| 80-89 | Very Satisfactory |
| 75-79 | Satisfactory |
| 0-74 | Needs Improvement |

Scores Below 0 or above 100 are considered invalid.

---

# Part 1 - Analyze the logic

## Input
What information does the program need?
>The program, score checker, needs the student’s score. 


## Valid Range
**The minimum value** 
> 0

**The maximum value** 
< 100


## Possible Outputs
List all possible outputs of the program 

1. Invalid Score
2. Needs Improvement
3. Satisfactory
4. Very satisfactory
5. Outstanding


## Boundary Condition 
What condition will you use to determine whether the score is valid?>Boundary condition will be used when the student gives a score below 0 or above 100. Condition: 0  > score or score > 100



**Multiple Decision Paths**
Explain how the program decides which classification should be displayed.
>The score must be validated first if it surpassed the boundaries, if not, it will be then classified based on how high their value is



# Part 2 - Flowchart 

## Flowchart 
![Score Checker Flowchart](./Score_Checker_Flowchart_20260906_202744_0000.png)



# Part 3 - Pseudocode 

## Sample pseudocode 

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


# Part 4 - Clean Code Implementation 

## Source Code 

![ Score Checker Source Code](./Score_Checker.py)

# Part 5 - Testing 
| Test | Input | Purpose | Expected Output | Actual Output | Result |





