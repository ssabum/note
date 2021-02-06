# import tkinter.ttk as ttk
# import tkinter.messagebox as msgbox
# from tkinter import *

# root = Tk()
# root.title('basic GUI')
# root.geometry('640x480+100+150') # 가로 * 세로 + x좌표 + y좌표
# root.resizable(False, False) # 크기 변경 불가

# btn = Button(root, fg='red', bg='yellow', padx=5, pady=10, text='버튼') # width, height는 고정길이
# btn.pack()

# photo = PhotoImage(file='./img.png')
# btn2 = Button(root, image=photo)
# btn2.pack()

# def btncmd():
#     print('버튼이 클릭되었어요')

# btn3 = Button(root, text='동작하는 버튼', command=btncmd)
# btn3.pack()
# label1 = Label(root, text='안녕하세요')
# label1.pack()

# def change():
#     label1.config(text='또 만나요')

# bnt = Button(root, text='클릭', command=change)
# bnt.pack()

# txt = Text(root,width=30, height=5)
# txt.pack()
# txt.insert(END, '글자를 입력하세요')
# txt.get('1.0', END)

# e = Entry(root, width=30)
# e.pack()
# e.get()

# listbox = Listbox(root, selectmode='extended', height=0)
# listbox.insert(END, '사과')
# listbox.curselection()

# chkvar = IntVar()
# chkbox = Checkbutton(root, text='오늘 하루 보지 않기', variable=chkvar)
# chkbox.pack()

# radio_var = IntVar()
# btn_radiobutton = Radiobutton(root, text='버거', value=1, variable=radi_bar)

# values = [str(i) + '일' for i in range(1, 32)]
# combobox = ttk.Combobox(root, height=5, values=values, state='readonly')
# combobox.set('날짜 선택')
# combobox.current(0)

# p_var = DoubleVar()
# progressbar = ttk.Progressbar(root, maximum=100, length=150, mode='determinate', variable=p_var)
# progressbar.start() # ms 마다 움직임

# menu = Menu(root)
# menu_file = Menu(menu, tearoff=0)
# menu_file.add_command(label='new file', command=create_new_file, state='disable')
# menu_file.add_separator()
# menu_file.add_command(label='exit', command=root.quit)

# menu.add_cascade(label='File', menu=menu_file)

# root.config(menu=menu)

# def info():
#     msgbox.showinfo('알림', '정상적으로 완료되었습니다.')

# Button(root, command=info, text='알림').pack()

# frame_bugger = LableFrame(root, relied='solid', bd=1, text='버거')
# frame_bugger.pack(sid='left', fill='both', expand=True)
# Button(frame_bugger, text='햄버거').pack()

# frame = Frame(root)
# frame.pack()

# Scrollbar = Scrollbar(frame)
# Scrollbar.pack(side='right', fill='y')

# listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand = Scrollbar.set)
# for i in range(1, 32):
#     listbox.insert(END, str(i)+'일')
# listbox.pack(side='left')

# Scrollbar.config(command=listbox.yview)

# btn.grid(row=0, column=0, sticky=N+E+W+S)

# root.mainloop()