# 参数化建模（计算结果查询）
import tkinter
from tkinter import ttk
import tkinter.messagebox
import os

# 资源：结果图片

# 还需要按照rh和rr更改jr和jh函数。
# 还需要录入jrdata和jhdata。
# 还需要在img文件夹中输入对应图片，命名格式1/2/3/4.{id}.1/2.png

def rhget_result(shared_data):
    result_dict=()
    i=1
    for key in shared_data.rh_dict.keys():
        result_dict = result_dict + (shared_data.rh_dict[key].get(), )
        i = i+1
    id = shared_data.rhdata.get(result_dict, 'id not found')
    # 在 没找到id 或 没找到id对应文件（结果未录入）时展示
    if id == 'id not found':
        tkinter.messagebox.showwarning('提示', '您所选择的组合不存在。\n请重新输入。')
    elif not os.path.exists(f'source\\img\\1.{id}.1.png'):
        tkinter.messagebox.showwarning('提示', '您所选择的模型计算结果未录入，请等待录入。')
    # 展示结果
    else:
        result_window = tkinter.Toplevel()
        result_window.title('查询结果')
        result_window.geometry('1600x600')
        label1 = tkinter.Label(result_window, text='流域流动截面云图', font=('黑体', 20))
        label1.grid(row=0, column=0)
        result1 = tkinter.PhotoImage(file=f'source\\img\\1.{id}.1.png')
        result1_label = tkinter.Label(result_window, image=result1)
        result1_label.grid(row=1, column=0)
        label2 = tkinter.Label(result_window, text='密封副温度分布云图', font=('黑体', 20))
        label2.grid(row=0, column=1)
        result2 = tkinter.PhotoImage(file=f'source\\img\\1.{id}.2.png')
        result2_label = tkinter.Label(result_window, image=result2)
        result2_label.grid(row=1, column=1)
        result_window.mainloop()
    
def rrget_result(shared_data):
    result_dict=()
    i=1
    for key in shared_data.rr_dict.keys():
        result_dict = result_dict + (shared_data.rr_dict[key].get(), )
        i = i+1
    id = shared_data.rrdata.get(result_dict, 'id not found')
    if id == 'id not found':
        tkinter.messagebox.showwarning('提示', '您所选择的组合不存在。\n请重新输入。')
    elif not os.path.exists(f'source\\img\\2.{id}.1.png'):
        tkinter.messagebox.showwarning('提示', '您所选择的模型计算结果未录入，请等待录入。')
    else:
        result_window = tkinter.Toplevel()
        result_window.title('查询结果')
        result_window.geometry('1600x600')
        label1 = tkinter.Label(result_window, text='流域流动截面云图', font=('黑体', 20))
        label1.grid(row=0, column=0)
        result1 = tkinter.PhotoImage(file=f'source\\img\\2.{id}.1.png')
        result1_label = tkinter.Label(result_window, image=result1)
        result1_label.grid(row=1, column=0)
        label2 = tkinter.Label(result_window, text='密封副温度分布云图', font=('黑体', 20))
        label2.grid(row=0, column=1)
        result2 = tkinter.PhotoImage(file=f'source\\img\\2.{id}.2.png')
        result2_label = tkinter.Label(result_window, image=result2)
        result2_label.grid(row=1, column=1)
        result_window.mainloop()
    
def jhget_result(shared_data):
    result_dict=[]
    i=1
    for key in shared_data.jh_dict.keys():
        result_dict.append(shared_data.jh_dict[key].get())
        i = i+1
    print(result_dict)
    
def jrget_result(shared_data):
    result_dict=[]
    i=1
    for key in shared_data.jr_dict.keys():
        result_dict.append(shared_data.jr_dict[key].get())
        i = i+1
    print(result_dict)

def query_window(shared_data):
    master = tkinter.Toplevel()
    master.title('机械密封装置仿真APP:计算结果查询')
    master.geometry('1000x600')
    master.resizable(False, False)

    QueryTitle = tkinter.PhotoImage(file='source\\img\\titleQuery.png')
    title_label = tkinter.Label(master, image=QueryTitle)
    title_label.grid(row=0, column=0, columnspan=4)

    
    frame1 = tkinter.Frame(master, bd=6, bg='#DAE3F3',relief='groove', height=350, width=230,
                           highlightcolor='red',
                           highlightthickness=2)
    frame1.grid_propagate(0)
    frame1.grid(row=1, column=0)
    frame2 = tkinter.Frame(master, bd=6, bg='#DAE3F3',relief='groove', height=350, width=230,
                           highlightcolor='red',
                           highlightthickness=2)
    frame2.grid_propagate(0)
    frame2.grid(row=1, column=1)
    frame3 = tkinter.Frame(master, bd=6, bg='#DAE3F3',relief='groove', height=350, width=230,
                           highlightcolor='red',
                           highlightthickness=2)
    frame3.grid_propagate(0)
    frame3.grid(row=1, column=2)
    frame4 = tkinter.Frame(master, bd=6, bg='#DAE3F3',relief='groove', height=350, width=230,
                           highlightcolor='red',
                           highlightthickness=2)
    frame4.grid_propagate(0)
    frame4.grid(row=1, column=3)
    
    frame = [frame1, frame2, frame3, frame4]

    ddict = [shared_data.rh_dict, shared_data.rr_dict, shared_data.jh_dict, shared_data.jr_dict]
    func = [lambda:rhget_result(shared_data),
            lambda:rrget_result(shared_data),
            lambda:jhget_result(shared_data),
            lambda:jrget_result(shared_data)]
    
    # 创建label和combobox
    for i in range(4):
        title_label = tkinter.Label(frame[i], text=shared_data.title[i], font=('黑体',18,'bold'), bg='#DAE3F3',
                                    foreground='#0a1220')
        title_label.grid(row=0, column=0, columnspan=2)
        j=1
        for key, value in ddict[i].items():
            label = tkinter.Label(frame[i], text=key, pady=6, bg='#DAE3F3')
            label.grid(row=j, column=0)
            ddict[i][key] = ttk.Combobox(frame[i], width=10)
            ddict[i][key]['values'] = value
            ddict[i][key].current(0)
            ddict[i][key].grid(row=j, column=1)
            j = j+1
        run_button = tkinter.Button(frame[i], text=f'{shared_data.title[i]}\n获取结果', font=('宋体',14,'bold'), 
                                    bg='#acafc9', command=func[i])
        run_button.grid(row=j, column=0, columnspan=2)
        
    QueryBottom = tkinter.PhotoImage(file='source\\img\\bottomQuery.png')
    bottom_label = tkinter.Label(master, image=QueryBottom)
    bottom_label.grid(row=2, column=0, columnspan=4)
    
    master.mainloop()