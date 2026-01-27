from tkinter import *
import math

def leftClick(event):
    BMI = (float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if BMI >= 30:
        labelResult.configure(text = "อ้วนมาก")
    elif (29.9 >= BMI >= 25.0):
        labelResult.configure(text = "อ้วน")
    elif (24.9 >= BMI >= 23.0):
        labelResult.configure(text = "น้ำหนักเกิน")
    elif (22.9 >= BMI >= 18.6):
        labelResult.configure(text = "น้ำหนักปกติ เหมาะสม")
    elif (18.5 > BMI ):
        labelResult.configure(text = "ผอมเกินไป")
    


MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (cm.)").grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
labelWeight = Label(MainWindow,text="น้ำหนัก (kg.)").grid(row=1,column=0)
textBoxWeight = Entry(MainWindow) 
textBoxHeight.grid(row=0,column=1)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวณ BMI")
calculateButton.grid(row=2,column=0)
calculateButton.bind('<Button-1>',leftClick)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2 , column = 1)
MainWindow.mainloop()