from tkinter import *
import os
from tkinter import filedialog
import tkinter.messagebox



class All:
    def __init__(self,master):
     
        self.ab = master
        self.li = []
        self.checkboxes = []
        self.checkVariables = []
        self.user = ""
        self.user_pass = ""
        self.menubar = Menu(master)
        master.config(menu=self.menubar)
        self.menu_s = Menu(self.menubar)
        self.menubar.add_cascade(label="Entry", menu=self.menu_s)        
        self.menu_s.add_command(label="SignUp",command=self.register)
        self.menu_s.add_separator()       
        self.menu_s.add_command(label="Login",command=self.login)
        self.menu_s.add_separator() 
        self.menu_s.add_command(label="Log out",command=self.logout)
        self.menubar.add_cascade(label="Close",command = master.destroy)
        
        self.browse = PhotoImage(file="browse.png")
        self.lock = PhotoImage(file="encrypt.png")
        self.unlock = PhotoImage(file="decrypt.png")
        self.toolbar = Frame(master)
        self.br_btn = Button(self.toolbar,image=self.browse,text="Choose File",font="Helvetica 14 bold",compound=TOP,command=self.fileBrowsing)
        self.lock_btn = Button(self.toolbar,image=self.lock,text="Encrypt",font="Helvetica 14 bold",compound=TOP,command=self.encrypt)
        self.unlock_btn = Button(self.toolbar,image=self.unlock,text="Decrypt",font="Helvetica 14 bold",compound=TOP,command=self.decrypt)
        self.br_btn.pack(side=TOP,padx=30,fill=X)
        self.lock_btn.pack(side=TOP,padx=30,fill=X)
        self.unlock_btn.pack(side=TOP,padx=30,fill=X)
        self.toolbar.pack(side=TOP,fill=X)
        label = Label(master,height = 5,text="Encrypted File List: ",font="Helvetica 18 bold")
        label.pack()
        self.new = Frame(master,height=100)
        self.new.pack(side="bottom")
        
        self.menu_s.entryconfig(5,state=DISABLED)
        self.br_btn.configure(state=DISABLED)
        self.lock_btn.configure(state=DISABLED)
        self.unlock_btn.configure(state=DISABLED)
        
        
    def fileBrowsing(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Choose a File",filetype=(("jpeg","*.jpg"),("All Files","*.*")))
        self.lock_btn.configure(state=NORMAL)
        
    def encrypt(self):
        self.com1 = 'encrypt "' + self.filename + '" ' + self.user
        os.system(self.com1)
        self.lock_btn.configure(state=DISABLED)
        self.unlock_btn.configure(state=NORMAL)
        f = open("fileList.txt","a+")
        line = ''+self.user + ' "'+ self.filename + '"\n'
        f.write(line)
        f.close()
        for i in self.checkboxes:
            i.destroy()
        self.checkboxes.clear()
        self.li.clear()
        self.updateList()
        
    def decrypt(self):
        count = 0
        self.file_to_be_decrypted = ''
        for i in self.checkVariables:
            if i.get() == 1:
                count = count+1
        if count==0:
            tkinter.messagebox.showinfo("No File Selected         ")
        elif count >1:
            tkinter.messagebox.showinfo("Only one file should be selected at a time.        ")
        else:
            for i in range(len(self.checkVariables)):
                if self.checkVariables[i].get():
                    self.file_to_be_decrypted = self.checkboxes[i].cget("text")
                    #print(self.file_to_be_decrypted,"ab")
                    self.com2 = 'decrypt' + self.file_to_be_decrypted + ' ' + self.user
                    self.afterDecrypt()
                    #print(self.com2)
                    os.system(self.com2)

        
    def key_gen(self):
        os.system("key_generate")
        
    def register(self):
        global reg_screen
        reg_screen = Toplevel(self.ab)
        reg_screen.title("Sign Up")
        reg_screen.geometry("300x100")
        self.username = StringVar()
        self.password = StringVar()
        self.confirm_pass = StringVar()
        Label(reg_screen,text="Username :").grid(row=0,sticky=E)
        Label(reg_screen,text="Password :").grid(row=1,sticky=E)
        Label(reg_screen,text="Confirm Password :").grid(row=2)
        self.name_entry = Entry(reg_screen,textvariable=self.username).grid(row=0,column=1)   
        self.pass_entry = Entry(reg_screen,textvariable=self.password).grid(row=1,column=1)
        self.conf_pass_entry = Entry(reg_screen,textvariable=self.confirm_pass).grid(row=2,column=1)
        Button(reg_screen,text="Submit",width=10, height=1,bg="white",command=self.register_user).grid(row=4,columnspan=10)
        
    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        confirm_info = self.confirm_pass.get()
        if (password_info == confirm_info) and (password_info != "") and (username_info != ""):
            reg_screen.destroy()
            f = open("keys.txt","a+")
            f.write(username_info+' '+password_info+' ')
            f.close()
            self.key_gen()
            tkinter.messagebox.showinfo("Confirmation","Registration Completed Successfully.")
            self.user = username_info
            self.user_pass = password_info
            self.menu_s.entryconfig(5,state=NORMAL)
            self.menu_s.entryconfig(1,state=DISABLED)
            self.menu_s.entryconfig(3,state=DISABLED)
            self.br_btn.configure(state=NORMAL)
            self.unlock_btn.configure(state=DISABLED)
            self.updateList()
            
            if li:
                self.unlock_btn.configure(state=NORMAL)
            
        else:
            tkinter.messagebox.showinfo("Error","Error !!!!!!")
            
    def login(self):
        global login_screen
        login_screen = Toplevel(self.ab)
        login_screen.title("Log in")
        login_screen.geometry("300x100")
        self.username_verify = StringVar()
        self.password_verify = StringVar()
        Label(login_screen,text="Username :").grid(row=0,sticky=E)
        Label(login_screen,text="Password :").grid(row=1,sticky=E)
        self.name_entry_verify = Entry(login_screen,textvariable=self.username_verify).grid(row=0,column=1)   
        self.pass_entry_verify = Entry(login_screen,textvariable=self.password_verify).grid(row=1,column=1)
        Button(login_screen,text="Log in",width=10, height=1,bg="white",command=self.login_user).grid(row=4,columnspan=2)
        
    def login_user(self):
        username_info_v = self.username_verify.get()
        password_info_v = self.password_verify.get()
        f = open("keys.txt","r")
        while (1):
            content = f.readline()
            if content=="":
                tkinter.messagebox.showinfo("Log in","Log in Error !!!!!!")
                break
            li = content.split()
            if li[0]==username_info_v and li[1]==password_info_v:
                tkinter.messagebox.showinfo("Login","Successfully Logged in ... ")
                self.user = username_info_v
                self.user_pass = password_info_v
                login_screen.destroy()
                self.menu_s.entryconfig(5,state=NORMAL)
                self.menu_s.entryconfig(1,state=DISABLED)
                self.menu_s.entryconfig(3,state=DISABLED)
                self.br_btn.configure(state=NORMAL)
                self.updateList()
                
                if li:
                    self.unlock_btn.configure(state=NORMAL)
                break
    def logout(self):
        self.menu_s.entryconfig(5,state=DISABLED)
        self.menu_s.entryconfig(1,state=NORMAL)
        self.menu_s.entryconfig(3,state=NORMAL)
        for i in self.checkboxes:
            i.destroy()
        self.li.clear()
        self.br_btn.configure(state=DISABLED)
        self.unlock_btn.configure(state=DISABLED)
    
    def updateList(self):
        self.li = []
        self.checkboxes = []
        self.checkVariables = []
        f = open("fileList.txt","r")
        lines = f.readlines()
        st = ''
        for line in lines:
            thisline = line.split()
            if self.user == thisline[0]:
                for i in range(1,len(thisline)):
                    st = st + " " + thisline[i]
                self.li.append(st)
                st = ''
        self.checkVariables = [0] * len(self.li)
        for i in range(len(self.li)):
            var = IntVar()
            self.checkboxes.append(Checkbutton(self.ab,text=self.li[i],variable=var))
            self.checkVariables[i] = var
            self.checkboxes[i].pack()
        f.close()
        
    def afterDecrypt(self):
        f = open("fileList.txt","r")
        lines = f.readlines()
        str1=''
        self.the_line=''
        for line in lines:
            thisline = line.split()
            if self.user==thisline[0]:
                for i in range(1,len(thisline)):
                    str1 = str1+" "+thisline[i]
                if str1==self.file_to_be_decrypted:
                    #print("got it")
                    self.the_line = line
                    break;
        f.close()
        with open("fileList.txt","w") as f:
            for line in lines:
                if line != self.the_line:
                    f.write(line)
        f.close()
        for i in self.checkboxes:
            i.destroy()
        self.updateList()
        
        
        

root = Tk()
root.minsize(width=800,height=400)
b = All(root)

root.mainloop()



