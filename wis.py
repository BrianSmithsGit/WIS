class Weight:
    def __init__(self, title, percent):
        self.title = title
        self.percent = percent
        self.grades = {}
    def add_grade(self, assignment, score):
        self.grades[assignment]=score
        
    def print_grades(self):
        for i in self.grades:
            print("{}: {}".format(i,self.grades[i]))

w = Weight("Homework", .20)
w.add_grade("Assignment 1", 70)
w.print_grades()

