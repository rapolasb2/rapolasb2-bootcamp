# Prompt the user to enter the number of students registering for the exam
number_of_students = int(input("How many students are registering for the exam? "))

# Loop through each student prompting to enter their ID number
for i in range(number_of_students):
    id = input("Please enter the student's ID number: ")
    
    # Open 'student_register.txt' file in 'a+' mode, which allows reading and appending
    with open('student_register.txt', 'a+') as f:
        # Write the student's ID and a signatory line to the file
        f.write("Student ID: " + id + "\n")
        f.write("Please sign here...................." + "\n")