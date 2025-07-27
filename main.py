import tkinter as tk
import time
import random

def sendtext(event=None):
    user_input = entry.get()
    chatbox.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)
    x = random.randint(0,3000)
    chatbox.after(x, bot_reply)

def bot_reply():
    chatbox.insert(tk.END, "Retardsim: fuck you\n")
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Retardsim")

chatbox = tk.Text(root, height=50, width=50)
chatbox.pack()

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT)
send_button = tk.Button(root, text="Send", command=sendtext)
entry.bind('<Return>',sendtext)
send_button.pack(side=tk.LEFT)

root.mainloop()

