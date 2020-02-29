from tkinter import *
from codabra_neuro import assert_auto

class Assert_Codabra:
    def __init__(self, root, title, labelText, button_Text):
        self.root = root
        self.title = title

        self.label = Label(root, text=labelText)
        self.label.pack() 

        self.main_cond = Entry()
        self.main_cond.pack()

        self.second_cond = Entry()
        self.second_cond.pack()

        self.lr = Entry()
        self.lr.pack()
        
        self.accur = Entry()
        self.accur.pack()

        self.epoch = Entry()
        self.epoch.pack()

        self.main_btn =  Button(root, text = button_Text, command = self.assertation)
        self.main_btn.pack()

        self.label_result = Label(root, text='')
        self.label_result.pack()

    def assertation(self):
        result = assert_auto(int(self.main_cond.get()), int(self.second_cond.get()), float(self.lr.get()), float(self.accur.get()),  int(self.epoch.get()))
        print(result)
        self.label_result["text"] = str(result)



root = Tk()

codabra_length = Assert_Codabra(root, " программа", "введите данные", "вычислить")

root.geometry("400x400")
root.mainloop()