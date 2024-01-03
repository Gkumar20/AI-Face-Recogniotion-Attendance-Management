from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def Help(root):
    root.title("Attendance marking system using multiple face recognition system")
    root.configure(background="lightgray")
    root.geometry("1520x780+0+0")
    root.wm_iconbitmap("Desktop_Icon.ico")

    # Header
    header_frame = ttk.Frame(root, style="Header.TFrame")
    header_frame.place(x=10, y=10, width=1500, height=100)
    style = ttk.Style()
    style.configure("Header.TFrame", background="white", relief="raised")

    # Title in the header
    title_label = Label(header_frame, text="Help - Facial Recognition & Attendance System", font=("Helvetica", 30, "bold"), bg="white", fg='#3498db')
    title_label.pack(pady=20)

    # Background box
    background_box = ttk.Frame(root, style="Background.TFrame")
    background_box.place(x=10, y=110, width=1500, height=660)
    style.configure("Background.TFrame", background="white", borderwidth=5, relief="groove")

    # Background image inside the box
    bg_image = Image.open("public/background.jpg")
    bg_image = bg_image.resize((1500, 660), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(background_box, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.pack()

    # Main frame
    main_frame = Frame(background_box, bd=2, bg="white")
    main_frame.place(x=15, y=30, width=600, height=600)

    # Add content to the main frame
    section_title = Label(main_frame, text="Welcome to Help Section", font=("Helvetica", 20, "bold"), bg="white", fg="#3498db")
    section_title.pack(pady=20)

    # Section 1 - Instructions
    instructions_label = Label(main_frame, text="Instructions:", font=("Helvetica", 16, "bold"), bg="white", fg="#333")
    instructions_label.pack(pady=10, anchor=W)

    instructions_text = Text(main_frame, wrap=WORD, font=("Helvetica", 12), height=6, width=60)
    instructions_text.insert(END, "1. Capture an image or use a camera for facial recognition.\n\n2. Wait for the system to detect and identify faces.\n\n3. Review the attendance details and save if necessary.")
    instructions_text.config(state=DISABLED)
    instructions_text.pack(pady=10, padx=10)

    # Section 2 - Process
    process_label = Label(main_frame, text="Process:", font=("Helvetica", 16, "bold"), bg="white", fg="#333")
    process_label.pack(pady=10, anchor=W)

    process_text = Text(main_frame, wrap=WORD, font=("Helvetica", 12), height=6, width=60)
    process_text.insert(END, "1. Start the system.\n\n2. Register and Gather the Students Details\n\n3. Make Sure that the every student have their respective images.\n\n4. Train the Model.\n\n5. Start Recognition and Mark Attendance.\n\n6. Review attendance logs.")
    process_text.config(state=DISABLED)
    process_text.pack(pady=10, padx=10)


    # section 3     
    video_canvas = Canvas(background_box, bg="black")
    video_canvas.place(x=630, y=30, width=860, height=600)

    video_frames = [
        "public/page1.png",
        "public/page2.png",
        "public/page3.png",
        "public/page4.png",
        "public/page5.png",
        "public/page6.png",
    ]
    video_image_list = [Image.open(frame).resize((860, 660), Image.LANCZOS) for frame in video_frames]
    video_photo_list = [ImageTk.PhotoImage(img) for img in video_image_list]

    def update_video_frame(idx):
        video_canvas.create_image(0, 0, anchor=NW, image=video_photo_list[idx])
        root.after(2000, lambda: update_video_frame((idx + 1) % len(video_photo_list)))

    update_video_frame(0)


if __name__ == "__main__":
    root = Tk()
    Help(root)
    root.mainloop()
