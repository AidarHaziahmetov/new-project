from main import FCFS
from tkinter import *
from tkinter import ttk

fcfs = FCFS()
    
def add_and_show():

    fcfs.process_add(int(entry.get()))
    entry.delete(0, END)
    fcfs.calculate_visual_representation()

    for i in frame1.grid_slaves():
            i.grid_forget()
    label_process = Label(frame1, text='Процесс',bg='grey',textvariable='v',width=15,height=1).grid(column=0,row=0,columnspan=1,rowspan=1)

    for i in range(sum(fcfs.process_list)):
        Label(frame1, text=f'{i+1}',bg='grey',width=3,height=1).grid(column=i+1,row=0,columnspan=1,rowspan=1)
    
    for i in range(len(fcfs.visual_representation)):
         Label(frame1, text=f'Процесс {i+1}',width=15,height=1).grid(column=0,row=i+1,columnspan=1,rowspan=1)
         for j in range(len(fcfs.visual_representation[i])):
              Label(frame1, text=f'{fcfs.visual_representation[i][j]}',width=3,height=1).grid(column=j+1,row=i+1,columnspan=1,rowspan=1)


def del_and_show():
    fcfs.process_clean()
    fcfs.visual_representation = []
    for i in frame1.grid_slaves():
        if (int(i.grid_info()["row"]) != 0) or (int(i.grid_info()["column"]) != 0):
            i.grid_forget()

def count_and_show():
    a = fcfs.calculate_time()
    if fcfs.__class__ == FCFS:
        label1['text'] = a[0]
        label2['text'] = a[1 ]
    # for i in range(len(a)):
    #     Label(frame3, text=f'{a[i]}',width=25,height=2).pack(pady=3)

root = Tk()
root.title('FCFS')
root.geometry('1000x400')


frame = Frame(root)
frame.place(relx=0,rely=0,relheight=0.65,relwidth=0.8)

canvas = Canvas(frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

yscrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
yscrollbar.pack(side=RIGHT, fill=Y)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL, command=canvas.xview)
xscrollbar.pack(side=BOTTOM, fill=X, padx=(0, yscrollbar.winfo_width()))

canvas.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

# Создаем внутренний фрейм, на котором будут размещены виджеты
frame1 = Frame(canvas)
frame1.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame1, anchor="nw")


frame2 = Frame(root)
frame2.place(relx=0.8,rely=0,relheight=0.65,relwidth=0.2)

label_process_time = Label(frame2,text='Процессорное время')
label_process_time.pack(ipady=6)
entry = Entry(frame2)
entry.pack(ipady=5,pady=3)
btn_add_process = Button(frame2, text="Добавить процесс", command=add_and_show)
btn_add_process.pack(ipady=5,ipadx=7,pady=3)
btn_clean_process = Button(frame2, text="Сброс процессов",command=del_and_show)
btn_clean_process.pack(ipady=5,ipadx=9,pady=3)




frame3 = Frame(root)
frame3.place(relx=0,rely=0.65,relheight=0.35,relwidth=0.4)
if fcfs.__class__ == FCFS:
        label1 = Label(frame3, text="Среднее время ожидания: ",width=25,height=2)
        label1.pack(pady=3)
        label2 = Label(frame3, text="Среднее время выполнения: ",width=25,height=2)
        label2.pack(pady=3)
# label_avg_process_time_wait = Label(frame3,text='Среднее время ожидания:')
# label_avg_process_time_wait.pack(pady=[10,3])
# label_avg_process_time = Label(frame3,text='Среднее время выполнения:')
# label_avg_process_time.pack(pady=3)
btn_calculate = Button(frame3, text="Вычислить", command=count_and_show)
btn_calculate.pack(ipady=5,ipadx=9,pady=3)


label_process = Label(frame1, text='Процесс',bg='grey',textvariable='v',width=15,height=1).grid(column=0,row=0,columnspan=1,rowspan=1)

root.mainloop()
