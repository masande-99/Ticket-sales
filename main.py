from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("400x200")
window.title("TicketSales")
window.configure(bg="lime")

soccer = 40
movie = 75
theater = 100

my_var = StringVar()
num = Entry(window, width=20, bd=12)
tickets = ttk.Combobox(window, textvariable=my_var, width=20, value=["Soccer", "Movie", "Theater"])
no_tickets = ttk.Spinbox(window, from_=0, to=20, state="readonly")
cell_number = Label(window, text="Cellphone number:", bg="lime")

ticket_cat = Label(window, text="Type of ticket:", bg="lime")

numbers_ticket = Label(window, text="No of tickets:", bg="lime")

answer = Label(window)
answer.grid(row=4, column=0)


def cal():

    if tickets.get() == "Soccer":
        price = soccer * int(no_tickets.get()) + (14/100)
        answer.config(text="Price:" + str(price) + "\n" + "tickets:"+str(no_tickets.get()) + "\n" + "Number:" + str(num.get()))

    if tickets.get() == "Movie":
        mov_price = movie * int(no_tickets.get()) + (14/100)
        answer.config(text="Price:" + str(mov_price) + "\n" + "tickets:"+str(no_tickets.get()) + "\n" + "Number:" + str(num.get()))

    if tickets.get() == "Theater":
        the_price = theater * int(no_tickets.get()) + (14/100)
        answer.config(text="Price:" + str(the_price) + "\n" + "tickets:"+str(no_tickets.get()) + "\n" + "Number:" + str(num.get()))


class ClsTicketSales:
    def __init__(self, cel, no_tic, price):
        self.cel = cel
        self.no_tic = no_tic
        self.price = price
        return

    btn = Button(window, text="calculate", command=cal, width=20, height=1, bg="blue")
    btn.grid(row=5, column=0)


cell_number.grid(row=0, column=0, sticky=W)
ticket_cat.grid(row=1, column=0, sticky=W)
numbers_ticket.grid(row=2, column=0, sticky=W)
num.grid(row=0, column=1)
tickets.grid(row=1, column=1)
no_tickets.grid(row=2, column=1)

window.mainloop()
