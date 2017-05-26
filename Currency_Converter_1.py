import json
import urllib.request
import urllib.response
from tkinter import *
from tkinter import ttk
import codecs

with urllib.request.urlopen('http://api.fixer.io/latest?base=USD') as response:
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))

    rates= obj["rates"]
    currencies=rates.keys()

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Currency Converter")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Equivalent Conversion:")
        self.instructions = Label(master, text="Enter USD, select output, Convert")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.convert_button = Button(master, text="convert", command=lambda: self.convert())


        ##This is For the Dropdown Menu
        self.var = StringVar(master)
        self.currency="AUD"
        self.var.set("AUD")
        self.option = OptionMenu(root, self.var, *currencies)
        self.select_button = Button(master, text="Select", command=lambda: self.select())

        # ID Where Everything Goes
        self.instructions.grid(row=0,column=0, columnspan=3)
        self.label.grid(row=4, column=0, sticky=W)
        self.total_label.grid(row=4, column=1, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.convert_button.grid(row=3, column=0, sticky=E)
        self.option.grid(row=2, column=0, sticky=W)
        self.select_button.grid(row=2,column=1)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = float(new_text)
            return True
        except ValueError:
            return False

    def convert(self):
        conversion=self.entered_number
        rate=rates[self.currency]
        converted=conversion*rate
        converted=float("{0:.2f}".format(converted))
        self.total=converted
        self.total_label_text.set(self.total)


    def select(self):
        self.currency=self.var.get()

root = Tk()
my_gui = Calculator(root)
root.mainloop()
