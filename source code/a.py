import tkinter as tk
from tkinter import ttk
from tkinter import font ,colorchooser,filedialog,messagebox
import os,shutil

win=tk.Tk()
win.geometry("1200x800")
win.title("Text Editor")
win.wm_iconbitmap('icon.ico')


mainmenu=tk.Menu()

win.configure(menu=mainmenu)

file=tk.Menu(mainmenu,tearoff=False)
edit=tk.Menu(mainmenu,tearoff=False)
view=tk.Menu(mainmenu,tearoff=False)
colorthem=tk.Menu(mainmenu,tearoff=False)
them_choice=tk.StringVar()
color_dict={
    "Ligt":("#000000","#ffffff"),
    "Dark":("#c4c4c4","#2d2d2d"),
    "Light Plus":("#474747","#e0e0e0"),
    "Red":("#2d2d2d","#ffe8e8"),
    "Monokai":("#d3b774","#474747"),
    "Night Blue":("#ededed","#6b9dc2"),
}
count=0
mainmenu.add_cascade(label="File",menu=file)
mainmenu.add_cascade(label="Edit",menu=edit)
mainmenu.add_cascade(label="View",menu=view)
mainmenu.add_cascade(label="Colorthem",menu=colorthem)


#tool bar
tool_bar=ttk.Label(win)
#tool_bar.configure(background='black')
tool_bar.pack(side=tk.TOP,fill=tk.X)

fonts=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,textvariable=font_family,state="readonly")
font_box['values']=fonts
font_box.current(fonts.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#size box
size_var=tk.StringVar()
size_box=ttk.Combobox(tool_bar,textvariable=size_var,state="readonly")
size_box["values"]=tuple(range(0,101,2))
size_box.current((5))
size_box.grid(row=0,column=1,padx=5)

bold_icon=tk.PhotoImage(file=r"./Icons/bold.png")
italic_icon=tk.PhotoImage(file=r"./Icons/italic.png")
underline_icon=tk.PhotoImage(file=r"./Icons/underline.png")
font_color_icon=tk.PhotoImage(file=r"./Icons/font_color.png")
align_center_icon=tk.PhotoImage(file=r"./Icons/align_center.png")
align_right_icon=tk.PhotoImage(file=r"./Icons/align_right.png")
align_left_icon=tk.PhotoImage(file=r"./Icons/align_left.png")
#bts
bold_btn=tk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

italic_btn=tk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)


underline_btn=tk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=10,padx=5)

font_btn=tk.Button(tool_bar,image=font_color_icon)
font_btn.grid(row=0,column=5,padx=5)

agl_btn=tk.Button(tool_bar,image=align_left_icon)
agl_btn.grid(row=0,column=6,padx=5)

agc_btn=tk.Button(tool_bar,image=align_center_icon)
agc_btn.grid(row=0,column=7,padx=5)

agr_btn=tk.Button(tool_bar,image=align_right_icon)
agr_btn.grid(row=0,column=8,padx=5)

text_editor=tk.Text(win)
text_editor.config(wrap="word",relief=tk.FLAT)


scroll_bar=tk.Scrollbar(win)
text_editor .focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
#font  family
current_font_family='Arial'
current_font_size=10

def change_font(even=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))


def change_fontsize(events=None):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
size_box.bind("<<ComboboxSelected>>",change_fontsize)

#bold buttons

def bold():
    text_porperty=tk.font.Font(font=text_editor['font'])
    if text_porperty.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_porperty.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

def italic():
    text_porperty=tk.font.Font(font=text_editor['font'])
    if text_porperty.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_porperty.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

def underline():
    text_porperty=tk.font.Font(font=text_editor['font'])
    if text_porperty.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_porperty.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))

#font colour
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

#alige

#left
def alige_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"left")
agl_btn.configure(command=alige_left)

def alige_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"center")

agc_btn.configure(command=alige_center)

def alige_righ():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"right")
agr_btn.configure(command=alige_righ)

font_btn.configure(command=change_font_color)
underline_btn.configure(command=underline)
bold_btn.configure(command=bold)
italic_btn.configure(command=italic)



text_editor.configure(font=("Arial",10))


status_bar=ttk.Label(win,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def count_cha(even=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,"end-1c").split())
        character=len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bar.configure(text=f"Character : {character} Words : {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",count_cha)

url=''

def new_file(even=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)



def open_files(even=None):
    global url 
    url=filedialog.askopenfilenames(initialdir=os.getcwd(),title="Select Files",filetype=(("Text File","*.txt"),("All Files","*.*")))
    try:
        with open(url[0],"r") as rf:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,rf.read())
    except FileNotFoundError:
        return 
    except :
        return
    win.title(os.path.basename(url[0]))



new_icon=tk.PhotoImage(file=r"./Icons/new.png")
open_icon=tk.PhotoImage(file=r"./Icons/open.png")
save_icon=tk.PhotoImage(file=r"./Icons/save.png")
save_as_icon=tk.PhotoImage(file=r"./Icons/save_as.png")
exit_icon=tk.PhotoImage(file=r"./Icons/exit.png")
copy_icon=tk.PhotoImage(file=r"./Icons/copy.png")
paste_icon=tk.PhotoImage(file=r"./Icons/paste.png")
cut_icon=tk.PhotoImage(file=r"./Icons/cut.png")
clear_icon=tk.PhotoImage(file=r"./Icons/clear_all.png")
find_icon=tk.PhotoImage(file=r"./Icons/find.png")
tool_bar_icon=tk.PhotoImage(file=r"./Icons/tool_bar.png")
status_bar_icon=tk.PhotoImage(file=r"./Icons/status_bar.png")

dark_icon=tk.PhotoImage(file=r"./Icons/dark.png")
red_icon=tk.PhotoImage(file=r"./Icons/red.png")
light_default_icon=tk.PhotoImage(file=r"./Icons/light_default.png")
night_blue_icon=tk.PhotoImage(file=r"./Icons/night_blue.png")
monokai_icon=tk.PhotoImage(file=r"./Icons/monokai.png")
light_plus_icon=tk.PhotoImage(file=r"./Icons/light_plus.png")

color_icons=(light_default_icon,dark_icon,light_plus_icon,red_icon,monokai_icon,night_blue_icon)
#file comands
def save_file(even=None):
    global url
    try:
        if url:
            print(url[0])
            content=str(text_editor.get(1.0,tk.END))
            print(content)
            with open(url[0],"w",encoding="utf-8") as wf:
                wf.write(content)
            
        else:
            url=filedialog.asksaveasfile(mode="w",defaultextension='.txt',filetype=(("Text File","*.txt"),("All Files","*.*")))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

def save_as(events=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode="w",defaultextension='.txt',filetype=(("Text File","*.txt"),("All Files","*.*")))
        url.write(content)
        url.close()
    except:
        return
def exit(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel("W A R N I N G !","Do You Want To Save File ?")
            if mbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url[0],"w",encoding="utf-8") as wf:
                        wf.write(content)
                        win.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode="w",defaultextension='.txt',filetype=(("Text File","*.txt"),("All Files","*.*")))
                    url.write(content2)
                    url.closed()
                    win.destroy()
            elif mbox is False:
                win.destroy()
        else:
            win.destroy()
    except:
        return

def find(even=None):

    def find():
        word=find_label_entry.get()
        text_editor.tag_remove('match','1.0',tk.END)
        match=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add('match',start_pos,end_pos)
                match+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
                match_founds.configure(text=f"Match Found : {match}")
        
    def replace():
        word=find_label_entry.get()
        replace_word=replace_label_entry.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_word)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)





    find_dialog=tk.Toplevel()
    find_dialog.geometry("500x250+500+200")
    find_dialog.title("Find or Replace")
    find_dialog.resizable(0,0)

    find_frame=ttk.LabelFrame(find_dialog)
    find_frame.pack(pady=20)

    find_label=ttk.Label(find_frame,text="Find")
    replace_label=ttk.Label(find_frame,text="Replace")
    find_label_entry=ttk.Entry(find_frame,width=30)
    replace_label_entry=ttk.Entry(find_frame,width=30)

    find_btn=ttk.Button(find_frame,text="Find",command=find)
    replace_btn=ttk.Button(find_frame,text="Replace",command=replace)

    find_label.grid(row=0,column=0,pady=10,padx=10)
    replace_label.grid(row=1,column=0,pady=10,padx=10)
    find_label_entry.grid(row=0,column=1)
    replace_label_entry.grid(row=1,column=1)

    find_btn.grid(row=10,column=0,pady=30,padx=30)
    replace_btn.grid(row=10,column=2,pady=30,padx=30)

    match_founds=ttk.Label(find_frame,text="Match Found / Words Relpaced")
    match_founds.grid(row=12,column=1)

    find_dialog.mainloop()

file.add_command(label="New",image=new_icon,accelerator="Ctrl+N",compound=tk.LEFT,command=new_file)
file.add_command(label="Open",image=open_icon,accelerator="Ctrl+O",compound=tk.LEFT,command=open_files)
file.add_separator()
file.add_command(label="Save",image=save_icon,accelerator="Ctrl+S",compound=tk.LEFT,command=save_file)
file.add_command(label="Save as",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+Shift+S",command=save_as)
file.add_separator()
file.add_command(label="Exit",image=exit_icon,accelerator="Ctrl+Q",compound=tk.LEFT,command=exit)
#edit comands
edit.add_command(label="Copy",image=copy_icon,accelerator="Ctrl+C",compound=tk.LEFT,command=lambda : text_editor.event_generate("<Control c>"))
edit.add_command(label="Cut",image=cut_icon,accelerator="Ctrl+X",compound=tk.LEFT,command=lambda : text_editor.event_generate("<Control x>"))
edit.add_command(label="Paste",image=paste_icon,accelerator="Ctrl+V",compound=tk.LEFT,command=lambda : text_editor.event_generate("<Control v>"))
edit.add_separator()
edit.add_command(label="Clear all",image=clear_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+X",command=lambda :text_editor.delete(1.0,tk.END))
edit.add_command(label="Find or Replace",image=find_icon,accelerator="Ctrl+F",compound=tk.LEFT,command=find)
#view comands
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar(event=None):
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True


def hide_statusbar(event=None):
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True


view.add_checkbutton(label="Tool Bar",onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label="Satus Bar",onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)
#color_them
def change_them():
    chose_them=them_choice.get()
    color_tuple=color_dict.get(chose_them)
    fg,bg=color_tuple[0],color_tuple[1]
    text_editor.config(foreground=fg,background=bg)
    

for i in color_dict:
    colorthem.add_radiobutton(label=i,image=color_icons[count],variable=them_choice,compound=tk.LEFT,command=change_them)
    count+=1

win.bind("<Control-n>",new_file)
win.bind("<Control-o>",open_files)
win.bind("<Control-s>",save_file)
win.bind("<Control-Alt-s>",save_as)
win.bind("<Control-q>",exit)
win.bind("<Control-f>",find)



win.mainloop()