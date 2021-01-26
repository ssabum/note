import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('ssabum GUI')

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x')

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text='파일추가')
btn_add_file.pack(side='left')

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text='선택삭제')
btn_del_file.pack(side='right')

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both')

# 스크롤 바
Scrollbar = Scrollbar(list_frame)
Scrollbar.pack(side='right', fill='y')

# 리스트 파일 프레임, 스크롤 바 매핑
list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=Scrollbar.set)
list_file.pack(sid='left', fill='both', expand=True)
Scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text='저장경로')
path_frame.pack(fill='x')

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(sid='left', fill='x', expand=True, ipady=4)

bnt_dest_path = Button(path_frame, text='찾아보기', width=10)
bnt_dest_path.pack(side='right')

# 옵션 프레임
frame_option = LabelFrame(root, text='옵션')
frame_option.pack()

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text='가로넓이', width=8)
lbl_width.pack(side='left')

# 가로 넓이 콤보
opt_width = ['원본유지', '1024', '800', '640']
cmb_width = ttk.Combobox(frame_option, state='readonly', values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side='left')

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text='간격', width=8)
lbl_space.pack(side='left')

# 간격 옵션 콤보
opt_space = ['없음', '좁게', '보통', '넓게']
cmb_space = ttk.Combobox(frame_option, state='readonly', values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side='left')

# 3. 포맷 옵션
# 포맷 옵션 레이블
lbl_format = Label(frame_option, text='포맷', width=8)
lbl_format.pack(side='left')

# 포맷 옵션 콤보
opt_format = ['PNG', 'JPG', 'BMP']
cmb_format = ttk.Combobox(frame_option, state='readonly', values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side='left')

# 진행 상황 progress bar
frame_progress = LabelFrame(root, text='진행상황')
frame_progress.pack()

progrss_bar = ttk.Progressbar(frame_progress, maxi)

root.resizable(False, False)
root.mainloop()