class person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
        
    def getname(self):
        return self.name
    def setname(self, name):
        self.name = name
        
    def getyob(self):
        return self.yob
    def setyob(self, yob):
        self.yob = yob
    
    def printf(self):
        print("Name: " + self.name)
        print("Yob: " + str(self.yob))
        
class student(person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    
    def getgrade(self):
        return self.grade
    def setgrade(self, grade):
        self.grade = grade
        
    def printf(self):
        super().printf()
        print("Grade: " + self.grade)
        
class teacher(person):
    def __init__(self, name, yob, subj):
        super().__init__(name, yob)
        self.subj = subj
        
    def getsubj(self):
        return self.subj
    def setsubj(self, subj):
        self.subj = subj
    def printf(self):
        super().printf()
        print("Subject: " + self.subj)
        
class doctor(person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
    
    def get_specialist(self):
        return self.specialist
    def set_specialist(self, spec):
        self.specialist = spec
    
    def printf(self):
        super().printf()
        print("Specialist: " + self.specialist)
        
class ward:
    def __init__(self, name):
        self.name = name
        self.people = []
    def addperson(self):
        print("1. Student\n"
            + "2. Teacher\n"
            + "3. Doctor")
        n = int(input("Chon doi tuong ban muon them vao: "))
    
        match(n):
            case 1:
                name = str(input("name: "))
                yob = int(input("Yob: "))
                grade = str(input("Grade: "))
                self.people.append(student(name, yob, grade))
            case 2:
                name1 = str(input("name: "))
                yob1 = int(input("Yob: "))
                subj = str(input("Subject: "))
                self.people.append(teacher(name1, yob1, subj))
            case 3:
                name2 = str(input("name: "))
                yob2 = int(input("Yob: "))
                spec = str(input("Specialist: "))
                self.people.append(doctor(name2, yob2, spec))
                
    def describe(self):
        print("Ward name: " + self.name)
        for person in self.people:
            person.printf()
            print("\n")
    
    def count_doctors(self):
        return sum(1 for person in self.people if isinstance(person, doctor))
    
    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)
    
    def average_teacher_yob(self):
        teachers = [person.yob for person in self.people if isinstance(person, teacher)]
        return sum(teachers) / len(teachers) if teachers else 0
    
    
w = ward("Ward A")
# for i in range(5):
#     w.addperson()
# w.describe()
# print("Number of Doctors:", w.count_doctors())
# w.sort_age()
# print("Sorted by Age:", w.describe())
# print("Average Year of Birth of Teachers:", w.average_teacher_yob())


exit_program = False

while not exit_program:
    print("\n----- MENU -----")
    print("1. Add Person")
    print("2. Describe")
    print("3. Count Doctors")
    print("4. Sort Age")
    print("5. Average Teacher YOB")
    print("6. Exit")
    choice = int(input("Select a function: "))
    if choice == 1:
        w.addperson()
    elif choice == 2:
        w.describe()
    elif choice == 3:
        w.count_doctors()
    elif choice == 4:
        w.sort_age()
    elif choice == 5:
        w.average_teacher_yob()
    elif choice == 6:
        exit_program = True
        print("Exit Prograam.")
    else:
        print("Invalid choice. Please select again.")