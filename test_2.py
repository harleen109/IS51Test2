"""
The program will first need to read the data from the Final.txt to display the data from the Final Exam
The program will need to count all the different exam scores of the students which means counting all the students who took the exam.
The program will need to ouput the class average score of the exam.
The program will need to output the percentage of students who scocred above the class average of 54.17 %

Function1 will output data.split()
Funciton2 will output sum(data) / len(data)
Function3 will output count = count + 54.17

"""

"""

#Function1

file = open("D:\Final.txt, "rt")
data = file.read()
Function1 = data.split

print('Number of Grades: ', len(Function1))


#Function2

Function2 = []
with open("D:\Final.txt, "rt")
     for line in rt:
         fields = line.split()
         rowdata = map(str.format, fields)
         Function2.extend(rowdata)
print(sum(Function2)/len(Function2))


#Function3 

test_list = open("D:\Final.txt, "rt")

k = whatever the average number comes out to

print ("the list :" + str(test_list))

"""

file = open(r"D:\Final.txt", "r")
Function1 = 0
for line in file :
    parts = line.split()
    Function1 += len(parts)

print("Number of Grades :", (Function1))


# space

Function2 = []

with open(r'D:\Final.txt') as f:
      Function2 = [float(line.rstrip()) for line in f]
biggest = min(Function2)
smallest = max(Function2)
(biggest - smallest)
print("Average grade: ", sum(Function2) / len(Function2))