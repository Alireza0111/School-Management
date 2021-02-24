from tkinter import *

student_window = Tk()
student_window.geometry("700x700")
student_window.configure(background="#F7F0F0")
student_window.title("Student Form")

#declear user variable.............
user_name=StringVar()
user_password=StringVar()

#user Details label...............
label_1 = Label(student_window, text="STUDENT FORM",bg="#F7F0F0" ,font=("arial",20,"bold")).place(x=230,y=50)


#Profile Option......

def profile():
    print("Profile")
    profile_window = Tk()
    profile_window.geometry("700x700")
    profile_window.configure(background="#F7F0F0")
    profile_window.title("Student Profile")

    logo2 = PhotoImage(file="logo2.png")
    plabel_0 = Label(profile_window, image=logo2, bg="#F7F0F0").place(x=500, y=130)
    plabel_1 = Label(profile_window, text="::STUDENT PROFILE::", bg="#F7F0F0", font=("italic", 20, "bold"),
                     fg="blue").place(x=210, y=20)
    plabel_2 = Label(profile_window, text="ID:", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=500, y=100)

    plabel_3 = Label(profile_window, text="Name        :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=100)
    plabel_4 = Label(profile_window, text="Father Name :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=150)
    plabel_5 = Label(profile_window, text="Mother Name :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=200)
    plabel_6 = Label(profile_window, text="Contact No. :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=250)
    plabel_7 = Label(profile_window, text="Email       :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=300)
    plabel_8 = Label(profile_window, text="Birth Date  :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=350)
    plabel_9 = Label(profile_window, text="Gender      :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=400)
    plabel_10 = Label(profile_window, text="Address    :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=450)
    plabel_11 = Label(profile_window, text="Signature  :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=500)
    profile_window.mainloop()

butn_1=Button(student_window, text=" Profile",bg="#F7F0F0" ,font=("arial",15,"bold"),borderwidth=3,height="5",width="58",command=profile).place(x=0,y=150)


#Fees Option......

def Fees():
    print("Fees")
    Fees_window = Tk()
    Fees_window.geometry("700x700")
    Fees_window.configure(background="#F7F0F0")
    Fees_window.title("Student Fees")

butn_2=Button(student_window, text=" Fees",bg="#F7F0F0" ,font=("arial",15,"bold"),borderwidth=3,height="5",width="58",command=Fees).place(x=0,y=300)


#Communication Option......

def Communication():
    print("Communication")
    Communication_window = Tk()
    Communication_window.geometry("700x700")
    Communication_window.configure(background="#F7F0F0")
    Communication_window.title("Communication")

butn_3=Button(student_window, text=" Communication",bg="#F7F0F0" ,font=("arial",15,"bold"),borderwidth=3,height="5",width="58",command=Communication).place(x=0,y=450)




student_window.mainloop()


