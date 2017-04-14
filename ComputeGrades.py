
def computeGrades(e1, e2, a):
    """Will compute a final average for two exams that equal 20% each of the final grade and then the top ten highest assignments that equal 60% of the final grade.
    It returns the grade in numerical form as well as the letter grade."""
    
    a = assignmentScores
    a.sort()
    i=0
    while i<10:
        sum+=sum a[i]
    avg = sum/10
    
    grade = ((e1 + e2) /2) * 0.4 + (avg) * 0.6
    
    return grade
    
    if grade >= 90 and grade <= 100:
            return("A")
    
    elif grade >= 80 and grade < 90:
            return("B")
    
    elif grade >= 70 and grade < 80:
            return("C")
    
    elif grade >= 60 and grade < 70:
            return("D")
    
    elif grade < 60:
            return("F")
            
def testDriver():
    """This funtion will test if the computeGrades function will pass or fail"""
    exam1=90
    exam2=85
    assignmentScores = [50, 60, 70, 80, ]
    computeGrades(exam1, exam2, assignmentScores)

print Passed
print Failed