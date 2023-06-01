from tkinter import *
import playsound
import time
from tkinter import messagebox

morseDict = {'A': '.-', 'B': '-...',
             'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-',
             'L': '.-..', 'M': '--', 'N': '-.',
             'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',
             'X': '-..-', 'Y': '-.--', 'Z': '--..',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.',
             '0': '-----', ', ': '--..--', '.': '.-.-.-',
             '?': '..--..', '/': '-..-.', '-': '-....-',
             '(': '-.--.', ')': '-.--.-', ' ': '/', '\n': ' ', '': ''}

reverse_Dict = {v: k for k, v in morseDict.items()}


def play_morse(result):
    for c in result:
        if c == ".":
            playsound.playsound("dot.mp3")
            time.sleep(0.25)
        elif c == "-":
            playsound.playsound("dash.mp3")
            time.sleep(0.25)
        elif c == " " or c == "/":
            time.sleep(0.38)
        else:
            print("Invalid character")


def create_window1():
    def encrypt():
        inputi = output.get("1.0", END)
        try:
            result = " ".join(morseDict[c] for c in inputi.upper())
        except:
            messagebox.showerror(title="Error", message="Invalid input")

        label5 = Label(new_window, text=result,
                       font=("Times New Roman", 20),
                       bd=10,
                       relief="sunken",
                       )
        label5.pack()

        for c in result:
            if c == ".":
                playsound.playsound("dot.mp3")
                time.sleep(0.25)
            elif c == "-":
                playsound.playsound("dash.mp3")
                time.sleep(0.25)
            elif c == " " or c == "/":
                time.sleep(0.3)
            else:
                print("Invalid character")

        output2.destroy()

    new_window = Tk()
    new_window.geometry("500x400")
    new_window.title("English To Morse")
    new_window.config(background="#085e56")

    label3 = Label(new_window, text="Enter a word or a phrase you want to translate",
                   font=("Times New Roman", 18, "bold"),
                   background="#085e56",
                   foreground="#FFFFFF",
                   bd=10,
                   padx=20,
                   pady=20)
    label3.pack()

    output = Text(new_window, width=20,
                  height=1,
                  bd=10,
                  font=("Times New Roman", 20))
    output.pack()

    submit_button = Button(new_window, text="Submit",
                           background="#085e56",
                           bd=10,
                           foreground="#FFFFFF",
                           padx=10,
                           pady=10,
                           command=encrypt)
    submit_button.pack()

    output2 = Text(new_window, width=20,
                   height=1,
                   bd=10,
                   font=("Times New Roman", 20),
                   state=DISABLED)
    output2.pack()

    window.destroy()


def create_window2():
    def decrypt():
        inputi = output.get("1.0", END)
        final_input = inputi.replace('\n', '')
        try:
            result2 = "".join(reverse_Dict[c] for c in final_input.split(" "))
        except:
            messagebox.showerror(title="Error", message="Invalid input")

        label5 = Label(new_window2, text=result2,
                       font=("Times New Roman", 20),
                       bd=10,
                       relief="sunken")
        label5.pack()

        output2.destroy()

    new_window2 = Tk()
    new_window2.geometry("500x400")
    new_window2.title("Morse To English")
    new_window2.config(background="#085e56")

    label4 = Label(new_window2, text="Enter the morse code you want to translate",
                   font=("Times New Roman", 18, "bold"),
                   background="#085e56",
                   foreground="#FFFFFF",
                   bd=10,
                   padx=20,
                   pady=20)
    label4.pack()

    output = Text(new_window2, width=20,
                  height=1,
                  bd=10,
                  font=("Times New Roman", 20))
    output.pack()

    submit_button = Button(new_window2, text="Submit",
                           background="#085e56",
                           bd=10,
                           foreground="#FFFFFF",
                           padx=10,
                           pady=10,
                           command=decrypt)
    submit_button.pack()

    output2 = Text(new_window2, width=20,
                   height=1,
                   bd=10,
                   font=("Times New Roman", 20))
    output2.pack()

    window.destroy()


window = Tk()

window.geometry("660x490")
window.title("Morse Code")
icon = PhotoImage(file="weird.png.png")
window.iconphoto(True, icon)
window.config(background="#085e56")

label = Label(window, text="Welcome to the Morse Code Translator",
              font=("Times New Roman", 20, "bold"),
              background="#085e56",
              foreground="#FFFFFF",
              relief="sunken",
              bd=10,
              padx=20,
              pady=20)
label.pack()

label2 = Label(window, text="Choose one of the options below",
               font=("Times New Roman", 20, "bold"),
               background="#085e56",
               foreground="#FFFFFF",
               bd=10,
               padx=20,
               pady=20)
label2.pack()
spacer = Label(window, background="#085e56",
               bd=10,
               padx=40,
               pady=20)

spacer.pack(side="left")

spacer2 = Label(window, background="#085e56",
                bd=10,
                padx=40,
                pady=20)

spacer2.pack(side="right")

button = Button(window, text="English to Morse",
                font=("Times New Roman", 12),
                command=create_window1,
                fg="#FFFFFF",
                bg="#1a919c",
                activebackground="#1a919c",
                state=ACTIVE,
                activeforeground="#FFFFFF",
                relief="raised")
button.pack(side="left", anchor="w")

button2 = Button(window, text="Morse to English",
                 font=("Times New Roman", 12),
                 command=create_window2,
                 fg="#FFFFFF",
                 bg="#1a919c",
                 activebackground="#1a919c",
                 state=ACTIVE,
                 activeforeground="#FFFFFF",
                 relief="raised")

button2.pack(side="right", anchor="w")

window.mainloop()
