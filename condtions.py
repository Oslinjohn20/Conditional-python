strFname = input("Please enter first name: \n")
strSname = input("Please enter surname: \n ")
intMark = int(input("Please enter mark:  \n"))
# declaring variables
# comparing mark to grades
if (intMark>=80) and (intMark<=100):
    # printing output of the grade with full name
    print(strFname, strSname, "Grade_A-Outstanding")
    # stating a different mark according the grading criteria given
elif (intMark>=60) and (intMark<=79):
    print(strFname, strSname, "Grade_B-Satisfactory")
elif (intMark>=50) and (intMark<=59):
    print(strFname, strSname, "Grade_C-Pass")
elif (intMark>=0) and (intMark<=49):
    print(strFname, strSname, "Grade_D-Fail")





