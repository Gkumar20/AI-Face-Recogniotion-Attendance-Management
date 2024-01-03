from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from about import About
from help import Help
import os
from time import strftime
from datetime import datetime

def main(root):
    # configure window
    root.title("Attendance marking system using multiple face recognition system")
    root.configure(background="gray")
    root.geometry("1520x780+0+0")
    root.wm_iconbitmap("Desktop_Icon.ico")



    # Header
    header_frame = ttk.Frame(root, style="Header.TFrame")
    header_frame.place(x=10, y=10, width=1500, height=100)

    style = ttk.Style()
    style.configure("Header.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Title in the header
    title_label = Label(header_frame, text="Face Recognition System Using AI", font=("Helvetica", 40, "bold"), bg="white", fg='skyblue')
    title_label.pack(pady=20)

    def time():
        string = strftime('%I:%M:%S %p')
        lbl.config(text = string)
        lbl.after(1000,time)
    
    lbl = Label(header_frame,font=('times new roman',14,'bold'),background='white',foreground='black')
    lbl.place(x=10,y=20,width=110,height=50)
    time()

    # Background box with rounded edges (resembling a shadow)
    background_box = ttk.Frame(root, style="Background.TFrame")
    background_box.place(x=10, y=110, width=1500, height=660)
    style.configure("Background.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Background image inside the box
    bg_image = Image.open("public/background.jpg")
    bg_image = bg_image.resize((1500, 660), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(background_box, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.pack()


    # Student Information
    btn_image1 = Image.open("public/register.jpeg")
    btn_image1 = btn_image1.resize((200, 200), Image.LANCZOS)
    btn_photo1 = ImageTk.PhotoImage(btn_image1)

    btn1_text = Button(background_box,command=student_details, text="Student Information", font=("Helvetica", 14, "bold"),bg="skyblue", fg='black',width=17)
    btn1_text.place(x=40, y=50)  

    btn1 = Button(background_box,command=student_details, image=btn_photo1, borderwidth=5)
    btn1.image = btn_photo1  
    btn1.place(x=40, y=80) 


    # Train Data
    btn_image4 = Image.open("public/admin.png")
    btn_image4 = btn_image4.resize((200, 200), Image.LANCZOS)
    btn_photo4 = ImageTk.PhotoImage(btn_image4)

    btn4_text = Button(background_box, text="Train Data",command=train_data, font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
    btn4_text.place(x=450, y=50)  

    btn4 = Button(background_box, image=btn_photo4, borderwidth=5,command=train_data)
    btn4.image = btn_photo4  
    btn4.place(x=450, y=80) 


    # Face Detector 
    btn_image2 = Image.open("public/face_recog.webp")
    btn_image2 = btn_image2.resize((200, 200), Image.LANCZOS)
    btn_photo2 = ImageTk.PhotoImage(btn_image2)

    btn2_text = Button(background_box, text="Face Detector",command=face_detection, font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
    btn2_text.place(x=850, y=50)  

    btn2 = Button(background_box, image=btn_photo2, borderwidth=5,command=face_detection)
    btn2.image = btn_photo2 
    btn2.place(x=850, y=80) 


    # Student Attendance
    btn_image3 = Image.open("public/attendance.jpeg")
    btn_image3 = btn_image3.resize((200, 200), Image.LANCZOS)
    btn_photo3 = ImageTk.PhotoImage(btn_image3)

    btn3_text = Button(background_box, text="Student Attendance",command=attendance_report, font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
    btn3_text.place(x=1250, y=50)  

    btn3 = Button(background_box, image=btn_photo3, borderwidth=5,command=attendance_report)
    btn3.image = btn_photo3  
    btn3.place(x=1250, y=80) 



    # Student Photos
    btn_image1 = Image.open("public/gallery.jpeg")
    btn_image1 = btn_image1.resize((200, 200), Image.LANCZOS)
    btn_photo1 = ImageTk.PhotoImage(btn_image1)

    btn1_text = Button(background_box, text="Student Photos",command=open_image, font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
    btn1_text.place(x=40, y=350)  

    btn1 = Button(background_box, image=btn_photo1, borderwidth=5,command=open_image)
    btn1.image = btn_photo1  
    btn1.place(x=40, y=380) 


    # About Us 
    btn_image2 = Image.open("public/developer.jpeg")
    btn_image2 = btn_image2.resize((200, 200), Image.LANCZOS)
    btn_photo2 = ImageTk.PhotoImage(btn_image2)

    btn2_text = Button(background_box, text="Developers",command=about_us, font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
    btn2_text.place(x=450, y=350)  

    btn2 = Button(background_box, image=btn_photo2, borderwidth=5,command=about_us)
    btn2.image = btn_photo2 
    btn2.place(x=450, y=380) 


    # Help Contact 
    btn_image3 = Image.open("public/help.jpeg")
    btn_image3 = btn_image3.resize((200, 200), Image.LANCZOS)
    btn_photo3 = ImageTk.PhotoImage(btn_image3)

    btn3_text = Button(background_box, text="Help",command=help_func, font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
    btn3_text.place(x=850, y=350)  

    btn3 = Button(background_box, image=btn_photo3, borderwidth=5,command=help_func)
    btn3.image = btn_photo3  
    btn3.place(x=850, y=380) 


    # Exit 
    btn_image4 = Image.open("public/exit.jpeg")
    btn_image4 = btn_image4.resize((200, 200), Image.LANCZOS)
    btn_photo4 = ImageTk.PhotoImage(btn_image4)

    btn4_text = Button(background_box, text="Exit Application",command=lambda:main_exit(root), font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
    btn4_text.place(x=1250, y=350)  

    btn4 = Button(background_box, image=btn_photo4, borderwidth=5,command=lambda:main_exit(root))
    btn4.image = btn_photo4  
    btn4.place(x=1250, y=380) 

# =============Student Image Open=======
def open_image():
    os.startfile("data")

# ==================functions for sgtudent detail=============
def student_details():
    new_window = Toplevel(root)
    app = Student(new_window)

# ==================functions for training=============
def train_data():
    new_window = Toplevel(root)
    app = Train(new_window)

# ==================functions for detection=============
def face_detection():
    new_window = Toplevel(root)
    app = Face_Recognition(new_window)
  
# ==================functions for Attendacne Report=============
def attendance_report():
    new_window = Toplevel(root)
    app = Attendance(new_window)


# ===========exit========
def main_exit(root):
    main_exit = tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit",parent=root)  
    if main_exit>0:
        root.destroy()
    else:
        return

# about us
def about_us():
    new_window = Toplevel(root)
    app = About(new_window)

# Help
def help_func():
    new_window = Toplevel(root)
    app = Help(new_window)

if __name__ == "__main__":
    root = Tk()
    main(root)
    root.mainloop()
