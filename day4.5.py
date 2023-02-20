class Student:
    def __init__(self,name,usn,branch):
        self.name = name
        self.usn = usn
        self.branch = branch
    def update_branch(self, branch_new):
        self.branch = branch_new
    def display_details(self):
        print("Student Name: ",self.name)
        print("USN: ",self.usn)
        print("Branch: ",self.branch)
student_data = [
    Student("Cezane Karki","010","Patan Dhoka"),
    Student("Harry Bro","006","Bhaktapur"),
    Student("Ram","005","Sinamangal")
]
input1 = input("Enter the search query for the student name: ")
data = [x for x in student_data if x.name.count(input1)>=1]
if data:
    data[0].display_details()
else:
    print("No data")