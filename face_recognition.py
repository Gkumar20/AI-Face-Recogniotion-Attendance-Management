import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import mysql.connector.locales.eng.client_error
from db_connection import get_database_connection



def Face_Recognition(root):
    # configure window
    root.title("Multiple Face Recognition System Using AI")
    root.configure(background="gray")
    root.geometry("1520x780+0+0")
    root.wm_iconbitmap("face.ico")

    # Header
    header_frame = ttk.Frame(root, style="Header.TFrame")
    header_frame.place(x=10, y=10, width=1500, height=100)

    style = ttk.Style()
    style.configure("Header.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Title in the header
    title_label = Label(header_frame, text="Face Recognition System", font=("Helvetica", 40, "bold"), bg="white", fg='brown')
    title_label.pack(pady=20)

    # Background box with rounded edges (resembling a shadow)
    background_box = ttk.Frame(root, style="Background.TFrame")
    background_box.place(x=10, y=110, width=1500, height=660)
    style.configure("Background.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Background image inside the box
    bg_image = Image.open("public/background1.png")
    bg_image = bg_image.resize((1500, 660), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(background_box, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.pack()

    
    # Button
    Recog_btn_image = Image.open("public/face.jpg")
    Recog_btn_image = Recog_btn_image.resize((300, 300), Image.LANCZOS)
    Recog_btn_photo = ImageTk.PhotoImage(Recog_btn_image)

    btn1 = Button(background_box, image=Recog_btn_photo ,borderwidth=5, command=face_recog)
    btn1.image = Recog_btn_photo 
    btn1.place(x=600, y=150)

# ==============functions ================

def mark_attendance(p,r,n,d):
    with open("attendance_report/attendance.csv","r+",newline="\n") as f:
        myDataList = f.readlines()
        name_list = []
        for line in myDataList:
            entry = line.split((","))
            name_list.append(entry[0])
        if((p not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{p},{r},{n},{d},{dtString},{d1},Present")


def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
        id, predict = clf.predict(gray_image[y:y + h, x:x + w])
        confidence = int((100 * (1 - predict / 300)))

        conn = get_database_connection()
        my_cursor = conn.cursor()

        my_cursor.execute("select Name from student where PRN=" + str(id))
        n = my_cursor.fetchone()
        n = "+".join(n)

        my_cursor.execute("select Roll from student where PRN=" + str(id))
        r = my_cursor.fetchone()
        r = "+".join(r)

        my_cursor.execute("select Dep from student where PRN=" + str(id))
        d = my_cursor.fetchone()
        d = "+".join(d)

        my_cursor.execute("select PRN from student where PRN=" + str(id))
        p = my_cursor.fetchone()
        p = "+".join(p)

        if confidence > 77:
            cv2.putText(img, f"PRN:{p}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            mark_attendance(p,r,n,d)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(img, f"Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

    return img


def recognize(img, clf, faceCascade):
    img = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
    return img


def face_recog():
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    video_cap = cv2.VideoCapture(0)

    while True:
        ret, img = video_cap.read()
        if ret:
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

        if cv2.waitKey(1) == 13:
            break

    video_cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    Face_Recognition(root)
    root.mainloop()