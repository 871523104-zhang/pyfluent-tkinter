# 参数化建模（计算结果查询）
import tkinter
from tkinter import ttk

rh_dict = {'压力':('0.1MPa', '0.3MPa', '0.5MPa'),
           '转速':('6630rpm', '8565rpm', '9210rpm'),
           '节流环间隙':('0.1mm', '0.2mm', '0.3mm'),
           '喷淋管径':('0.5mm', '0.6mm', '0.7mm'),
           '织构':('无织构', '激光脸'),
           '喷淋角度':('35°', '38°', '41°'),
           '喷淋管数':('2', '3')}
rr_dict = {'压力':('0.1MPa', '0.2MPa', '0.3MPa'),
           '转速':('6630rpm', '8565rpm', '9210rpm'),
           '出口直径':('2mm', '3mm'),
           '织构':('无织构', '人字槽', '螺旋槽')}
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
    result_dict=[]
    i=1
    for key in rh_dict.keys():
        result_dict.append(rh_dict[key].get())
        i = i+1
    print(result_dict)
    
def rrget_result():
    result_dict=[]
    i=1
    for key in rr_dict.keys():
        result_dict.append(rr_dict[key].get())
        i = i+1
    print(result_dict)
    
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

    frame1 = tkinter.Frame(master, bd=3, relief='sunken', height=200)
    frame1.grid(row=1, column=0)
    frame2 = tkinter.Frame(master, bd=3, relief='sunken', height=200)
    frame2.grid(row=1, column=1)
    frame3 = tkinter.Frame(master, bd=3, relief='sunken', height=200)
    frame3.grid(row=1, column=2)
    frame4 = tkinter.Frame(master, bd=3, relief='sunken', height=200)
    frame4.grid(row=1, column=3)
    
    frame = [frame1, frame2, frame3, frame4]
    title = ['燃油增压泵滑油端', '燃油增压泵燃油端', '加力燃油泵滑油端', '加力燃油泵燃油端']

    ddict = [rh_dict, rr_dict, jh_dict, jr_dict]
    func = [rhget_result, rrget_result, jhget_result, jrget_result]
    
    # 创建label和combobox
    for i in range(4):
        title_label = tkinter.Label(frame[i], text=title[i], font=('黑体',14))
        title_label.grid(row=0, column=0, pady=10)
        j=1
        for key, value in ddict[i].items():
            label = tkinter.Label(frame[i], text=key, justify='left', anchor='w', width=10)
            label.grid(row=j, column=0, pady=5)
            ddict[i][key] = ttk.Combobox(frame[i], width=10)
            ddict[i][key]['values'] = value
            ddict[i][key].current(0)
            ddict[i][key].grid(row=j, column=1)
            j = j+1
        run_button = tkinter.Button(frame[i], text=f'{title[i]}\n获取结果', command=func[i])
        run_button.grid(row=j, column=0, columnspan=2)
        
    master.mainloop()