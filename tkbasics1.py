import tkinter as tk
from tkinter import messagebox
class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        #menubar in tinkter 
        
        self.menubar = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menubar, tearoff = 0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close with out asking ", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff = 0)
        self.actionmenu.add_command(label="Print Task", command=self.show_message)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="View")
        
        self.root.config(menu=self.menubar)
        
        self.root.title("To do list")
        self.label = tk.Label(self.root, text="Your tasks", font = ('Arial',18))
        self.label.pack(padx=10,pady=10)
        
        self.textbox = tk.Text(self.root, font=('Arial',18))
        self.textbox.pack(padx=10,pady=10)
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="show messagebox", font=('Arial',16),variable=self.check_state)
        self.check.pack(padx=10,pady=10)
        
        self.button = tk.Button(self.root, text="Show Message", font=('Arial',18),command=self.show_message)
        self.button.pack(padx=10,pady=10)
        
        self.clearbtn = tk.Button(self.root, text="Clear tasks", font=('Arial',18),command=self.clear)
        self.clearbtn.pack(padx=10,pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.root.mainloop()
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(title="Message Box",message=self.textbox.get('1.0',tk.END))
    def on_closing(self):
        if messagebox.askyesno(title="Quit",message="Wanna Quit?"):
            print("Program closed")
            self.root.destroy()
    
    def clear(self):
        self.textbox.delete('1.0',tk.END)

MyGUI()
        