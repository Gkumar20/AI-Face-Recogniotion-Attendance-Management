    teacher_name_label = Label(top_frame, text="Prof. D.K. Ray", font=("times new roman", 25, "bold"), fg="black")
    teacher_name_label.place(relx=0.5, rely=0.15, anchor="center")  # Positioned in the center horizontally

    # Project Description
    project_label = Label(top_frame, text="Final Year Project\nMultiple Face Recognition using AI", font=("times new roman", 18), fg="black")
    project_label.place(relx=0.5, rely=0.35, anchor="center")  # Positioned in the center horizontally

    # Guidance Note
    guidance_label = Label(top_frame, text="Under the guidance of Prof. D.K. Ray", font=("times new roman", 14), fg="black")
    guidance_label.place(relx=0.5, rely=0.55, anchor="center")  # Positioned in the center horizontally

    # Additional beautiful lines about the project
    beautiful_lines = Label(top_frame, text="Your beautiful lines here...", font=("times new roman", 14), fg="black")
    beautiful_lines.place(relx=0.5, rely=0.75, anchor="center")