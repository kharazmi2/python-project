from vars import *
def show():
    for i in labs:
        i.pack()
    buttons[0].pack(side="left", padx=90)
    buttons[1].pack(side="right", padx=90)