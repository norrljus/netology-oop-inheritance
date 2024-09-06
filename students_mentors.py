class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_m(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n\
Фамилия: {self.surname}\n\
Средняя оценка за домашние задания: {sum(sum(list(self.grades.values()), [])) / len(sum(list(self.grades.values()), []))}\n\
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n\
Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) < (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))

    def __gt__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) > (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))

    def __eq__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) == (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))

    def __le__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) <= (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))

    def __ge__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) >= (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):

    def __lt__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) < (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))

    def __gt__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) > (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))

    def __eq__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) == (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))

    def __le__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) <= (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))

    def __ge__(self, other):
        return (sum(sum(list(self.grades.values()), [])) / len(list(other.grades.values()))) >= (sum(sum(list(other.grades.values()), []))) / len(list(other.grades.values()))

    def __str__(self):
        return (f"Имя: {self.name}\n\
Фамилия: {self.surname}\n\
Средняя оценка за лекции: {sum(sum(list(self.grades.values()), [])) / len(sum(list(self.grades.values()), []))}")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


student_one = Student('Bob', 'Dylan', 'male')
student_one.courses_in_progress += ['Python', 'Git']

student_two = Student('Marie', 'Antoinette', 'female')
student_two.courses_in_progress += ['Databases', 'Django', 'Python']
student_two.finished_courses += ['Surviving Guillotine']

reviewer_one = Reviewer('Michael', 'Jackson')
reviewer_one.courses_attached += ['Databases', 'Git']

reviewer_two = Reviewer('Freddie', 'Mercury')
reviewer_two.courses_attached += ['Python', 'Django']

lecturer_one = Lecturer('Ivan', 'the Terrible')
lecturer_one.courses_attached += ['Git', 'Django', 'Python']

lecturer_two = Lecturer('Yuri', 'Gagarin')
lecturer_two.courses_attached += ['Python', 'Databases']

reviewer_two.rate_hw(student_one, 'Python', 8)
reviewer_one.rate_hw(student_two, 'Databases', 10)
reviewer_one.rate_hw(student_one, 'Git', 6)
reviewer_two.rate_hw(student_two, 'Django', 5)
reviewer_two.rate_hw(student_two, 'Python', 9)

student_one.rate_m(lecturer_one, 'Git', 8)
student_one.rate_m(lecturer_two, 'Python', 9)
student_two.rate_m(lecturer_one, 'Django', 10)
student_two.rate_m(lecturer_one, 'Python', 9)
student_two.rate_m(lecturer_two, 'Databases', 8)

print(lecturer_one < lecturer_two)
print(student_one > student_two)
print(lecturer_one == lecturer_two)
print(student_one <= student_two)

print(student_one)
print(student_two)

print(reviewer_one)
print(reviewer_two)

print(lecturer_one)
print(lecturer_two)


def avg_studentscore(students, course):
    avgsc = []
    for i in students:
        if course in i.grades.keys():
            avgsc.extend(i.grades[course])
    return f"Средняя оценка среди студентов за курс '{course}': {sum(avgsc) / len(avgsc)}"


def avg_lectscore(lects, course):
    avgsc = []
    for i in lects:
        if course in i.grades.keys():
            avgsc += i.grades[course]
    return f"Средняя оценка среди преподователей за курс '{course}': {sum(avgsc) / len(avgsc)}"


print(avg_studentscore([student_one, student_two], "Python"))
print(avg_lectscore([lecturer_one, lecturer_two], "Python"))