import tkinter

win = tkinter.Tk()
# Размеры меню
win.title('Мое приложения')
win.geometry('745x605+700+200')
# win.resizable(width = False, height = False)

# Фото
photo = tkinter.PhotoImage(file='application/icon.png')
win.iconphoto(False, photo)

# Цвет фона
win.config(bg = 'black')


# Функции поля

def test(number):
    if entry.get() == 'Ошибка':
        clean()
    a = entry.get()
    if a[0] == '0' and len(a) == 1:
        a = a[1:]
    entry.delete(0, 'end')
    entry.insert('end', a + number)
    if len(a) > 10:
        a = a[0:10]
        entry.delete(11, 'end')


def point(s):
    a = entry.get()
    for i in reversed(a):
        if not i.isdigit():
            if i in '+-/*':
                if a[-1] == '+' or a[-1] == '-' or a[-1] == '/' or a[-1] == '*':
                    print('test')
                    return entry.insert('end', '0' + s)
                print('qwqer')
                entry.delete(0, 'end')
                return entry.insert('end', a + s)
            if i == '.':
                return None    
    for i in reversed(a):
        if i.isdigit():
            print('yos')
            entry.delete(0, 'end')
            return entry.insert('end', a + s)
              



    

      
def calculations():
    try:
        if entry.get() == 'Ошибка':
            clean()
        a = entry.get()
        if a[-1] not in '+-*/':    
            entry.delete(0, 'end')
            entry.insert('end', eval(a))
            print('fe')
    except ZeroDivisionError:
        entry.insert('end', 'Ошибка')




def stop():
    entry.delete(10)

    

def operations(oper):
    if entry.get() == 'Ошибка':
        clean()
    a = entry.get()
    if a[-1] in '+-/*':
        a = a[:-1]
        print('da')   
    entry.delete(0, 'end')    
    entry.insert('end', a + oper)
    
    


def clean():
    entry.delete(0, 'end')
    entry.insert(0, '0')    
    

    
def back():
    a = entry.get()
    entry.delete(0, 'end')
    a = a[0:-1]
    entry.insert(0, a)
    if len(entry.get()) == 0:
        entry.insert(0, '0')


    


    



# Поля
entry = tkinter.Entry(win, justify = tkinter.RIGHT, font = ('Arial',50))
entry.insert(0, '0')
entry.grid(row = 0, column = 0, columnspan = 4, stick = 'wesn')

# создание кнопок
btn_1 = tkinter.Button(win, text = '1', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('1'))
btn_2 = tkinter.Button(win, text = '2', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('2'))
btn_3 = tkinter.Button(win, text = '3', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('3'))
btn_4 = tkinter.Button(win, text = '4', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('4'))
btn_5 = tkinter.Button(win, text = '5', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('5'))
btn_6 = tkinter.Button(win, text = '6', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('6'))
btn_7 = tkinter.Button(win, text = '7', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('7'))
btn_8 = tkinter.Button(win, text = '8', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('8'))
btn_9 = tkinter.Button(win, text = '9', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('9'))
btn_0 = tkinter.Button(win, text = '0', font = ('Arial', 20), bd = 4, bg = 'grey', fg = 'white', command = lambda: test('0'))
btn_point = tkinter.Button(win, text = '.', font = ('Arial', 30), bg = 'grey', fg = 'white', bd = 4, command = lambda:point('.')) 


# Операции
plus = tkinter.Button(win, text = '+', font = ('Arial', 25), bd = 4, fg = 'orange', command = lambda:operations('+'))
minus = tkinter.Button(win, text = '-', font = ('Arial', 30), bd = 4, fg = 'orange', command = lambda:operations('-'))
multiplication = tkinter.Button(win, text = 'x', font = ('Arial', 20), bd = 4, fg = 'orange', command = lambda:operations('*'))
division = tkinter.Button(win, text = '÷', font = ('Arial', 30), bd = 4, fg = 'orange', command = lambda:operations('/'))
equals = tkinter.Button(win, text = '=', font = ('Arial', 30), bd = 4, fg = 'orange', command = calculations)
ac = tkinter.Button(win, text = 'AC', font = ('Arial', 20), bd = 4, fg = 'orange', command = clean)
btn_del = tkinter.Button(win, text = 'back', font = ('Arial', 20), bg = 'grey', fg = 'white', command = back) 

# размещения кнопок
btn_1.grid(row = 2, column = 0, stick = 'wesn', padx = 5, pady = 5)
btn_2.grid(row = 2, column = 1, stick = 'wesn', padx = 5, pady = 5)
btn_3.grid(row = 2, column = 2, stick = 'wesn', padx = 5, pady = 5)
btn_4.grid(row = 3, column = 0, stick = 'wesn', padx = 5, pady = 5)
btn_5.grid(row = 3, column = 1, stick = 'wesn', padx = 5, pady = 5)
btn_6.grid(row = 3, column = 2, stick = 'wesn', padx = 5, pady = 5)
btn_7.grid(row = 4, column = 0, stick = 'wesn', padx = 5, pady = 5)
btn_8.grid(row = 4, column = 1, stick = 'wesn', padx = 5, pady = 5)
btn_9.grid(row = 4, column = 2, stick = 'wesn', padx = 5, pady = 5)
btn_0.grid(row = 5, column = 0, stick = 'wesn', padx = 5, pady = 5)
btn_point.grid(row = 5, column = 3, stick = 'wesn', padx = 5, pady = 5)


# размещения кнопок операции
plus.grid(row = 1, column = 3, stick = 'wesn', padx = 5, pady = 5)
minus.grid(row = 2, column = 3, stick = 'wesn', padx =5, pady = 5)
multiplication.grid(row = 3, column = 3, stick = 'wesn', padx = 5, pady = 5)
division.grid(row = 4, column = 3, stick = 'wesn', padx = 5, pady = 5)
equals.grid(row = 1, column = 0, stick = 'wesn', padx = 5, pady = 5, columnspan = 3)
ac.grid(row = 5, column = 2, stick = 'wesn ', padx = 5, pady = 5)
btn_del.grid(row = 5, column = 1, stick = 'wesn', padx = 5, pady = 5)


    
# доп конфигурации
win.grid_columnconfigure(0, minsize = 130)
win.grid_columnconfigure(1, minsize = 130)
win.grid_columnconfigure(2, minsize = 130)
win.grid_columnconfigure(3, minsize = 130)



win.grid_rowconfigure(0, minsize = 100)  
win.grid_rowconfigure(1, minsize = 100) 
win.grid_rowconfigure(2, minsize = 100) 
win.grid_rowconfigure(3, minsize = 100) 
win.grid_rowconfigure(4, minsize = 100)
win.grid_rowconfigure(5, minsize = 100)  


win.mainloop()