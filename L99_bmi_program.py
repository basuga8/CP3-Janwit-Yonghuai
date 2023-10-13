from tkinter import *
import math

def left_click_button(event):
    result = round(float(text_box_weight.get()) / math.pow(float(text_box_height.get())/100,2))
    #print(round(float(text_box_weight.get()) / math.pow(float(text_box_height.get())/100,2)))
    label_result.configure(text=result)
    result_bmi = ""
    if result > 30:
        result_bmi = "อ้วนมาก"
    elif result >= 25:
        result_bmi = "อ้วน"
    elif result >= 23:
        result_bmi = "น้ำหนักเกิน"
    elif result >= 18:
        result_bmi = "น้ำหนักปกติ"
    elif result < 18:
        result_bmi = "ผอมเกินไป"
    label_bmi.configure(text=result_bmi)

main_window = Tk()
label_height = Label(main_window, text="ส่วนสูง (cm.)")
label_height.grid(row=0, column=0)
text_box_height = Entry(main_window)
text_box_height.grid(row=0, column=1)
label_weight = Label(main_window, text="น้ำหนัก (kg.)")
label_weight.grid(row=1, column=0)
text_box_weight = Entry(main_window)
text_box_weight.grid(row=1, column=1)

calculate_button = Button(main_window, text="คำนวณ", width=12)
calculate_button.bind('<Button-1>', left_click_button)
calculate_button.grid(row=2, column=0)

label_result = Label(main_window, text="ผลลัพธ์", bg="orange", width=15)
label_result.grid(row=2, column=1)
label_bmi = Label(main_window, text="BMI", bg="orange", width=15)
label_bmi.grid(row=3, column=1)


main_window.mainloop()