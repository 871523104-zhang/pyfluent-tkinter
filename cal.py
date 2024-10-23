import tkinter
from tkinter import ttk
import threading as Thread
import ansys.fluent.core as pyfluent

# 资源：有对应模型的cas文件（非全部cas）
title = ['燃油增压泵滑油端', '燃油增压泵燃油端', '加力燃油泵滑油端', '加力燃油泵燃油端']

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

rhdata = {
    ('0.1MPa', '6630rpm', '无织构', '无节流环', '0.5mm', '38°', '1'):1,
    ('0.1MPa', '8565rpm', '无织构', '无节流环', '0.5mm', '38°', '1'):2,
    ('0.1MPa', '9210rpm', '无织构', '无节流环', '0.5mm', '38°', '1'):3,
    ('0.3MPa', '6630rpm', '无织构', '无节流环', '0.5mm', '38°', '1'):4,
    ('0.3MPa', '8565rpm', '无织构', '无节流环', '0.5mm', '38°', '1'):5,
    ('0.3MPa', '9210rpm', '无织构', '无节流环', '0.5mm', '38°', '1'):6,
    ('0.5MPa', '6630rpm', '无织构', '无节流环', '0.5mm', '38°', '1'):7,
    ('0.5MPa', '8565rpm', '无织构', '无节流环', '0.5mm', '38°', '1'):8,
    ('0.5MPa', '9210rpm', '无织构', '无节流环', '0.5mm', '38°', '1'):9,
    ('0.1MPa', '6630rpm', '激光脸', '无节流环', '0.5mm', '38°', '1'):10,
    ('0.1MPa', '8565rpm', '激光脸', '无节流环', '0.5mm', '38°', '1'):11,
    ('0.1MPa', '9210rpm', '激光脸', '无节流环', '0.5mm', '38°', '1'):12,
    ('0.3MPa', '6630rpm', '激光脸', '无节流环', '0.5mm', '38°', '1'):13,
    ('0.3MPa', '8565rpm', '激光脸', '无节流环', '0.5mm', '38°', '1'):14,
    ('0.3MPa', '9210rpm', '激光脸', '无节流环', '0.5mm', '38°', '1'):15,
    ('0.5MPa', '6630rpm', '激光脸', '无节流环', '0.5mm', '38°', '1'):16,
    ('0.5MPa', '8565rpm', '激光脸', '无节流环', '0.5mm', '38°', '1'):17,
    ('0.5MPa', '9210rpm', '激光脸', '无节流环', '0.5mm', '38°', '1'):18,
    ('0.1MPa', '6630rpm', '无织构', '0.1mm', '0.5mm', '38°', '1'):19,
    ('0.1MPa', '8565rpm', '无织构', '0.1mm', '0.5mm', '38°', '1'):20,
    ('0.1MPa', '9210rpm', '无织构', '0.1mm', '0.5mm', '38°', '1'):21,
    ('0.3MPa', '6630rpm', '无织构', '0.1mm', '0.5mm', '38°', '1'):22,
    ('0.3MPa', '8565rpm', '无织构', '0.1mm', '0.5mm', '38°', '1'):23,
    ('0.3MPa', '9210rpm', '无织构', '0.1mm', '0.5mm', '38°', '1'):24,
    ('0.5MPa', '6630rpm', '无织构', '0.1mm', '0.5mm', '38°', '1'):25,
    ('0.5MPa', '8565rpm', '无织构', '0.1mm', '0.5mm', '38°', '1'):26,
    ('0.5MPa', '9210rpm', '无织构', '0.1mm', '0.5mm', '38°', '1'):27,
    ('0.1MPa', '6630rpm', '无织构', '0.2mm', '0.5mm', '38°', '1'):28,
    ('0.1MPa', '8565rpm', '无织构', '0.2mm', '0.5mm', '38°', '1'):29,
    ('0.1MPa', '9210rpm', '无织构', '0.2mm', '0.5mm', '38°', '1'):30,
    ('0.3MPa', '6630rpm', '无织构', '0.2mm', '0.5mm', '38°', '1'):31,
    ('0.3MPa', '8565rpm', '无织构', '0.2mm', '0.5mm', '38°', '1'):32,
    ('0.3MPa', '9210rpm', '无织构', '0.2mm', '0.5mm', '38°', '1'):33,
    ('0.5MPa', '6630rpm', '无织构', '0.2mm', '0.5mm', '38°', '1'):34,
    ('0.5MPa', '8565rpm', '无织构', '0.2mm', '0.5mm', '38°', '1'):35,
    ('0.5MPa', '9210rpm', '无织构', '0.2mm', '0.5mm', '38°', '1'):36,
    ('0.1MPa', '6630rpm', '无织构', '0.3mm', '0.5mm', '38°', '1'):37,
    ('0.1MPa', '8565rpm', '无织构', '0.3mm', '0.5mm', '38°', '1'):38,
    ('0.1MPa', '9210rpm', '无织构', '0.3mm', '0.5mm', '38°', '1'):39,
    ('0.3MPa', '6630rpm', '无织构', '0.3mm', '0.5mm', '38°', '1'):40,
    ('0.3MPa', '8565rpm', '无织构', '0.3mm', '0.5mm', '38°', '1'):41,
    ('0.3MPa', '9210rpm', '无织构', '0.3mm', '0.5mm', '38°', '1'):42,
    ('0.5MPa', '6630rpm', '无织构', '0.3mm', '0.5mm', '38°', '1'):43,
    ('0.5MPa', '8565rpm', '无织构', '0.3mm', '0.5mm', '38°', '1'):44,
    ('0.5MPa', '9210rpm', '无织构', '0.3mm', '0.5mm', '38°', '1'):45,
    ('0.1MPa', '6630rpm', '无织构', '无节流环', '0.6mm', '38°', '1'):46,
    ('0.1MPa', '8565rpm', '无织构', '无节流环', '0.6mm', '38°', '1'):47,
    ('0.1MPa', '9210rpm', '无织构', '无节流环', '0.6mm', '38°', '1'):48,
    ('0.3MPa', '6630rpm', '无织构', '无节流环', '0.6mm', '38°', '1'):49,
    ('0.3MPa', '8565rpm', '无织构', '无节流环', '0.6mm', '38°', '1'):50,
    ('0.3MPa', '9210rpm', '无织构', '无节流环', '0.6mm', '38°', '1'):51,
    ('0.5MPa', '6630rpm', '无织构', '无节流环', '0.6mm', '38°', '1'):52,
    ('0.5MPa', '8565rpm', '无织构', '无节流环', '0.6mm', '38°', '1'):53,
    ('0.5MPa', '9210rpm', '无织构', '无节流环', '0.6mm', '38°', '1'):54,
    ('0.1MPa', '6630rpm', '无织构', '无节流环', '0.7mm', '38°', '1'):55,
    ('0.1MPa', '8565rpm', '无织构', '无节流环', '0.7mm', '38°', '1'):56,
    ('0.1MPa', '9210rpm', '无织构', '无节流环', '0.7mm', '38°', '1'):57,
    ('0.3MPa', '6630rpm', '无织构', '无节流环', '0.7mm', '38°', '1'):58,
    ('0.3MPa', '8565rpm', '无织构', '无节流环', '0.7mm', '38°', '1'):59,
    ('0.3MPa', '9210rpm', '无织构', '无节流环', '0.7mm', '38°', '1'):60,
    ('0.5MPa', '6630rpm', '无织构', '无节流环', '0.7mm', '38°', '1'):61,
    ('0.5MPa', '8565rpm', '无织构', '无节流环', '0.7mm', '38°', '1'):62,
    ('0.5MPa', '9210rpm', '无织构', '无节流环', '0.7mm', '38°', '1'):63,
    ('0.5MPa', '9210rpm', '无织构', '无节流环', '0.5mm', '35°', '1'):64,
    ('0.5MPa', '9210rpm', '无织构', '无节流环', '0.5mm', '41°', '1'):65,
    ('0.5MPa', '9210rpm', '无织构', '无节流环', '0.5mm', '38°', '2'):66,
    ('0.5MPa', '9210rpm', '无织构', '无节流环', '0.5mm', '38°', '2'):67,
}

rrdata = {
    ('0.1MPa', '6630rpm', '无织构', '2mm'):1,
    ('0.2MPa', '8565rpm', '无织构', '2mm'):2,
    ('0.3MPa', '9210rpm', '无织构', '2mm'):3,
    ('0.1MPa', '6630rpm', '人字槽', '2mm'):4,
    ('0.2MPa', '8565rpm', '人字槽', '2mm'):5,
    ('0.3MPa', '9210rpm', '人字槽', '2mm'):6,
    ('0.1MPa', '6630rpm', '螺旋槽', '2mm'):7,
    ('0.2MPa', '8565rpm', '螺旋槽', '2mm'):8,
    ('0.3MPa', '9210rpm', '螺旋槽', '2mm'):9,
    ('0.1MPa', '6630rpm', '无织构', '3mm'):10,
    ('0.2MPa', '8565rpm', '无织构', '3mm'):11,
    ('0.3MPa', '9210rpm', '无织构', '3mm'):12
}
ddict = [rh_dict, rr_dict, jh_dict, jr_dict]

# 线程启动标志
threadStart = False
class myThread(Thread.Thread):
    def run(self):
        global threadStart
        if threadStart == False:
            print('fluent thread starting...')
            self.solver = pyfluent.launch_fluent(product_version='22.2.0', mode='solver')
            self.solver.tui.file.read_case("source\\case\\1.1.cas")
            print('fluent started')
            calInformationLabel.config(text='可计算')
            threadStart = True
        else:
            pass
    
# 验证输入合法（仅数字）
def validate_input(entry, i):
    input_text = entry.get()
    try:
        float(input_text)
        return True
    except ValueError:
        tkinter.messagebox.showwarning('提示', '请输入数字。')
        return False

# 获取frame中的输入并组合成列表
def frameInput(frameIndex):
    key = ddict[frameIndex].keys()
    input = [ddict[frameIndex][i].get() for i in key]
    return input

# 开启并进行fluent计算
def rhget_result(input, iteration, fluentThread):
    print('开始计算rh')
    # 获取输入数据
    print(input, iteration)
    fluentThread.run()
    if input[0] == '1':
        fluentThread.solver.tui.define.boundary_conditions.set.velocity_inlet('inlet', '()', 'mixture', 'vmag', 'n', 24.7, 'q')
        fluentThread.solver.tui.solve.initialize.hyb_initialization()
        fluentThread.solver.tui.solve.iterate(iteration)
        print('calfinished')
        
def rrget_result(input):
    print('开始计算rr')
    print(input)
    
def jhget_result(input):
    print('开始计算jh')
    print(input)
    
def jrget_result(input):
    print('开始计算jr')
    print(input)
    
    
def cal_window():
    global calMaster, calInformationLabel
    calMaster = tkinter.Toplevel()
    calMaster.title('机械密封装置仿真APP:流体传热仿真')
    calMaster.geometry('1000x700')
    calMaster.resizable(False, False)
    calInformationLabel = tkinter.Label(calMaster, text='等待fluent启动')
    calInformationLabel.grid(row=3, column=0, columnspan=4)

    # 打开fluent进程
    fluentThread = myThread()

    CalTitle = tkinter.PhotoImage(file='source\\img\\titleCal.png')
    title_label = tkinter.Label(calMaster, image=CalTitle)
    title_label.grid(row=0, column=0, columnspan=4)
    
    frame1 = tkinter.Frame(calMaster, bd=6, bg='#DAE3F3',relief='groove', height=350, width=230,
                           highlightcolor='red',
                           highlightthickness=2)
    frame1.grid_propagate(0)
    frame1.grid(row=1, column=0)
    frame2 = tkinter.Frame(calMaster, bd=6, bg='#DAE3F3',relief='groove', height=350, width=230,
                           highlightcolor='red',
                           highlightthickness=2)
    frame2.grid_propagate(0)
    frame2.grid(row=1, column=1)
    frame3 = tkinter.Frame(calMaster, bd=6, bg='#DAE3F3',relief='groove', height=350, width=230,
                           highlightcolor='red',
                           highlightthickness=2)
    frame3.grid_propagate(0)
    frame3.grid(row=1, column=2)
    frame4 = tkinter.Frame(calMaster, bd=6, bg='#DAE3F3',relief='groove', height=350, width=230,
                           highlightcolor='red',
                           highlightthickness=2)
    frame4.grid_propagate(0)
    frame4.grid(row=1, column=3)

    frame = [frame1, frame2, frame3, frame4]
    func = [rhget_result, rrget_result, jhget_result, jrget_result]
    
    # 创建label和combobox
    for frameIndex in range(4):
        title_label = tkinter.Label(frame[frameIndex], text=title[frameIndex], font=('黑体',18,'bold'), bg='#DAE3F3', foreground='#0a1220')
        title_label.grid(row=0, column=0, columnspan=2)
        j=1
        
        for key, value in ddict[frameIndex].items():
            label = tkinter.Label(frame[frameIndex], text=key, pady=6, bg='#DAE3F3')
            label.grid(row=j, column=0)
            if key in ['压力', '转速']:
                ddict[frameIndex][key] = tkinter.Entry(frame[frameIndex], width=13, validate='focusout', 
                                              validatecommand=lambda i=frameIndex, key=key:validate_input(ddict[i][key], i))
                ddict[frameIndex][key].insert(0, '0.00')
                ddict[frameIndex][key].grid(row=j, column=1)
                j = j+1
            else:
                ddict[frameIndex][key] = ttk.Combobox(frame[frameIndex], width=10)
                ddict[frameIndex][key]['values'] = value
                ddict[frameIndex][key].current(0)
                ddict[frameIndex][key].grid(row=j, column=1)
                j = j+1

        iterationLabel = tkinter.Label(frame[frameIndex], text='迭代次数')
        iterationLabel.grid(row=j, column=0)
        iterationSpinboxValue = tkinter.StringVar()
        iterationSpinbox = tkinter.Spinbox(frame[frameIndex], textvariable=iterationSpinboxValue)
        iterationSpinbox.grid(row=j, column=1)
        run_button = tkinter.Button(frame[frameIndex], 
                                    text=f'{title[frameIndex]}\n获取结果', 
                                    font=('宋体',14,'bold'), 
                                    bg='#acafc9', 
                                    command=lambda frameIndex=frameIndex:func[frameIndex](frameInput(frameIndex), iterationSpinboxValue.get(), fluentThread))
        run_button.grid(row=j+1, column=0, columnspan=2)
        
    QueryBottom = tkinter.PhotoImage(file='source\\img\\bottomQuery.png')
    bottom_label = tkinter.Label(calMaster, image=QueryBottom)
    bottom_label.grid(row=2, column=0, columnspan=4)
    
    calMaster.mainloop()