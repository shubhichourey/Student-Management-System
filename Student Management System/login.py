from tkinter import * #use for graphical user interface
from tkinter import messagebox #show a box on dispaly
from PIL import ImageTk #python image library , dowload pillow from command prompt(only for jpg images)

def login():
     if entry.get()=='' or pentry.get()=='':
       messagebox.showerror('Error','Feilds cannot be empty')   
     elif  entry.get()=="Shubhi"  and pentry.get()=='1234':
         messagebox.showinfo('Sucess','Welcome')
         window.destroy() 
         import sms
         
     else:
         messagebox.showerror('Error','Please enter correct details')
    
           

window=Tk()
window.geometry('1528x782+0+0') # giving width and height to window using geometry method
#0: 0 dist form x and y axis , always start at top left corner
window.title('Login System of Student Management System')

window.resizable(False,False) #window size fixed 

bg=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window,image=bg)#label method in tk to show bg
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='#e1c290')
loginFrame.place(x=900,y=250 )

logoimage=PhotoImage(file='profile_logo.png')
logolabel=Label(loginFrame,image=logoimage,border=0)
logolabel.grid(row=0,columnspan=2,pady=10)

userImage=PhotoImage(file='user.png')
username=Label(loginFrame,image=userImage,text="Username",compound=LEFT,font=('times new roman',20,'bold'),bg='#E2C492')
username.grid(row=1,column=0,pady=10,padx=2)

entry=Entry(loginFrame,font=('calibri',20),bd=5)
entry.grid(row=1,column=1,pady=10,padx=10)

passwordImage=PhotoImage(file='key.png')
password=Label(loginFrame,image=passwordImage,text="Password",compound=LEFT,font=('times new roman',20,'bold'),bg='#E2C492')
password.grid(row=2,column=0,pady=10,padx=2)

pentry=Entry(loginFrame,font=('calibri',20),bd=5)
pentry.grid(row=2,column=1,pady=10,padx=10)

loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15,fg='white',bg='cornflowerblue',activeforeground='white',activebackground="cornflowerblue",cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)


window.mainloop() #keep window on loop



