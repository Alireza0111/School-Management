from tkinter import *
from tkinter import ttk


main_window = Tk()
main_window.geometry("700x700")
main_window.configure(background="#F7F0F0")
main_window.title("SCHOOL MANAGEMENT")
#logo.........
logo1=PhotoImage(file="logo1.png")
label_1=Label(main_window,image=logo1,bg="#F7F0F0" ).place(x=100,y=50)
#declear user variable.............
user_name=StringVar()
user_password=StringVar()
#user name label...............
label_2 = Label(main_window, text="User Name:",bg="#F7F0F0" ,font=("arial",15,"bold")).place(x=100,y=350)
#uder name entry label.......
entry_1=Entry(main_window,textvariable=user_name,bg="#F7F0F0" ,font=("arial",15) ).place(x=250,y=350)

#Password label......
label_3 = Label(main_window, text="Password:" ,bg="#F7F0F0" ,font=("arial",15,"bold")).place(x=100,y=400)
#password entry label.....
entry_2=Entry(main_window,show="*",textvariable=user_password,bg="#F7F0F0" ,font=("arial",15) ).place(x=250,y=400)



#login button action......
def login():
    print("username="+str(user_name.get()))
    print("PasswordPassword="+str(user_password.get()))
    print("login")
    new()

login_button=Button(main_window,bg="#F7F0F0" ,text="Login" ,height=2,width=10,command=login).place(x=394,y=440)
#signup button action......



def signin():
    print("sign in")
    signup_window = Tk()
    signup_window.geometry("700x700")
    signup_window.configure(background="#F7F0F0")
    signup_window.title("signup")


butn_2 = Button(main_window,bg="#F7F0F0" , text="If you don't have any account please signup" ,fg="blue",borderwidth=0,font=("arial",13,"italic","underline"),command=signin).place(x=50,y=550)
butn_3 =Button(main_window, text="  Adimin Login")
butn_3.place(x=50,y=600)

logo_2=PhotoImage(file="admin_logo.png",)
logo_2=logo_2.subsample(10,10)
butn_3.config(image=logo_2,compound=LEFT,bg="#F7F0F0",font=("arial",13),padx=8,pady=3)
main_window.mainloop()


