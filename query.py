# 参数化建模（计算结果查询）
import tkinter
from tkinter import ttk
import tkinter.messagebox
from data import rhdata, rrdata

# 还需要按照rh和rr更改jr和jh函数。
# 还需要录入jrdata和jhdata。
# 还需要在img文件夹中输入对应图片，命名格式1/2/3/4.{id}.1/2.png

rh_dict = {'压力':('0.1MPa', '0.3MPa', '0.5MPa'),
           '转速':('6630rpm', '8565rpm', '9210rpm'),
           '织构':('无织构', '激光脸'),
           '节流环间隙':('无节流环', '0.1mm', '0.2mm', '0.3mm'),
           '喷淋管径':('0.5mm', '0.6mm', '0.7mm'),
           '喷淋角度':('38°', '35°', '41°'),
           '喷淋管数':('1', '2')}
rr_dict = {'压力':('0.1MPa', '0.2MPa', '0.3MPa'),
           '转速':('6630rpm', '8565rpm', '9210rpm'),
           '织构':('无织构', '人字槽', '螺旋槽'),
           '出口直径':('2mm', '3mm')}
jh_dict = {'转速':('18835rpm', '21255rpm', '22600rpm', '23950rpm', '25560rpm', '26906rpm'),
           '压力':('0.25MPa', '0.3MPa', '0.35MPa'),
           '入口管径':('0.7mm', '0.8mm'),
           '织构':('无织构', '激光脸(新)'),
           '喷淋角度':('14.5°', '11.5°', '17.5°')}
jr_dict = {'转速':('18835rpm', '21255rpm', '22600rpm', '23950rpm', '25560rpm', '26906rpm'),
           '流速':('1900-2000ml/min', '2300-2400ml/min'),
           '织构':('无织构', '激光脸(新)'),
           '进口管径':('1mm', '1.5mm')}

def rhget_result():
    result_dict=()
    i=1
    for key in rh_dict.keys():
        result_dict = result_dict + (rh_dict[key].get(), )
        i = i+1
    id = rhdata.get(result_dict, 'id not found')
    if id == 'id not found':
        tkinter.messagebox.showwarning('提示', '您所选择的组合不存在。\n请重新输入。')
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
    
def rrget_result():
    result_dict=()
    i=1
    for key in rr_dict.keys():
        result_dict = result_dict + (rr_dict[key].get(), )
        i = i+1
    id = rrdata.get(result_dict, 'id not found')
    if id == 'id not found':
        tkinter.messagebox.showwarning('提示', '您所选择的组合不存在。\n请重新输入。')
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
    
def jhget_result():
    result_dict=[]
    i=1
    for key in jh_dict.keys():
        result_dict.append(jh_dict[key].get())
        i = i+1
    print(result_dict)
    
def jrget_result():
    result_dict=[]
    i=1
    for key in jr_dict.keys():
        result_dict.append(jr_dict[key].get())
        i = i+1
    print(result_dict)

def query_window():
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
    title = ['燃油增压泵滑油端', '燃油增压泵燃油端', '加力燃油泵滑油端', '加力燃油泵燃油端']

    ddict = [rh_dict, rr_dict, jh_dict, jr_dict]
    func = [rhget_result, rrget_result, jhget_result, jrget_result]
    
    # 创建label和combobox
    for i in range(4):
        title_label = tkinter.Label(frame[i], text=title[i], font=('黑体',18,'bold'), bg='#DAE3F3',
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
        run_button = tkinter.Button(frame[i], text=f'{title[i]}\n获取结果', font=('宋体',14,'bold'), 
                                    bg='#acafc9', command=func[i])
        run_button.grid(row=j, column=0, columnspan=2)
        
    QueryBottom = tkinter.PhotoImage(file='source\\img\\bottomQuery.png')
    bottom_label = tkinter.Label(master, image=QueryBottom)
    bottom_label.grid(row=2, column=0, columnspan=4)
    
    master.mainloop()