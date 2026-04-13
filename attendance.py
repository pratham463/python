import matplotlib.pyplot as plt
student_names=["tom","ben","hen","ken","ten"]
attendance_days=[23,56,78,90,100]
attendance_prec = []
for x in attendance_days:
    res=(x/50)*100
    attendance_prec.append(res)
print(attendance_prec)
def marks_lines_chart():
    plt.plot(student_names,attendance_days)
    plt.title("students marks graph")
    plt.xlabel("names")
    plt.ylabel("attendance")
    plt.show()
marks_lines_chart()
def percentage_bar_chart():
    plt.plot(student_names,attendance_days)
    plt.title("students marks graph 2 ")
    plt.xlabel("names")
    plt.ylabel("attendance")
    plt.show()
percentage_bar_chart()