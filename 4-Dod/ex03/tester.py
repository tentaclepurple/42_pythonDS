from new_student import Student


try:
    student1 = Student(name="Edward", surname="Agle")
    print(student1)
except (TypeError, ValueError) as e:
    print(e)

try:
    student2 = Student(name="", surname="Agle")
    print(student2)
except (TypeError, ValueError) as e:
    print(e)

try:
    student3 = Student(name="Edward", surname=123)
    print(student3)
except (TypeError, ValueError) as e:
    print(e)

try:
    student4 = Student(name="Edward", surname="Agle", id="123")
    print(student4)

except (TypeError, ValueError) as e:
    print(e)
