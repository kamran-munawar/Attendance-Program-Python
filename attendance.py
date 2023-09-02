# Create an empty dictionary to store student attendance
attendance_record = {}

def mark_attendance():
    student_name = input("Enter student name: ")
    status = input(f"Mark {student_name}'s attendance (Present/Absent): ").lower()
    
    if student_name in attendance_record:
        attendance_record[student_name].append(status)
    else:
        attendance_record[student_name] = [status]

def view_attendance():
    for student, status_list in attendance_record.items():
        attendance = ", ".join(status_list)
        print(f"{student}: {attendance}")

def main():
    while True:
        print("\nStudent Attendance Tracker")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
