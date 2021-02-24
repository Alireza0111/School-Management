from tkinter import *

profile_window = Tk()
profile_window.geometry("700x700")
profile_window.configure(background="#F7F0F0")
profile_window.title("Student Profile")


#image.........
logo2=PhotoImage(file="logo2.png")
plabel_0=Label(profile_window,image=logo2,bg="#F7F0F0" ).place(x=500,y=130)

# user Details label...............
plabel_1=Label(profile_window,text="::STUDENT PROFILE::",bg="#F7F0F0",font=("italic",20,"bold"),fg="blue").place(x=210,y=20)
plabel_2= Label(profile_window, text="ID:", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=500, y=100)

plabel_3= Label(profile_window, text="Name        :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=100)
plabel_4= Label(profile_window, text="Father Name :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=150)
plabel_5= Label(profile_window, text="Mother Name :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=200)
plabel_6= Label(profile_window, text="Contact No. :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=250)
plabel_7= Label(profile_window, text="Email       :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=300)
plabel_8= Label(profile_window, text="Birth Date  :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=350)
plabel_9= Label(profile_window, text="Gender      :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=400)
plabel_10= Label(profile_window, text="Address    :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=450)
plabel_11= Label(profile_window, text="Signature  :", bg="#F7F0F0", font=("arial", 12, "bold")).place(x=5, y=500)


profile_window.mainloop()
