import random
import time
import tkinter.messagebox
from tkinter import *
from tkinter import Label

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background='Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle: Label = Label(Tops, font=('arial', 58, 'bold'), text='Restaurant Management System', bd=21, bg='Cadet Blue',
                        fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)

ReceiptCal_F = Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F = Frame(ReceiptCal_F, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F = Frame(ReceiptCal_F, bg='Powder Blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F = Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F = Frame(MenuFrame, bg='Powder Blue', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F = Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F = Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)

# ===========================================Variables==============================================

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Thumbsup = StringVar()
E_Redbull = StringVar()
E_Sevenup = StringVar()
E_Pepsi = StringVar()

E_Thumbsup.set("0")
E_Redbull.set("0")
E_Sevenup.set("0")
E_Pepsi.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))


# ===========================================Function Declaration======================================
def iExit():
    iExit = tkinter.messagebox.askyesno("Exit", "Are you sure?")
    if iExit > 0:
        root.destroy()
        return


def Reset():
    E_Thumbsup.set("0")
    E_Redbull.set("0")
    E_Sevenup.set("0")
    E_pepsi.set("0")

    CostofDrinks.set("0")
    ServiceCharge.set("0")
    SubTotal.set("0")
    PaidTax.set("0")
    TotalCost.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)

    txtThumbsup.configure(state=DISABLED)
    txtRedbull.configure(state=DISABLED)
    txtSevenup.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)

def CostofItem():
    Item1 = float(E_Thumbsup.get())
    Item2 = float(E_Redbull.get())
    Item3 = float(E_Sevenup.get())
    Item4 = float(E_Pepsi.get())

    PriceofDrinks = ((Item1 * 40) + (Item2 * 200) + (Item3 * 40) + (Item4 * 300))

    DrinksPrice = "Rs", str('%.2f' % PriceofDrinks)
    CostofDrinks.set(DrinksPrice)
    SC = "Rs", str('%.2f' % 2.5)
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs", str('%.2f' % (PriceofDrinks + 2.5))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs", str('%.2f' % ((PriceofDrinks + 2.5) * 0.5))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + 2.5) * 0.5)
    TC = "Rs", str('%.2f' % (PriceofDrinks + 2.5 + TT))
    TotalCost.set(TC)


def chkThumbsup():
    if var1.get() == 1:
        txtThumbsup.configure(state=NORMAL)
        txtThumbsup.focus()
        txtThumbsup.delete('0', END)
        E_Thumbsup.set("")
    elif var1.get() == 0:
        txtThumbsup.configure(state=DISABLED)
        E_Thumbsup.set("0")


def chkRedbull():
    if var2.get() == 1:
        txtRedbull.configure(state=NORMAL)
        txtRedbull.focus()
        txtRedbull.delete('0', END)
        E_Redbull.set("")
    elif var2.get() == 0:
        txtRedbull.configure(state=DISABLED)
        E_Redbull.set("0")


def chkSevenup():
    if var3.get() == 1:
        txtSevenup.configure(state=NORMAL)
        txtSevenup.focus()
        txtSevenup.delete('0', END)
        E_Sevenup.set("")
    elif var3.get() == 0:
        txtSevenup.configure(state=DISABLED)
        E_Sevenup.set("0")


def chkPepsi():
    if var4.get() == 1:
        txtPepsi.configure(state=NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0', END)
        E_Pepsi.set("")
    elif var4.get() == 0:
        txtPepsi.configure(state=DISABLED)
        E_Pepsi.set("0")


def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10903, 609235)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + "\t" + DateofOrder.get() + "\n")
    txtReceipt.insert(END, 'Item:\t\t\t' + "No of Items\n")
    txtReceipt.insert(END, 'Thumbsup: \t\t\t\t' + E_Thumbsup.get() + "\n")
    txtReceipt.insert(END, 'Red Bull: \t\t\t\t' + E_Redbull.get() + "\n")
    txtReceipt.insert(END, '7Up: \t\t\t\t' + E_Sevenup.get() + "\n")
    txtReceipt.insert(END, 'Pepsi: \t\t\t\t' + E_Pepsi.get() + "\n")

class funcdeclare:
    def __init__(self):
        pass


obj = funcdeclare()

# ===========================================Drinks===================================================

Thumbsup = Checkbutton(Drinks_F, text='Thumbs Up', variable=var1, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                       , bg="Powder Blue", command=chkThumbsup).grid(row=0, sticky=W)
Redbull = Checkbutton(Drinks_F, text='Red Bull', variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                      , bg="Powder Blue", command=chkRedbull).grid(row=1, sticky=W)
Sevenup = Checkbutton(Drinks_F, text='7 Up', variable=var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                      , bg="Powder Blue", command=chkSevenup).grid(row=2, sticky=W)
Pepsi = Checkbutton(Drinks_F, text='Pepsi', variable=var4, onvalue=1, offvalue=0, font=('arial', 18, 'bold')
                   , bg="Powder Blue", command=chkPepsi).grid(row=3, sticky=W)
# ===========================================Entry Box for Drinks===========================================================

txtThumbsup = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                    textvariable=E_Thumbsup)
txtThumbsup.grid(row=0, column=1)

txtRedbull = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                   textvariable=E_Redbull)
txtRedbull.grid(row=1, column=1)

txtSevenup = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                   textvariable=E_Sevenup)
txtSevenup.grid(row=2, column=1)

txtPepsi = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=E_Pepsi)
txtPepsi.grid(row=3, column=1)

# =======================================================Total Cost====================================================
lblCostofDrinks = Label(Cost_F, font=('arial', 14, 'bold'), text='Cost of Drinks\t', bg='Powder Blue', fg='black')
lblCostofDrinks.grid(row=0, column=0, sticky=W)
txtCostofDrinks = Entry(Cost_F, width=40, bg='white', bd=7, font=('arial', 7, 'bold'), justify=RIGHT,
                        textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0, column=1)

lblServiceCharge = Label(Cost_F, font=('arial', 14, 'bold'), text='Service Charge\t', bg='Powder Blue', fg='black')
lblServiceCharge.grid(row=2, column=0, sticky=W)
lblServiceCharge = Entry(Cost_F, bg='white', width=40, bd=7, font=('arial', 7, 'bold'), justify=RIGHT,
                         textvariable=ServiceCharge)
lblServiceCharge.grid(row=2, column=1)

# =======================================================Payment Information================================================
lblPaidTax = Label(Cost_F, font=('arial', 14, 'bold'), text='\tPaid Tax', bg='Powder Blue', fg='black')
lblPaidTax.grid(row=0, column=2, sticky=W)
txtPaidTax = Entry(Cost_F, width=40, bg='white', bd=7, font=('arial', 7, 'bold'), justify=RIGHT, textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F, font=('arial', 14, 'bold'), text='\tSub Total', bg='Powder Blue', fg='black')
lblSubTotal.grid(row=1, column=2, sticky=W)
txtSubTotal = Entry(Cost_F, width=40, bg='white', bd=7, font=('arial', 7, 'bold'), justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F, font=('arial', 14, 'bold'), text='\tTotal Cost', bg='Powder Blue', fg='black')
lblTotalCost.grid(row=2, column=2, sticky=W)
txtTotalCost = Entry(Cost_F, width=40, bg='white', bd=7, font=('arial', 7, 'bold'), justify=RIGHT,
                     textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)

# =======================================================Receipt============================================================

txtReceipt = Text(Receipt_F, width=46, height=12, bg='white', bd=4, font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)

# =======================================================Buttons============================================================

btnTotal = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                  width=4, text="Total", bg="Powder Blue", command=CostofItem).grid(row=0, column=0)
btnReceipt = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                    width=4, text="Receipt", bg="Powder Blue", command=Receipt).grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                  width=4, text="Reset", bg="Powder Blue", command=Reset).grid(row=0, column=2)
btnExit = Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                 width=4, text="Exit", bg="Powder Blue", command=iExit).grid(row=0, column=3)

root.mainloop()