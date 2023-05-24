from tkinter import *
from tkinter import ttk

def OnMouseWheel(event):
    scrollbar1.yview_scroll(-1*(event.delta/120),"units")
    return "break"

root = Tk()

root.title("School Management System")

root.geometry("1300x1300+-8+-6")
root.state("zoomed")

width= 1300
height= 2000

root.geometry(str(width) + "x" + str(height) + "-8" + "-6")

main_Frame = Canvas(root, width=width, height=height)
main_Frame.pack(fill=BOTH, expand=1)
main_canvas = Canvas(main_Frame, width=200, height=height)
main_canvas.pack(side=LEFT, fill=BOTH, expand=1)


main_vertical_scrollbar = ttk.Scrollbar(main_Frame, orient=VERTICAL, command = main_canvas.yview)
main_vertical_scrollbar.pack(side=RIGHT, fill=Y)

main_canvas.configure(yscrollcommand=main_vertical_scrollbar.set)
main_canvas.bind("<MouseWheel>", OnMouseWheel)

scrollable_frame = Frame(main_canvas, bg="crimson", height=600, bd=5)
scrollable_frame.pack(side=TOP, fill=X)

top_frame = Frame(scrollable_frame, bg="crimson", height=600, bd=5)
top_frame.pack(side=TOP, fill=X)
menu_frame = Frame(scrollable_frame, bg="blue", height=30, bd=5, relief=RIDGE)
menu_frame.pack(side=TOP, fill=X, anchor=SW)
pane_frame = Frame(scrollable_frame, bg="white", bd=5, relief=GROOVE, width=1300, height=470)
pane_frame.pack(side=TOP)
bottom_frame = Frame(scrollable_frame, bg="grey", height=20, bd=5)
bottom_frame.pack(side=BOTTOM)

navigation_pane_frame = Frame(pane_frame, bg="Blue", width=400, height=470)
navigation_pane_frame.pack(side=LEFT)
space_pane_frame = Frame(pane_frame, width=20, height=470)
space_pane_frame.pack(side=LEFT)
action_pane_frame = Frame(pane_frame, bg="purple", width=200, height=470)
action_pane_frame.pack(side=RIGHT)
detail_pane_frame = Frame(pane_frame, bg="black", width=600, height=470)
detail_pane_frame.pack(side=RIGHT)

root.mainloop()