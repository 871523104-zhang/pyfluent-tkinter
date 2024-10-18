import tkinter
from tkinter import ttk
from threading import Thread
import ansys.fluent.core as pyfluent
from data import title, rhdata, rrdata, rh_dict, rr_dict, jh_dict, jr_dict

# 资源：有对应模型的cas文件（非全部cas）

def run_fluent():
    solver = pyfluent.launch_fluent(product_version='22.2.0', mode='solver')
    solver.tui.file.read_case("source\\case\\1.1.cas")

# 开启新线程：fluent
def start_fluent():
    Thread(target=run_fluent).start()
    
# 验证输入合法（仅数字）
def validate_input(entry):
    input_text = entry.get()
    if not input_text.isdigit():
        tkinter.messagebox.showwarning('提示', '请输入数字。')
    # else:
    #     tkinter.messagebox.showwarning('提示', '请输入数字。')

# 开启并进行fluent计算
def rhget_result():
    print('开始计算rh')
def rrget_result():
    print('开始计算rr')
def jhget_result():
    print('开始计算jh')
def jrget_result():
    print('开始计算jr')
    
def cal_window():
    master = tkinter.Toplevel()
    master.title('机械密封装置仿真APP:流体传热仿真')
    master.geometry('1000x600')
    master.resizable(False, False)

    CalTitle = tkinter.PhotoImage(file='source\\img\\titleCal.png')
    title_label = tkinter.Label(master, image=CalTitle)
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
            if key == '压力' or key == '转速': # , validatecommand=lambda:validate_input(ddict[i][key])
                ddict[i][key] = tkinter.Entry(frame[i], width=13)
                ddict[i][key].insert(0, '0.00')
                ddict[i][key].grid(row=j, column=1)
                j = j+1
            else:
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