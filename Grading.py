# In this project I will calcultae the grade of student 
print ("Enter your name")
name = input ()
# Initialize an empty list to store the column elements
subject_name = []
subject_marks = []
# Get the number of elements in the column from the user
num_elements = int(input("Enter the number of Subjects: "))
# Loop to iterate over each element in the column
for i in range(num_elements):
    element = input(f"Enter Subject Name {i+1}: ")
    subject_name.append(element)
    element = int(input(f"Enter Subject Marks {i+1}: "))
    subject_marks.append(element)
# Print the column
for elem1, elem2 in zip(subject_name , subject_marks):
    print(elem1, elem2)
# Calculate the average of elements in the column
column_sum = sum(subject_marks)  # Calculate the sum of all elements in the column
print("Marks Obtained:", column_sum)
print("Total Marks:", num_elements*100)
average = column_sum / num_elements  # Calculate the average
print("Percentage:", average)
if average > 49  and average < 60 :
    print(name, "has for A Grade")    
elif average > 49  and average < 60 :
    print(name, "has for F Grade")
elif average > 59  and average < 70 :
    print(name, "has C Grade")
elif average > 69  and average < 80 :
    print(name, "has B Grade")
elif average > 79  and average < 90 :
    print(name, "has A Grade")
elif average > 99  and average <= 100 :
    print(name, "has A+ Grade")
else:
    print (name,"is Fail")