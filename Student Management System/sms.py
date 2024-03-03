from tkinter import *
import time 
import ttkthemes 
from tkinter import ttk,messagebox,filedialog
import pymysql  
import pandas # convert datalist into tabular form

def iexit():
   result=messagebox.askyesno('Confirm','Do you want to exit?')
   if result:
      root.destroy()
   else:
      pass


def export_data():
   url=filedialog.asksaveasfilename(defaultextension='.csv')
   indexing=studenttable.get_children()
   newlist=[]
   for index in indexing:
      content=studenttable.item(index)
      datalist=content['values']
      newlist.append(datalist)

   table=pandas.DataFrame(newlist,columns=['Id','Fist Name','Last Name','Phone No','Email','Address','Gender','D.O.B','Added Date','Added Time'])
   table.to_csv(url,index=FALSE) #FALSE: will not see the index in file
   messagebox.showinfo('Success','Data is saved successfully')


def toplevel_data(title,button_text,command):
   global identry,firstnameentry,lastnameentry,phoneentry,emailentry,addressentry,genderentry,dobentry,screen

   screen=Toplevel()
   screen.title(title)
   screen.grab_set()
   screen.resizable(0,0)
   idlabel=Label(screen,text='Id',font=('times new roman',20,'bold'))
   idlabel.grid(row=0,column=0,padx=20,pady=15,sticky=W)
   identry=Entry(screen,font=('times new roman',15,'bold'),width=24)
   identry.grid(row=0,column=1,padx=10,pady=15)

   firstnamelabel=Label(screen,text='First Name',font=('times new roman',20,'bold'))
   firstnamelabel.grid(row=1,column=0,padx=20,pady=15,sticky=W)
   firstnameentry=Entry(screen,font=('times new roman',15,'bold'),width=24)
   firstnameentry.grid(row=1,column=1,padx=10,pady=15)

   lastnamelabel=Label(screen,text='Last Name',font=('times new roman',20,'bold'))
   lastnamelabel.grid(row=2,column=0,padx=20,pady=15,sticky=W)
   lastnameentry=Entry(screen,font=('times new roman',15,'bold'),width=24)
   lastnameentry.grid(row=2,column=1,padx=10,pady=15)

   phonelabel=Label(screen,text='PhoneNo',font=('times new roman',20,'bold'))
   phonelabel.grid(row=3,column=0,padx=20,pady=15,sticky=W)
   phoneentry=Entry(screen,font=('times new roman',15,'bold'),width=24)
   phoneentry.grid(row=3,column=1,padx=10,pady=15)

   emaillabel=Label(screen,text='Email',font=('times new roman',20,'bold'))
   emaillabel.grid(row=4,column=0,padx=20,pady=15,sticky=W)
   emailentry=Entry(screen,font=('times new roman',15,'bold'),width=24)
   emailentry.grid(row=4,column=1,padx=10,pady=15)

   addresslabel=Label(screen,text='Address',font=('times new roman',20,'bold'))
   addresslabel.grid(row=5,column=0,padx=20,pady=15,sticky=W)
   addressentry=Entry(screen,font=('times new roman',15,'bold'),width=24)
   addressentry.grid(row=5,column=1,padx=10,pady=15)

   genderlabel=Label(screen,text='Gender',font=('times new roman',20,'bold'))
   genderlabel.grid(row=6,column=0,padx=20,pady=15,sticky=W)
   genderentry=Entry(screen,font=('times new roman',15,'bold'),width=24)
   genderentry.grid(row=6,column=1,padx=10,pady=15)

   doblabel=Label(screen,text='D.O.B',font=('times new roman',20,'bold'))
   doblabel.grid(row=7,column=0,padx=20,pady=15,sticky=W)
   dobentry=Entry(screen,font=('times new roman',15,'bold'),width=24)
   dobentry.grid(row=7,column=1,padx=10,pady=15)

   student_button=ttk.Button(screen,text=button_text,command=command)
   student_button.grid(row=8,columnspan=2,pady=15)
   
   if title=='Update Student':
     index=studenttable.focus()
     content=studenttable.item(index)
     
     listdata=content['values']
     identry.insert(0,listdata[0])
     firstnameentry.insert(0,listdata[1])
     lastnameentry.insert(0,listdata[2])
     phoneentry.insert(0,listdata[3])
     emailentry.insert(0,listdata[4])
     addressentry.insert(0,listdata[5])
     genderentry.insert(0,listdata[6])
     dobentry.insert(0,listdata[7])


def update_data():
   query='update student set firstname=%s , lastname=%s , mobileno=%s , email=%s , address=%s , gender=%s , dob=%s , date=%s , time=%s where id=%s'
   mycursor.execute(query,(firstnameentry.get(),lastnameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),genderentry.get(),dobentry.get(),date,currenttime,identry.get()))
   con.commit()
   messagebox.showinfo('Success',' Data updated successfully',parent=screen)
   screen.destroy()
   show_student()

   
   

def show_student():
   query='select * from student'
   mycursor.execute(query)
   studenttable.delete(* studenttable.get_children())
   fetched_data=mycursor.fetchall()
   for data in fetched_data:
      studenttable.insert('',END,values=data)

def delete_student():
   index=studenttable.focus() # whichever row wil be selected will store in the index
   print(index)
   content=studenttable.item(index)
   content_id=content['values'][0] # content value will give the value of all the rows in dict and '0' taking the index of dict which is present at 0th index
   query='delete from student where id=%s'
   mycursor.execute(query,content_id)
   con.commit()
   messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
   query='select * from student'
   mycursor.execute(query)
   fetched_data=mycursor.fetchall()
   studenttable.delete(*studenttable.get_children()) 
   for data in fetched_data: # data will have all data in tuple 
      studenttable.insert('',END,values=data)



def search_data():
   query='select * from student where id=%s or firstname=%s or lastname=%s or mobileno=%s or email=%s or address=%s or gender=%s or dob=%s'
   mycursor.execute(query,(identry.get(),firstnameentry.get(),lastnameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),genderentry.get(),dobentry.get())) 
   studenttable.delete(*studenttable.get_children())
   fetched_data=mycursor.fetchall()
   for data in fetched_data:
      studenttable.insert('',END,values=data)
      

def add_data():
   if identry.get()=='' or firstnameentry.get()=='' or lastnameentry.get()=='' or phoneentry.get()=='' or emailentry.get()=='' or addressentry.get()=='' or genderentry.get()=='' or dobentry.get()=='':
     messagebox.showerror('Error','All Feilds are required',parent=screen)
   else:
     currentdate=time.strftime('%d/%m/%Y')
     currenttime=time.strftime('%H:%M:%S')
     try:
       query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
       mycursor.execute(query,(identry.get(),firstnameentry.get(),lastnameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),genderentry.get(),dobentry.get(),currentdate,currenttime))
       con.commit()
       result=messagebox.askyesno('Confirm','Data added successfully.Do you want to clear the form ?',parent=screen)
       if result:
          identry.delete(0,END)
          firstnameentry.delete(0,END)
          lastnameentry.delete(0,END)
          phoneentry.delete(0,END)
          emailentry.delete(0,END)
          addressentry.delete(0,END)
          genderentry.delete(0,END)
          dobentry.delete(0,END)
       else:
          pass
     except:
        messagebox.showerror('Error','Id cannot be repeated',parent=screen)
        return
        
   query='select * from student'
   mycursor.execute(query)
   fetched_data=mycursor.fetchall()
   studenttable.delete(* studenttable.get_children()) #deleting the previous data s it does not repeat when new data is being added
   print(fetched_data)
   for data in fetched_data:
      studenttable.insert('',END,values=data)
    



def connect_database():
    def connect():
        global mycursor,con
        try:
          con=pymysql.connect(host='localhost',user='root',password='shubhii010')
          mycursor=con.cursor()
          
        except:
          messagebox.showerror('Error','Invalid Details',parent=connectwindow) 
          return 

        try:
          query='create database studentmanagementsystem'
          mycursor.execute(query)
          query='use studentmanagementsystem'
          mycursor.execute(query)
          query="create table student(id int not null primary key, firstname varchar(10), lastname varchar(10), mobileno varchar(10) , email varchar(20), address varchar(30), gender varchar(10), dob varchar(20), date varchar(20), time varchar(20))"
          mycursor.execute(query)
        except:
           query='use studentmanagementsystem'
           mycursor.execute(query)

        messagebox.showinfo('Success','Database Connection is Successful',parent=connectwindow)
        connectwindow.destroy()
        addstudent.config(state=NORMAL)
        searchstudent.config(state=NORMAL)
        updatestudent.config(state=NORMAL)
        showstudent.config(state=NORMAL)
        exportstudent.config(state=NORMAL)
        deletestudent.config(state=NORMAL)
        


    connectwindow=Toplevel()
    connectwindow.grab_set() #if we click on somewhere else the window will not minimize, therefore first we need to click canacle then only go back
    connectwindow.geometry('470x250+530+230')
    connectwindow.title('connect to database')
    connectwindow.resizable(0,0)

    hostname=Label(connectwindow,text='Host Name:',font=('arial',20,'bold'))
    hostname.grid(row=0,column=0,padx=20)

    hostentry=Entry(connectwindow,font=('calibri',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=20,pady=20)

    username=Label(connectwindow,text='User Name:',font=('arial',20,'bold'))
    username.grid(row=1,column=0,padx=20)

    userentry=Entry(connectwindow,font=('calibri',15,'bold'),bd=2)
    userentry.grid(row=1,column=1,padx=20,pady=20)

    password=Label(connectwindow,text='Password:',font=('arial',20,'bold'))
    password.grid(row=2,column=0,padx=20)

    passentry=Entry(connectwindow,font=('calibri',15,'bold'),bd=2)
    passentry.grid(row=2,column=1,padx=20,pady=20)

    cbutton=ttk.Button(connectwindow,text='CONNECT',command=connect)
    cbutton.grid(row=3,columnspan=2)

def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    dt.config(text=f'    Date:{date}\n Time:{currenttime}')
    dt.after(1000,clock)

count=0
text='' 
def sliderg():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count] #word display one by one
    slider.config(text=text)
    count+=1
    slider.after(300,sliderg)
    

root=ttkthemes.ThemedTk ()
root.get_themes()
root.set_theme('black')

root.geometry('1528x782+0+0')
root.resizable(0,0)
root.title('Database of Student Management System ')

dt=Label(root,text='hello',font=('times new roman',18,'bold'))
dt.place(x=5,y=5)
clock()

s='Student Management System'
slider=Label(root,font=('arial',28,'italic bold'),width=30)
slider.place(x=400,y=0)
sliderg()

connectbutton=ttk.Button(root,text='Connect Button',width=20,padding=8,style='connect.TButton',command=connect_database)
connectbutton.place(x=1300,y=0)

style = ttk.Style()
h= ttk.Button(root, style="connect.TButton")
style.configure('connect.TButton', font=(None,10,'bold'))

leftframe=Frame(root,bg='orange')
leftframe.place(x=50,y=80,width=300,height=672)

logo_image=PhotoImage(file='graduates.png')
logolabel=Label(leftframe,image=logo_image)
logolabel.grid(row=0,column=0,padx=(50,10),pady=(20,10))

addstudent=ttk.Button(leftframe,text='Add Student',width=25,padding=10,style='a.TButton',state=DISABLED,command=lambda: toplevel_data('Add Student','Add Student',add_data))
addstudent.grid(row=1,column=0,pady=20,padx=(50,10))

searchstudent=ttk.Button(leftframe,text='Search Student',width=25,padding=10,style='b.TButton',state=DISABLED,command=lambda: toplevel_data('Search Student','Search',search_data))
searchstudent.grid(row=2,column=0,pady=20,padx=(50,10))

deletestudent=ttk.Button(leftframe,text='Delete Student',width=25,padding=10,style='c.TButton',state=DISABLED,command=delete_student)
deletestudent.grid(row=3,column=0,pady=20,padx=(50,10))

updatestudent=ttk.Button(leftframe,text='Update Student',width=25,padding=10,style='d.TButton',state=DISABLED,command=lambda: toplevel_data('Update Student','Update',update_data))
updatestudent.grid(row=4,column=0,pady=20,padx=(50,10))

showstudent=ttk.Button(leftframe,text='Show Student',width=25,padding=10,style='e.TButton',state=DISABLED,command=show_student)
showstudent.grid(row=5,column=0,pady=20,padx=(50,10))

exportstudent=ttk.Button(leftframe,text='Export Data',width=25,padding=10,style='f.TButton',state=DISABLED,command=export_data)
exportstudent.grid(row=6,column=0,pady=20,padx=(50,10))

exit=ttk.Button(leftframe,text='Exit',width=25,padding=10,style='g.TButton',command=iexit)
exit.grid(row=7,column=0,pady=20,padx=(50,10))

style = ttk.Style()
a = ttk.Button(leftframe, style="a.TButton")
style.configure('a.TButton', font=(NONE, 10,'bold'))

b= ttk.Button(leftframe,style="b.TButton")
style.configure('b.TButton', font=(None, 10,'bold'))

c= ttk.Button(leftframe,style="c.TButton")
style.configure('c.TButton', font=(None, 10,'bold'))

d= ttk.Button(leftframe,style="d.TButton")
style.configure('d.TButton', font=(None, 10,'bold'))

e= ttk.Button(leftframe,style="e.TButton")
style.configure('e.TButton', font=(None, 10,'bold'))

f= ttk.Button(leftframe,style="f.TButton")
style.configure('f.TButton', font=(None, 10,'bold'))

g= ttk.Button(leftframe,style="g.TButton")
style.configure('g.TButton', font=(None, 10,'bold'))




rightframe=Frame(root)
rightframe.place(x=350,y=80,width=1150,height=690)

scrollX=Scrollbar(rightframe,orient=HORIZONTAL)
scrollY=Scrollbar(rightframe,orient=VERTICAL)

studenttable=ttk.Treeview(rightframe,columns=('Id','FirstName','LastName','MobileNo','Email','Address','Gender','D.O.B','Added Date','Added Time')
                          ,xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

style = ttk.Style()
style.configure("Treeview.Heading", font=(None,15))

scrollX.config(command=studenttable.xview)
scrollY.config(command=studenttable.yview)

scrollX.pack(side=BOTTOM,fill=X)
scrollY.pack(side=RIGHT,fill=Y)
studenttable.pack(fill=BOTH,expand=1)

studenttable.heading('Id',text='Id')
studenttable.heading('FirstName',text='First Name')
studenttable.heading('LastName',text='Last Name')
studenttable.heading('MobileNo',text='Mobile Number')
studenttable.heading('Email',text='Email Id')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')

studenttable.column('Id',width=50,anchor=CENTER)
studenttable.column('FirstName',width=300,anchor=CENTER)
studenttable.column('LastName',width=300,anchor=CENTER)
studenttable.column('MobileNo',width=300,anchor=CENTER)
studenttable.column('Email',width=300,anchor=CENTER)
studenttable.column('Address',width=300,anchor=CENTER)
studenttable.column('Gender',width=300,anchor=CENTER)
studenttable.column('D.O.B',width=100,anchor=CENTER)
studenttable.column('Added Date',width=300,anchor=CENTER)
studenttable.column('Added Time',width=300,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',12),foreground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'))


studenttable.config(show='headings')

root.mainloop()