import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_no", "E-mail ID"])

        writer.writerow(info_list)


if __name__ == '__main__':
   condition = True
   student_count = 1

   while (condition):
       student_info = input("Enter information of student #{} in the following format (Name Age Contact_no. E-mail_id): ".format(student_count))

       student_info_list = student_info.split(' ')
       print("Verify the information-\nName: {}\nAge: {}\nContact_no: {}\nE-mail ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2],student_info_list[3]))

       choice_check = input("Is the entered information correct? (yes/no): ")

       if choice_check == 'yes':
           write_into_csv(student_info_list)

           condition_check = input("Enter (yes/no) if you want to add information for another student: ")
           if condition_check == "yes":
                condition = True
                student_count = student_count + 1
           elif condition_check == "no":
               condition = False
       elif condition_check == "no":
           print("\nPlease re-enter the information.")



