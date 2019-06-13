from tkinter import *
import tkinter.font as tkFont
import kernel as ke

master = Tk()

master.title("数解法求最大绿波带相位差求解器")

ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
thelabel = Label(master, text='数解法求最大绿波带相位差',font=ft)
thelabel.pack()

frame = Frame(master)
frame.pack(padx=100,pady=67)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

v4 = StringVar()
v5 = StringVar()
v6 = StringVar()

def test(content):
    return content.isdigit()

r = 0
l1 = Label(frame, text="周期时长(s)：").grid(row=r,column=0);r+=1
l3 = Label(frame, text="交叉口距离(m)：").grid(row=r,column=0);r+=1
l2 = Label(frame, text="各交叉口绿信比(%)：").grid(row=r,column=0);r+=1

testCMD = master.register(test)
e1 = Entry(frame,width=10,textvariable=v1,validate="key",\
           validatecommand=(testCMD,'%P')).grid(row=0,column=1)
#Label(frame,text="周期长度").grid(row=0,column=1)

e2 = Entry(frame,width=30,textvariable=v2,\
           validatecommand=(testCMD,'%P')).grid(row=1,column=1)
#Label(frame,text="绿信比").grid(row=0,column=3)

e4 = Entry(frame,width=30,textvariable=v3,\
           validatecommand=(testCMD,'%P')).grid(row=2,column=1)

e3 = Entry(frame,width=20,textvariable=v4,state="readonly").grid(row=r,column=1);

e5 = Entry(frame,width=20,textvariable=v5,state="readonly").grid(row=r+1,column=1);

e6 = Entry(frame,width=20,textvariable=v6,state="readonly").grid(row=r+2,column=1);


def string_to_int(input_string):
    buff = []
    temp = 0
    for each in input_string:
        if each == ' ' or each == ',':
            temp = 0
            continue
        else:
            temp = temp*10 + int(each)
            # buff.append(temp)
    
    buff.append(temp)
    
    return buff


def calc():
    # 信号周期
    input_string1 = v1.get()
    cycle_temp = 0
    for each in input_string1:
        cycle_temp = cycle_temp*10 + int(each)
    print(cycle_temp) 
    
    # 交叉口间距
    input_string2 = v2.get()
    distance = string_to_int(input_string2)
    print(distance)
    
    # 各交叉口绿信比
    input_string3 = v3.get()
    green_rate = string_to_int(input_string3)
    print(green_rate)
    
    valid = ke.coordination(cycle_temp, distance, green_rate)    
    
    v4.set(valid)

    
Button(frame,text='顺输入方向单向协调：',command=calc).grid(row=r,column=0,pady=10);r+=1
Button(frame,text='逆输入方向单向协调：',command=calc).grid(row=r,column=0,pady=10);r+=1
Button(frame,text='双向协调：',command=calc).grid(row=r,column=0,pady=10)
mainloop()
