from student import calculate_grade  #  importing calculate grade function
import json      # importing json file
import os

# func. to load student details from json file
FILE_NAME = "students.json"
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
        return[]


# func. to save student details to json file
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)




# main list to store details 
students = load_students()   # using load_studnts func...  to load data from json file
           


# func. to add atudents

def add_detail():
        print()
        print("Enter the details of new Student :->")
        print()
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        print("Enter marks for each Subject :->")

        # creating one more dict.......... and add it to in students
        subjects = {
            "IP": int(input("Enter IP marks: ")),
            "Chemistry": int(input("Enter Chemistry Marks: ")),
            "Maths": int(input("Enter Maths marks: ")),
            "English": int(input("Enter English marks: ")),
            "Q & LA": int(input("Enter Q & LA marks: "))
        }
        
   # func...  to check that marks are only out of 100 
        for marks in subjects.values():
            if marks < 0 or marks > 100:
                print()
                print("Marks are only out of 100")
                return
            
        
        total_marks = calculate_total(subjects)
        grade = calculate_grade(total_marks)

        
        student = {
            "Roll No": roll,
            "Name": name,
            "Subjects": subjects,
            "Total marks": total_marks,
            "Grade": grade
        }
        students.append(student)      # appending  data to list
        print()
        print("✅ Details added successfully!")
        
        print()
        print("Details of New Student :->")
        print()
        print("Roll No     :", student["Roll No"])
        print("Name        :", student["Name"])
        print("Subjects    :->")
        print("IP          :", student["Subjects"]["IP"])
        print("Chemistry   :", student["Subjects"]["Chemistry"])
        print("Math        :", student["Subjects"]["Maths"])
        print("English     :", student["Subjects"]["English"])
        print("Q & LA      :", student["Subjects"]["Q & LA"])
        print("Total Marks :", student["Total marks"])
        print("Grade       :", student["Grade"])



        save_students()   # saving data to json file



# func. to calculate total of marks
def calculate_total(subjects):
    return sum(subjects.values())


    


#  searching a student detail  in list
def search_student_by_rollno():
    print()
    roll = int(input("Enter the roll number of student which you want to search: "))

    found = False   # flag
    
    for i in students:
        if i["Roll No"] == roll:
             print()
             print("✅ Student Found")
             print()
             print("Roll No     :",i["Roll No"])
             print("Name        :",i["Name"])
             print("Subjects    :->")
             print("IP          :",i["Subjects"]["IP"])
             print("Chemistry   :",i["Subjects"]["Chemistry"])
             print("Math        :",i["Subjects"]["Maths"])
             print("English     :",i["Subjects"]["English"])
             print("Q & LA      :",i["Subjects"]["Q & LA"])
             print("Total marks :",i["Total marks"])
             print("Grade       :",i["Grade"])
             found = True
             break
           
    if not found:
        print()
        print("❌ Roll No not exist")







# func. to update student details
def update_detail():
        print()
        roll = int(input("Enter the Roll No of student which you want to update: "))
    
        found = False
        # loop to check that roll no exist in list
        for i in students:
          if i["Roll No"] == roll:
              found = True
              print()
              print("What details are you want to update :->")
              print()
              print("Here are the choices")
              print("1. Update Student Roll No")
              print("2. Update  Student Name")
              print("3. Update Student marks")
              print()
              choice = int(input("Enter your choice (1-3): "))

              # update roll no
              if choice ==1:
               print()
               newroll = int(input("Enter new Roll No of student: "))
               i["Roll No"] = newroll
               print()
               print("✅ Roll No Updated")
               print()

               save_students()   # saving data to json file

             # update name
              elif choice ==2:
               print()
               newname = input("Enter New Name of student:  ")
               i["Name"]= newname
               print()
               print("✅ Name updated") 
               print()

               save_students()   # saving data to json file


              # update subject marks
              elif choice ==3:
                print()
                subjects = i["Subjects"]
                print("CHOOSE SUBJECT :->")
                print()
                print("Here are the choices for subject: ")
                print()
                print("1. IP Marks")
                print("2. Chemistry Marks")
                print("3. Maths Marks")
                print("4. English Marks")
                print("5. Q & LA Marks")
                print()
                s = int(input("Enter your choice (1-5): "))  # chossing which subject
                print()
                if s == 1:
                  subjects["IP"] = int(input("Enter new IP marks: "))


                  # *****  🔥🔥🔥🔥 very IMP  update total marks and grade ******
                  i["Total marks"]=calculate_total(i["Subjects"])
                  i["Grade"]=calculate_grade(i["Total marks"])


                  save_students()   # saving data to json file

                  print()
                  print("✅ Subject Marks, Total marks & Grade Updated")
                  print()
                elif s == 2:
                  subjects["Chemistry"] = int(input("Enter new  Chemistry marks: "))


                  # *****  🔥🔥🔥🔥 very IMP  update total marks and grade ******
                  i["Total marks"]=calculate_total(i["Subjects"])
                  i["Grade"]=calculate_grade(i["Total marks"])


                  save_students() 
                  print()
                  print("✅ Subject Marks, Total marks & Grade Updated")
                  print()
                elif s == 3:
                  subjects["Maths"] = int(input("Enter new  Maths marks: "))
                 
                  
                  # *****  🔥🔥🔥🔥 very IMP  update total marks and grade *****
                  i["Total marks"]=calculate_total(i["Subjects"])
                  i["Grade"]=calculate_grade(i["Total marks"])


                  save_students() 
                  print()
                  print("✅ Subject Marks, Total marks & Grade Updated")
                  print()
                elif s == 4:
                  subjects["English"]= int(input("Enter new  English marks: "))
                 
                  # *****  🔥🔥🔥🔥 very IMP  update total marks and grade ******
                  i["Total marks"]=calculate_total(i["Subjects"])
                  i["Grade"]=calculate_grade(i["Total marks"])


                  save_students() 
                  print()
                  print("✅ Subject Marks, Total marks & Grade Updated")
                  print()
                elif s == 5:
                  subjects["Q & LA"]= int(input("Enter new Q & LA marks: "))
                  
                   # *****  🔥🔥🔥🔥 very IMP  update total marks and grade ******
                  i["Total marks"]=calculate_total(i["Subjects"])
                  i["Grade"]=calculate_grade(i["Total marks"])


                  save_students() 
                  print()
                  print("✅ Subject Marks, Total marks & Grade Updated")
                  print()
                else:
                       print()
                       print("❌ Invalid Subject!")
               
              else:
                print()
                print("❌ Invalid Choice!")
              break
        if not found:
         print()
         print("❌ Roll No not exist")

        



# func.  to delete detail
def delete_detail():
       print()
       roll = int(input("Enter the roll number of student which you want to delete detail: "))
       found = False
       for i in students:
           if i["Roll No"] == roll:
               found = True
               students.remove(i)
               print()       
               print("✅ Student detail deleted successfully")
               save_students()
       if not found:
               print()
               print("❌ Roll No not exist")
               
       
    