from tkinter import *

root = Tk()

root.title("Codabra Neuro")
root.geometry("300x400")

def toSquare():
    result = int(entry_data.get())
    int_arr = []
    for i in range(2,10):
        res = result**i
        int_arr.append(str(res))
    s = ", "
    final_res = s.join(int_arr) #объединие
    res_square = Label(root, text=final_res)
    res_square.pack()
    
   


entry_data = Entry() 
entry_data.pack()

label_square = Label(root, text="Результат квадрата")
label_square.pack()

# сюда пишется результат

# res_square.pack()

square_btn = Button(root, text = "square", command=toSquare)
square_btn.pack()


root.mainloop()
