//Final_code.ipynb:

import tkinter as tk 
from tkinter import messagebox, filedialog 
import mysql.connector 
from ultralytics import YOLO 
import cv2 
import numpy as np 
class Multiwindow: 
def __init__(self): 
self.root = tk.Tk() 
self.root.title("road accident prediction") 
self.root.config(bg="light grey") 
self.root.geometry("500x400") 
self.create_widgets() 
def create_widgets(self): 
# Buttons for navigation 
self.login_button = tk.Button(self.root, text="Login", bg="white", fg="black", 
font=("arial", 20),  
command=self.login) 
self.login_button.place(x=200, y=120) 
self.register_button = tk.Button(self.root, text="Registration", bg="white", fg="black", 
font=("arial", 20),  
command=self.register) 
self.register_button.place(x=165, y=200) 
def login(self): 
self.clear_root() 
self.login_frame = tk.Frame(self.root, bg="lightgrey") 
self.login_frame.place(relx=0.5, rely=0.5, anchor="center") 
title = tk.Label(self.login_frame, text="Login", bg="lightgrey", fg="black", 
font=("arial", 30)) 
title.grid(row=0, column=0, columnspan=2, pady=10) 
name_label = tk.Label(self.login_frame, text="Name:", bg="lightgrey", fg="black", 
font=("arial", 15)) 
name_label.grid(row=1, column=0) 
self.name_en = tk.Entry(self.login_frame) 
self.name_en.grid(row=1, column=1) 
35 
pwd_label = tk.Label(self.login_frame, text="Password:", bg="lightgrey", fg="black", 
font=("arial", 15)) 
pwd_label.grid(row=2, column=0) 
self.pwd_en = tk.Entry(self.login_frame, show="*") 
self.pwd_en.grid(row=2, column=1) 
submit_button = tk.Button(self.login_frame, text="Submit", bg="WHITE", fg="black", 
font=("arial", 15),  
command=self.validation) 
submit_button.grid(row=3, column=0, columnspan=2, pady=10) 
back_button = tk.Button(self.login_frame, text="Back", bg="light grey", fg="black", 
font=("arial", 15),  
command=self.back_to_menu) 
back_button.grid(row=4, column=0, columnspan=2, pady=10) 
def register(self): 
self.clear_root() 
self.register_frame = tk.Frame(self.root, bg="lightgrey") 
self.register_frame.place(relx=0.5, rely=0.5, anchor="center") 
title1 = tk.Label(self.register_frame, text="Registration", bg="lightgrey", fg="black", 
font=('bold', 30)) 
title1.grid(row=0, column=0, columnspan=2, pady=10) 
labels = ["Name", "Password", "EmailId"] 
for i, label in enumerate(labels): 
label_widget = tk.Label(self.register_frame, text=label, bg="lightgrey", fg="black", 
font=("Arial", 15)) 
label_widget.grid(row=i+1, column=0) 
entry = tk.Entry(self.register_frame) 
entry.grid(row=i+1, column=1) 
setattr(self, f"box{i+1}_en", entry) 
submit_button = tk.Button(self.register_frame, text="Submit", fg="black", bg="white", 
font=("arial", 17),  
command=self.reg) 
submit_button.grid(row=4, column=0, columnspan=2, pady=10) 
back_button = tk.Button(self.register_frame, text="Back", bg="light grey", fg="black", 
font=("arial", 15), 
command=self.back_to_menu) 
back_button.grid(row=5, column=0, columnspan=2, pady=10) 
def clear_root(self): 
for widget in self.root.winfo_children(): 
36 
 
 
37 
 
            widget.destroy() 
 
 
    def back_to_menu(self): 
        self.clear_root() 
        self.create_widgets() 
         
    def validation(self): 
        name = self.name_en.get() 
        password = self.pwd_en.get() 
        mydb=mysql.connector.connect(host="localhost",user="root", password="root", 
port=3306, database="mydatabase") 
        mycursor = mydb.cursor() 
        mycursor.execute("select * from student where name=%s and password=%s", (name, 
password)) 
        c = 0 
        for _ in mycursor: 
            c += 1 
        if c >= 1: 
            messagebox.showinfo("Result", "Logged in Successfully ") 
            self.clear_root() 
            app = VideoUploaderApp(self.root, self.back_to_menu) 
        else: 
            messagebox.showinfo("Result", "Incorrect details entered") 
 
    def reg(self): 
       name = self.box1_en.get() 
       password = self.box2_en.get() 
       emailid = self.box3_en.get() 
       mydb = mysql.connector.connect(host="localhost", user="root", password="root", 
port=3306, database="mydatabase") 
       mycursor = mydb.cursor() 
       mycursor.execute("insert into student values(%s,%s,%s)", (name, password, emailid)) 
       mydb.commit() 
       messagebox.showinfo("Result", "Registered Successfully") 
 
class VideoUploaderApp(tk.Frame): 
    def __init__(self, root, back_to_menu): 
        super().__init__(root) 
        self.root = root 
        self.root.title("Video Uploader") 
        self.root.geometry("500x400") 
        self.root.config(bg="light grey") 
 
        self.file_path = tk.StringVar() 
        self.back_to_menu = back_to_menu 
self.create_widgets() 
def create_widgets(self): 
# Label 
self.label = tk.Label(self.root, text="Select a video to upload:", bg="light grey", 
fg="BLACK", font=("arial", 20)) 
self.label.place(x=100, y=35) 
# Button to browse file 
self.browse_button=tk.Button(self.root,text="Browse", command=self.browse_file, 
bg="white", fg="black", 
font=("arial", 20)) 
self.browse_button.place(x=200, y=120) 
# Entry to display file path 
self.file_entry=tk.Entry(self.root,textvariable=self.file_path, state='readonly', 
width=(20), font=("arial", 17)) 
self.file_entry.place(x=115, y=190) 
# Upload button 
self.upload_button=tk.Button(self.root,text="Upload", command=self.upload_video, 
bg="white", fg="black", 
font=("arial", 20)) 
self.upload_button.place(x=200, y=235) 
# Back button 
self.back_button=tk.Button(self.root,text="Back", command=self.back_to_menu, 
bg="light grey", fg="black", 
font=("arial", 15)) 
self.back_button.place(x=10, y=10) 
def browse_file(self): 
file_path=filedialog.askopenfilename(filetypes=[("Videofiles", ".mp4;.avi;*.mkv")]) 
if file_path: 
self.file_path.set(file_path) 
def upload_video(self): 
file_path = self.file_path.get() 
if file_path: 
model = YOLO("best .pt") 
class_names = model.names 
cap = cv2.VideoCapture(file_path) 
while True: 
38 
ret, img = cap.read() 
if not ret: 
break 
img = cv2.resize(img, (1020, 500)) 
h, w, _ = img.shape 
results = model.predict(img) 
for r in results: 
boxes = r.boxes  # Boxes object for bbox outputs 
masks = r.masks  # Masks object for segment masks outputs 
if masks is not None: 
masks = masks.data.cpu() 
for seg, box in zip(masks.data.cpu().numpy(), boxes): 
seg = cv2.resize(seg, (w, h)) 
contours,_=cv2.findContours((seg).astype(np.uint8), cv2.RETR_EXTERNAL, 
cv2.CHAIN_APPROX_SIMPLE) 
for contour in contours: 
d = int(box.cls) 
c = class_names[d] 
x, y, x1, y1 = cv2.boundingRect(contour) 
cv2.polylines(img,[contour],True,color=(0, 0, 255), thickness=2) 
cv2.putText(img,c,(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 
255, 255), 1) 
cv2.imshow('img', img) 
if cv2.waitKey(1) & 0xFF == ord('q'): 
break 
cap.release() 
cv2.destroyAllWindows() 
else: 
messagebox.showerror("Error", "Please select a video file to upload.") 
if __name__ == "__main__": 
m = Multiwindow() 
m.root.mainloop() 
