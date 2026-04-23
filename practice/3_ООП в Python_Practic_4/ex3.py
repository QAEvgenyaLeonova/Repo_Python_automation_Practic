from CourseGroup import CourseGroup
from Student import Student

student = Student('Anna', 'Petrova', 28, 5, )
classmate1 = Student('Иван', 'Иванов', 25, 3)
classmate2 = Student('Александр', 'Морозов', 24, 2)
classmate3 = Student('Анастасия', 'Летняя', 23, 1)

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)


















