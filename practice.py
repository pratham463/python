import matplotlib.pyplot as plt
student_names = [

"Aarav", "Vihaan", "Ishita", "Ananya", "Rohan",

"Meera", "Kabir", "Sneha", "Arjun", "Priya"

]

students_scores = [92, 67, 88, 79, 73, 84, 91, 76, 69, 95]
scores_prec=[]
for x in students_scores:
    res=(x/50)*100
    scores_prec.append(res)
print(scores_prec)
def marks_lines_chart():
    plt.plot(student_names,students_scores)
    plt.title("students scores graph")
    plt.xlabel("names")
    plt.ylabel=("scores")
    plt.show()
marks_lines_chart()
def percentage_bar_chart():
    plt.plot(student_names,students_scores)
    plt.title("graph")
    plt.xlabel("names")
    plt.ylabel("scores")
    plt.show()
percentage_bar_chart()