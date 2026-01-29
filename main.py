from operations import add_detail,search_student_by_rollno,update_detail,delete_detail

while True:
 print()
 print()
 print()
 print("|---------------------------------------------|")
 print("|----WELCOME TO STUDENT MANAGMEMENT SYSTEM----|")
 print("|                                             |")
 print("|-----Which task you want to do---------------|")
 print("|                                             |")
 print("|-----Here are the choices--------------------|")
 print("|                                             |")
 print("| 1.  Add New Student detail                  |")
 print("| 2.  View Student detail                     |")
 print("| 3.  Update Student detail                   |")
 print("| 4.  Delete Student detail                   |")
 print("| 5.  Exit                                    |")
 print("|---------------------------------------------|")
 print()
 choice = int(input("Enter your choice (1-5):"))

 if choice == 1:
  add_detail()
 elif choice ==2:
  search_student_by_rollno()
 elif choice ==3:
  update_detail()
 elif choice ==4:
  delete_detail()
 elif choice ==5:
  print()
  print("Thank You!")
  break
 else:
  print()
  print("❌ Invalid choice!")

