rhmodel = {
    ('无织构', '无节流环', '0.5mm', '38°', '1'):1,
    ('激光脸', '无节流环', '0.5mm', '38°', '1'):10,
    ('无织构', '0.1mm', '0.5mm', '38°', '1'):19,
    ('无织构', '0.2mm', '0.5mm', '38°', '1'):28,
    ('无织构', '0.3mm', '0.5mm', '38°', '1'):37,
    ('无织构', '无节流环', '0.6mm', '38°', '1'):46,
    ('无织构', '无节流环', '0.7mm', '38°', '1'):55,
    ('无织构', '无节流环', '0.5mm', '35°', '1'):64,
    ('无织构', '无节流环', '0.5mm', '41°', '1'):65,
    ('无织构', '无节流环', '0.5mm', '38°', '2'):66
}

partial_tuple = ('激光脸', '无节流环', '0.2mm', '38°', '1')

try:
    rhmodel[partial_tuple]
    print(f'找到对应值:{rhmodel[partial_tuple]}')
except:
    print('没找到')