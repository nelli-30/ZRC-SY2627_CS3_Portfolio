class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self._is_submitted = False
        self._grade = None
        self._submitted_files = []

    def _validate_grade(self, score):
        return 0 <= score <= 100

    def _check_submission_status(self):
        return len(self._submitted_files) > 0

    def _is_duplicate(self, filename):
        return filename in self._submitted_files

    def add_file(self, filename):
        if self._is_duplicate(filename):
            print(f"Error: '{filename}' already exists in submission.")
            return False
        
        self._submitted_files.append(filename)
        self._is_submitted = True
        return True

    def remove_file(self, filename):
        if self._grade is not None:
            print(f"Blocked: Cannot remove '{filename}' because a grade has already been assigned.")
            return False
        
        if filename in self._submitted_files:
            self._submitted_files.remove(filename)
            if len(self._submitted_files) == 0:
                self._is_submitted = False
            print(f"Successfully removed '{filename}'.")
            return True
        else:
            print(f"Error: '{filename}' not found in submission.")
            return False

    def view_files(self):
        return self._submitted_files

    def assign_grade(self, score):
        if not self._check_submission_status():
            print(f"Failed to assign grade: Cannot grade an empty submission for {self.student_name}.")
            return False
        
        if not self._validate_grade(score):
            print(f"Error: Invalid grade '{score}'. Must be between 0 and 100.")
            return False
            
        self._grade = score
        print(f"Grade {score} assigned to {self.student_name}.")
        return True

    def get_grade(self):
        if self._grade is None:
            return "Ungraded"
        return str(self._grade)

    def get_status_report(self):
        status = "Submitted" if self._is_submitted else "Not Submitted"
        return (f"Student: {self.student_name} (ID: {self.student_id}) | "
                f"Assignment: {self._assignment_title} | "
                f"Status: {status} | "
                f"Files: {self._submitted_files} | "
                f"Grade: {self.get_grade()}")


print("---INITIALIZING DROPBOX FOR STUDENTS---")
student1 = AssignmentSubmission(student_name = "Alex Gonzaga", student_id = "pshs-1090-x", assignment_title = "CS-101" , due_date = "2026-10-01" )
student2 = AssignmentSubmission(student_name = "Adelle", student_id = "pshs-1920-x", assignment_title = "CS-103" , due_date = "2026-10-01" )
student3 = AssignmentSubmission(student_name = "Juan Dela Cruz", student_id = "pshs-1033-x", assignment_title = "CS-101" , due_date = "2026-10-01" )
student4 = AssignmentSubmission(student_name = "Maria Santos", student_id = "pshs-1044-x", assignment_title = "CS-101" , due_date = "2026-10-01" )
student5 = AssignmentSubmission(student_name = "Jose Reyes", student_id = "pshs-1055-x", assignment_title = "CS-101" , due_date = "2026-10-01" )
print()

print("---TEST SCENARIO 1: Multiple Files via List---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("---TEST SCENARIO 2: Removing Files from List---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files:{student2.view_files()}\n")

print("---TEST SCENARIO 3: Preventing Duplicate Files---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Juan's Files: {student3.view_files()}\n")

print("---TEST SCENARIO 4: Removing the Test File after being graded ---")
student4.add_file("exam.answers.pdf")
student4.assign_grade(90)
student4.remove_file("draft.txt")
student4.remove_file("exam.answers.pdf") 
print()

print("---TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)#should fail because list is empty
print()

print("---FINAL SYSTEM REPORT---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())

print("IM GOING TO FUCKING KILL MYSELf")