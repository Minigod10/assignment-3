"""4. Write a program to prompt the user for a grade between 4 and 10. If the grade
is out of range print error message. If the grade is between 4 and 10 Print the
grade and the performance using the following:
Letter Grade Performance Grade Points
A+  Outstanding     10
A   Excellent   9
B+  Very Good   8
B   Good        7
C+  Average     6
C   Below Average 5
D   Poor        4
E.g.: For Grade 9 Output is:
Your Grade is A and Excellent Performance."""



grade_point=int(input("Enter grade points:"))
if grade_point>10 or grade_point<4:
    print("Error")
elif grade_point==10:
    print("Your grade is A++ and Outstanding Performance")
elif grade_point==9:
    print("Your grade is A and Excellent Performance")
elif grade_point==8:
    print("Your grade is B+ and Very Good Performance")
elif grade_point==7:
    print("Your grade is B and Good Performance")
elif grade_point==6:
    print("Your grade is C+ and Average Performance")
elif grade_point==5:
    print("Your grade is C and Below Average Performance")
elif grade_point==4:
    print("Your grade is D and Poor Performance")

