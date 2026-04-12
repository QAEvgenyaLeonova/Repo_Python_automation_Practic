from Student import Student

class CourseGroup:
    def __init__(self, student, classmates):
        self.student = student
        self.classmates = classmates

    def __str__(self):
        classmates = ', '.join([str(classmates) for classmates in self.classmates])
        return f'{self.student} учится вместе с : {self.classmates}'


