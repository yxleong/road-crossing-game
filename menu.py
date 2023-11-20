from tkinter import *
import subprocess

NEW_GAME_BTN = "images/button_back.png"
RESUME_BTN = "images/button_resume.png"
QUIT_BTN = "images/button_quit.png"

def createBtn(btnPicPath, command=None):
    try:
        btnPic = PhotoImage(file=btnPicPath)
        btn = Button(window, image=btnPic, fg="blue", command=command)
        btn.img = btnPic
        btn.grid(padx=100, pady=10)
        return btn
    except Exception as e:
        print(f"Error creating button: {e}")
        return None

def new_game():
    window.destroy()
    subprocess.run(["python", "main.py"])
    return 1

def resume_game():
    window.destroy()
    return 0

def quit_game():
    window.destroy()
    return 1

def changeColor(event):
    if event["fg"] == "blue":
        event["fg"] = "red"
    else:
        event["fg"] = "blue"

window = Tk()
window.title("Turtle Road Crossing Game")

#entName = Entry(window, width=20, fg="blue")
#entName.grid(padx=100, pady=15)
#entName.bind("<Button-3>", changeColor)

lblMenu = Label(window, text="Menu", bg="light blue")
lblMenu.grid(padx=100, pady=15)

newGame = createBtn(NEW_GAME_BTN, command=new_game)
resumeGame = createBtn(RESUME_BTN, command=resume_game)
quitGame = createBtn(QUIT_BTN, command=quit_game)

window.mainloop()


# from tkinter import *

# def changeColor():
#     if btnCalculate["fg"] == "blue":
#         btnCalculate["fg"] == "red"
#     else:
#         btnCalculate["fg"] == "blue"

# window = Tk()
# window.title("Button")
# btnCalculate = Button(window, text = "Calculate", fg = "blue", command=changeColor)

# btnCalculate.grid(padx=100, pady=150)
# window.mainloop()