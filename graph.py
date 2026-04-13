import matplotlib.pyplot as plt
students_names = ["tom","tim","pom","mom","hom","tam","tem","top"]
students_marks = [35,34,25,23,13,23,23,45]
marks_prec = []
for x in students_marks:
    res = (x/50)*100
    marks_prec.append(res)
print(marks_prec)
def marks_lines_chart():
    plt.plot(students_names,students_marks)
    plt.title("students marks graph")
    plt.xlabel("names")
    plt.ylabel("marks")
    plt.show()
marks_lines_chart()
def percentage_bar_chart():
    plt.plot(students_names,students_marks)
    plt.title("percentage graph")
    plt.xlabel("names")
    plt.ylabel("marks")
    plt.show()
percentage_bar_chart()