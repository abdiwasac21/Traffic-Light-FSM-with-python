from tkinter import *


def maingreen():
    # Green lights are on for 60s so here is also turned on for 60s
    global start_timer
    canvas.itemconfig(main_1, image= green_image)
    canvas.itemconfig(main_2, image= green_image)
    canvas.itemconfig(side_1,  image= red_image)
    canvas.itemconfig(side_2,  image= red_image)
    # when you run the code u have to wait 60s, if u can't just change the 60,000 to lower ms
    start_timer= window.after(60000, func=yellowmain)

def yellowmain():
    # Yellow  lights are on only 6s
    global start_timer
    canvas.itemconfig(main_1, image= yellow_image)
    canvas.itemconfig(main_2, image= yellow_image)
    canvas.itemconfig(side_1, image= red_image)
    canvas.itemconfig(side_2, image= red_image)
    start_timer = window.after(6000, func=greensides)


def greensides():
    # Another 60s for the side roads
    global start_timer
    canvas.itemconfig(main_1,  image= red_image)
    canvas.itemconfig(main_2,  image= red_image)
    canvas.itemconfig(side_1, image= green_image)
    canvas.itemconfig(side_2, image= green_image)
    start_timer= window.after(5000, func=yellowsides)

def yellowsides():
    global start_timer
    canvas.itemconfig(main_1,  image= red_image)
    canvas.itemconfig(main_2,  image= red_image)
    canvas.itemconfig(side_1, image= yellow_image)
    canvas.itemconfig(side_2, image= yellow_image)
    start_timer= window.after(4000, func=maingreen)

def redboth():
    # when a pedastrian clicks the emergancy button all lights turn red for 10s
    global start_timer
    canvas.itemconfig(main_1,  image= red_image)
    canvas.itemconfig(main_2,  image= red_image)
    canvas.itemconfig(side_1,  image= red_image)
    canvas.itemconfig(side_2,  image= red_image)
    start_timer= window.after(2000, func=maingreen)

# This Part is the GUI part
window = Tk()

window.configure(background="white")
window.geometry("900x750")
start_timer = window.after(1000, func=maingreen)
text = Label(text="Welcome To Traffic Light FSM")
canvas = Canvas(width=800, height=576, bg="white", highlightthickness=0)
road_img = PhotoImage(file="Images/road.png")
img = canvas.create_image(400, 300, image = road_img)
canvas.grid(column= 0, row=1, columnspan=2,  padx=50, pady=50)
red_image = PhotoImage(file="Images/red-light.png")
green_image = PhotoImage(file="Images/green-light.png")
yellow_image = PhotoImage(file="Images/yellow-light-2.png")
main_1 = canvas.create_image(500, 260, image= green_image)
main_2 = canvas.create_image(300, 260, image= green_image)
side_1 = canvas.create_image(400, 400, image= red_image)
side_2 = canvas.create_image(400, 150, image=red_image)

ped_butt = Button(text="click to Stop", width=20, height=3, background="#FFC94A", command=redboth)
ped_butt.grid(column=0, row=2, columnspan=2)
text.grid(column=0, row=0, columnspan=2)


window.mainloop()