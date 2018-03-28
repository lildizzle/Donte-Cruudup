#Donte Crudup 

Sub_1, Grade_1 = input("what is the subject: "), float(input("What did you get in this class: "))

Sub_2, Grade_2 = input("what is the subject: "), float(input("What did you get in this class: "))

Sub_3, Grade_3 = input("what is the subject: "), float(input("What did you get in this class: "))

Sub_4, Grade_4 = input("what is the subject: "), float(input("What did you get in this class: "))

Sub_5, Grade_5 = input("what is the subject: "), float(input("What did you get in this class: "))

New_list1 = [Sub_1, Sub_2, Sub_3, Sub_4, Sub_5]
New_list2 = [Grade_1, Grade_2, Grade_3, Grade_4, Grade_5]

grade_overall = (Grade_1 + Grade_2 + Grade_3 + Grade_4 + Grade_5) /  5

New_list2.append(grade_overall)
New_list1.append("average")


print New_list1
print New_list2


for grade_overall in range (1,59):
    print ("You are doing very bad. try harder")
for grade_overall in range(60,79):
     print ("you are doing fine but you can do better")
for grade_overall in range(80,90):
    print ("you are excelling at evrything you do keep up the good work")
    
    
