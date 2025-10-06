import time
from tkinter import *
import random
def play():
    from Sound import BG_Sound
    x1=400
    y1=300
    x2=420
    y2=320

    Snake = Tk()
    screen_Width = Snake.winfo_screenwidth()
    screen_Height = Snake.winfo_screenheight()
    Snake.geometry(f"{screen_Width}x{screen_Height}")

    canvas = Canvas(Snake, width=screen_Width-210, height=screen_Height-305, bg='Black', highlightthickness=5, highlightbackground='dark green')
    canvas.pack(side='top')
    rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill='Dark Green')
    btn_y = screen_Height - 200
    btn_x = 500
    btn_spacing = 80

    x_1=x1
    x_2=x2
    y_1=y1
    y_2=y2

    def move_left():
        canvas.move(rect_id, -20, 0)
    def movementFunction_for_B1():
        nonlocal x_1, x_2
        x_1 -= 20
        x_2 -= 20
        if (x_1 == -20):
            time.sleep(0.5)
            Snake.destroy()
        return x_1, x_2
    def c_command_for_B1():
        move_left()
        movementFunction_for_B1()

    def move_up():
        canvas.move(rect_id, 0, -20)
    def movementFunction_for_B2():
        nonlocal y_1, y_2
        y_1 -= 20
        y_2 -= 20
        if (y_1 == -20):
            time.sleep(0.5)
            Snake.destroy()
        return y_1, y_2
    def c_command_for_B2():
        move_up()
        movementFunction_for_B2()

    def move_right():
        canvas.move(rect_id, 20, 0)
    def movementFunction_for_B3():
        nonlocal x_1, x_2
        x_1 += 20
        x_2 += 20
        if (x_2 == screen_Width-180):
            time.sleep(0.5)
            Snake.destroy()
        return x_1, x_2
    def c_command_for_B3():
        move_right()
        movementFunction_for_B3()

    def move_down():
        canvas.move(rect_id, 0, 20)
    def movementFunction_for_B4():
        nonlocal y_1, y_2
        y_1 += 20
        y_2 += 20
        if (y_2 == screen_Height-280):
            time.sleep(0.5)
            Snake.destroy()
        return y_1, y_2
    def c_command_for_B4():
        move_down()
        movementFunction_for_B4()

    Button(Snake, text="\u2190", command=c_command_for_B1).place(x=btn_x, y=btn_y, width=60, height=40)
    Button(Snake, text="\u2191", command=c_command_for_B2).place(x=btn_x + btn_spacing, y=btn_y, width=60, height=40)
    Button(Snake, text="\u2192", command=c_command_for_B3).place(x=btn_x + btn_spacing * 2, y=btn_y, width=60, height=40)
    Button(Snake, text="\u2193", command=c_command_for_B4).place(x=btn_x + btn_spacing * 3, y=btn_y, width=60, height=40)
    from Sound import stop_BG_Sound
    Snake.mainloop()
    play_again()
    
def play_again():
    play_again=Tk()
    play_again.geometry("400x200")
    def Show_starting_window_and_destroy():
        play_again.destroy()
        Show_starting_window()
    def end():
        play_again.destroy()
    button_Play_again=Button(play_again, text="Play again", command=Show_starting_window_and_destroy).pack()
    button_close=Button(play_again, text="close", command=end).pack(padx=10,pady=10)
    play_again.mainloop()

def Show_starting_window():
    stating_window= Tk()
    stating_window.geometry("400x200")
    def stating_window_play_and_destroy():
        stating_window.destroy()
        play()
    Button_PLAY=Button(stating_window, text="Play", command=stating_window_play_and_destroy).pack()
    stating_window.mainloop()


Show_starting_window()