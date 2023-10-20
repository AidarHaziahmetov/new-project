from main import FCFS
from tkinter import *
from tkinter import ttk

fcfs = FCFS()
    
def add_and_show():
    fcfs.process_add(int(entry.get()))
    entry.delete(0, END)
    for i in range(sum(fcfs.process_list)):
        Label(frame1, text=f'{i+1}',bg='grey',width=3,height=1).grid(column=i+1,row=0,columnspan=1,rowspan=1)
    for i in range(len(fcfs.process_list)):
        Label(frame1, text=f'Процесс {i+1}',width=15,height=1).grid(column=0,row=i+1,columnspan=1,rowspan=1)
        for j in range(sum(fcfs.process_list[0:i+1])):
            if j>=sum(fcfs.process_list[0:i]):
                Label(frame1, text='И',width=3,height=1).grid(column=j+1,row=i+1,columnspan=1,rowspan=1)
            else:
                Label(frame1, text='Г',width=3,height=1).grid(column=j+1,row=i+1,columnspan=1,rowspan=1)

def del_and_show():
    fcfs.process_clean()
    label_avg_process_time_wait['text'] = 'Среднее время ожидания:'
    label_avg_process_time['text'] = 'Среднее время выполнения:'
    for i in frame1.grid_slaves():
        if (int(i.grid_info()["row"]) != 0) or (int(i.grid_info()["column"]) != 0):
            i.grid_forget()

def count_and_show():
    fcfs.avg_process_time_counting()
    label_avg_process_time_wait['text'] = f'Среднее время ожидания: {fcfs.avarage_time_of_waiting}'
    label_avg_process_time['text'] = f'Среднее время выполнения: {fcfs.avarage_full_time}'

root = Tk()
root.title('FCFS')
root.geometry('1000x500')



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
label_avg_process_time_wait = Label(frame3,text='Среднее время ожидания:')
label_avg_process_time_wait.pack(pady=[10,3])
label_avg_process_time = Label(frame3,text='Среднее время выполнения:')
label_avg_process_time.pack(pady=3)
btn_calculate = Button(frame3, text="Вычислить", command=count_and_show)
btn_calculate.pack(ipady=5,ipadx=9,pady=3)




frame1 = Frame(root)# Будующая таблица
frame1.place(relx=0,rely=0,relheight=0.65,relwidth=0.8)
label_process = Label(frame1, text='Процесс',bg='grey',textvariable='v',width=15,height=1).grid(column=0,row=0,columnspan=1,rowspan=1)

root.mainloop()