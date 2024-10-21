import tkinter
from data import SharedData
from query import query_window
from cal import cal_window
from rebianixng import rebianixng_window
from minganixng import minganxing_window


shared_data = SharedData()
master = tkinter.Tk()
master.title('机械密封装置仿真APP')
master.geometry('525x300')
master.resizable(False, False)


master_title = tkinter.PhotoImage(file='source\\img\\title1.png')
title_label = tkinter.Label(master, image=master_title)
title_label.grid(row=0, column=0, columnspan=2)

query_open_button = tkinter.Button(master, text='结果查询(参数化建模)', width=30, height=3, font=40, command=lambda:query_window(shared_data))
query_open_button.grid(row=1, column=0)
cal_open_button = tkinter.Button(master, text='流体传热仿真', width=30, height=3, font=40, command=lambda:cal_window(shared_data))
cal_open_button.grid(row=1, column=1)
rebianxing_open_button = tkinter.Button(master, text='热变形仿真', width=30, height=3, font=40, command=rebianixng_window)
rebianxing_open_button.grid(row=2, column=0)
minganxing_open_button = tkinter.Button(master, text='参数敏感性及参数优化仿真', width=30, height=3, font=40, command=minganxing_window)
minganxing_open_button.grid(row=2, column=1)

master.mainloop()
