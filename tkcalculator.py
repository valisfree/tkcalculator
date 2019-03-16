from tkinter import *
root = Tk()

root.geometry("330x300+300+300")
root.minsize(330,300)
root.title("Calculator")

operations = []
def get_number(event=0):
    operations.append(ent.get())
    ent.delete(0, END)
def clear_entry(event=0):
    operations.clear()
    ent.delete(0, END)
def add_number1(event=0):
    ent.insert(END, 1)
def add_number2(event=0):
    ent.insert(END, 2)
def add_number3(event=0):
    ent.insert(END, 3)
def add_number4(event=0):
    ent.insert(END, 4)
def add_number5(event=0):
    ent.insert(END, 5)
def add_number6(event=0):
    ent.insert(END, 6)
def add_number7(event=0):
    ent.insert(END, 7)
def add_number8(event=0):
    ent.insert(END, 8)
def add_number9(event=0):
    ent.insert(END, 9)
def add_number0(event=0):
    ent.insert(END, 0)
def add_dot(event=0):
    ent.insert(END, ".")
def add_devnum(event=0):
    ent.insert(END, "%")
def add_plus(event=0):
    get_number(event)
    operations.append("+")
def add_minus(event=0):
    get_number(event)
    operations.append("-")
def add_mult(event=0):
    get_number(event)
    operations.append("*")
def add_div(event=0):
    get_number()
    operations.append("/")
def add_exp(event=0):
    ent.insert(END, "x²")
    sol()
def add_sq(event=0):
    ent.insert(END, "√")
def sol(event=0):
    get_number()
    x = operations[0]
    if operations[2]:
        y = operations[2]
    char = operations[1]
    if x.isdigit() and y.isdigit(): # вещественные или целочисленные?
        x = int(x)
        y = int(y)
    else:
        x = float(x)
        y = float(y)
    if char == "+":
        sum = x + y
    if char == "-":
        sum = x - y
    if char == "*":
        sum = x * y
    if char == "/":
        sum = x / y
    if char == "x²":
        sum = x * 2
    if char == "√":
        sum = sqrt(x)
    ent.insert(END, sum)

### FOR INTENDATION
f_max=Frame(root)

f_top=LabelFrame(f_max, text='HELLO BRO!')
ent=Entry(f_top, width=15, bg='gray', font="Arial 14", text="5")

### TOP CLEAR BLOCK
f_top_block=Frame(f_max)
but_clear=Button(f_top_block, width=2, text="Clear", font="Arial 24", command=clear_entry)

### NUMBERS AND CHARS BLOCKS
f_big_left_block=Frame(f_max)
f_big_right_block=Frame(f_max)


### LEFT BUTTON BLOCK
f_three_line=Frame(f_big_left_block) # 7-9
but7=Button(f_three_line, width=2, text="7", font="Arial 24", command=add_number7)
# root.bind("<7>", add_number7)
but8=Button(f_three_line, width=2, text="8", font="Arial 24", command=add_number8)
# root.bind("<8>", add_number8)
but9=Button(f_three_line, width=2, text="9", font="Arial 24", command=add_number9)
# root.bind("<9>", add_number9)

f_two_line=Frame(f_big_left_block) # 4-6
but4=Button(f_two_line, width=2, text="4", font="Arial 24", command=add_number4)
# root.bind("<4>", add_number4)
but5=Button(f_two_line, width=2, text="5", font="Arial 24", command=add_number5)
# root.bind("<5>", add_number5)
but6=Button(f_two_line, width=2, text="6", font="Arial 24", command=add_number6)
# root.bind("<6>", add_number6)

f_one_line=Frame(f_big_left_block) # 1-3
but1=Button(f_one_line, width=2, text="1", font="Arial 24", command=add_number1)
# root.bind("<1>", add_number1)
but2=Button(f_one_line, width=2, text="2", font="Arial 24", command=add_number2)
# root.bind("<2>", add_number2)
but3=Button(f_one_line, width=2, text="3", font="Arial 24", command=add_number3)
# root.bind("<3>", add_number3)

f_null_line=Frame(f_big_left_block) # 0.%
but0=Button(f_null_line, width=2, text="0", font="Arial 24", command=add_number0)
# root.bind("<0>", add_number0)
but_dot=Button(f_null_line, width=2, text=".", font="Arial 24", command=add_dot)
but_remdiv=Button(f_null_line, width=2, text="%", font="Arial 24", command=add_devnum)

### RIGHT BUTTON BLOCK
f_r_one_line=Frame(f_big_right_block) # +-
but_plus=Button(f_r_one_line, width=2, text="+", font="Arial 24", command=add_plus)
but_minus=Button(f_r_one_line, width=2, text="-", font="Arial 24", command=add_minus)

f_r_two_line=Frame(f_big_right_block) # */
but_mult=Button(f_r_two_line, width=2, text="*", font="Arial 24", command=add_mult)
but_div=Button(f_r_two_line, width=2, text="/", font="Arial 24", command=add_div)

f_r_three_line=Frame(f_big_right_block) # x² √
but_exp=Button(f_r_three_line, width=2, text="x²", font="Arial 24", command=add_exp)
but_sq=Button(f_r_three_line, width=2, text="√", font="Arial 24", command=add_sq)

f_r_four_line=Frame(f_big_right_block) # =
but_sol=Button(f_r_four_line, text="=", font="Arial 24", command=sol)

### PACK TOP
f_top_block.pack(fill=X)
but_clear.pack(fill=X)
f_top.pack(fill=X, padx=2, pady=2)
ent.pack(fill=X)

### PACK LEFT BUTTON BLOCK
f_three_line.pack(fill=X)
f_two_line.pack(fill=X)
f_one_line.pack(fill=X)
f_null_line.pack(fill=X)
but1.pack(side=LEFT)
but2.pack(side=LEFT)
but3.pack(side=LEFT)
but4.pack(side=LEFT)
but5.pack(side=LEFT)
but6.pack(side=LEFT)
but7.pack(side=LEFT)
but8.pack(side=LEFT)
but9.pack(side=LEFT)
but0.pack(side=LEFT)
but_dot.pack(side=LEFT)
but_remdiv.pack(side=LEFT)

### PACK RIGHT BUTTON BLOCK
f_r_one_line.pack(fill=X)
f_r_two_line.pack(fill=X)
f_r_three_line.pack(fill=X)
f_r_four_line.pack(fill=X)
but_plus.pack(side=LEFT)
but_minus.pack(side=LEFT)
but_mult.pack(side=LEFT)
but_div.pack(side=LEFT)
but_exp.pack(side=LEFT)
but_sq.pack(side=LEFT)
but_sol.pack(fill=X)

### PACK MIDDLE
f_big_left_block.pack(side=LEFT)
f_big_right_block.pack(side=LEFT)

f_max.pack(padx=4, pady=4)
root.mainloop()
