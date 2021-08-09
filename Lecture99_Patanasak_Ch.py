from tkinter import *
import math

def leftClickButton(event):
    BMI = (float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if BMI <= 18.50:
        labelResult.configure(text = "น้ำหนักน้อย / ผอม")
    elif BMI >= 18.50 and BMI <= 22.90:
        labelResult.configure(text ="ปกติ - สุขภาพดี")
    elif BMI >= 22.90 and BMI <= 24.90:
        labelResult.configure(text ="ท้วม / โรคอ้วนระดับ 1")
    elif BMI >= 24.90 and BMI <= 29.90:
        labelResult.configure(text="อ้วน / โรคอ้วนระดับ 2")
    else :
        labelResult.configure(text ="อ้วนมาก / โรคอ้วนระดับ 3")


MainWindow = Tk()

labelHeight = Label(MainWindow,text = "ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text = "น้าหนัก (kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2)

labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()
