class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        delimeter = ','
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade}\nКурсы в процессе изучения: {delimeter.join(self.courses_in_progress)}\nЗавершенные курсы: {delimeter.join(self.finished_courses)}'
        return result
    
    def av_grade(self):
        average_grade = sum(self.grades.values())/len(self.grades.values())
        return average_grade
    
    def _lt_(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.av_grade < other.av_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
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
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade}'
        return result

    def av_grade(self):
        average_grade = sum(self.grades.values())/len(self.grades.values())
        return average_grade

    def _lt_(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.av_grade < other.av_grade

all_courses = ['DADA', 'Potions']  

albus_dumbledore = Lecturer('Albus', 'Dumbledore')
severus_snape = Lecturer('Severus', 'Snape')
filius_flitvik = Reviewer('Filius', 'Flitvik')
dolores_umbridge = Reviewer('Dolores', 'Umbridge')
harry_potter = Student('Harry', 'Potter', 'male')
drako_malfoy = Student('Drako', 'Malfoy', 'male')
harry_potter.courses_in_progress = all_courses 
drako_malfoy.courses_in_progress = all_courses

dolores_umbridge.courses_attached += ['Potions']
albus_dumbledore.courses_attached += ['DADA']
severus_snape.courses_attached += ['Potions']
filius_flitvik.courses_attached += ['DADA']

filius_flitvik.rate_hw(harry_potter, 'DADA', 10)
filius_flitvik.rate_hw(drako_malfoy, 'DADA', 8)

dolores_umbridge.rate_hw(harry_potter, 'Potions', 4)
dolores_umbridge.rate_hw(drako_malfoy, 'Potions', 7)

harry_potter.rate_hw(albus_dumbledore, 'DADA', 9)
harry_potter.rate_hw(severus_snape, 'Potions', 3)


drako_malfoy.rate_hw(albus_dumbledore, 'DADA', 3)
drako_malfoy.rate_hw(severus_snape, 'Potions', 7)



print(albus_dumbledore.av_grade)

