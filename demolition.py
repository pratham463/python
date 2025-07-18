def no_notes(a):
    Q= [2000, 500, 100, 200, 50, 20, 10]
    x =0
    for i in range(7):
        q = Q[i]
        x = a//q
        print("Notes of {} = {}".format(q,x))
        a = a%q
amount = int(input("Enter Total Amount"))
no_notes(amount)