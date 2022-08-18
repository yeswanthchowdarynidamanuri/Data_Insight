#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import tkinter as tk
import time
import datetime
import random
from tkinter import messagebox

root =Tk()
root.geometry("1800x770+1+0")
root.title("DONE BY YESWANTH CHOWDARY")
root.configure(background='green')

Tops = Frame(root,bg='green',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('Algerian',50,'bold'),text='RESTAURANT BILLING SYSTEM',bd=21,bg='yellow',
                fg='black',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='green',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='green',bd=5,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

#==========Customers Frame==========#
F1 = LabelFrame(root,text = "Details",font = ("time new roman",12,"bold"),fg = "white",bg = "green",bd = 8,relief=RIDGE)
F1.pack(side=TOP)

#===============Customer Name===========#

cname_lbl = Label(F1,text="Table Number",bg = "green",fg = "white",font=("aria",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)

Receipt_F=Frame(ReceiptCal_F,bg='green',bd=6,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='green',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='green',bd=6)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg='green',bd=6)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='green',bd=6,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='green',bd=6,relief=RIDGE)
Food_F.pack(side=RIGHT)
###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()
cus_name = StringVar()

text_Input = StringVar()
operator = ""

E_Sprite = StringVar()
E_Pepsi = StringVar()
E_DietCoke = StringVar()
E_Mojito = StringVar()
E_Cappuccino = StringVar()
E_Fanta = StringVar()
E_CocaCola = StringVar()
E_ColdCoffee = StringVar()

E_HotDog = StringVar()
E_VegBurger = StringVar()
E_Pasta = StringVar()
E_HamBurger = StringVar()
E_Sandwich = StringVar()
E_Fires = StringVar()
E_Spagetti = StringVar()
E_Fazitas = StringVar()

E_Sprite.set("0")
E_Pepsi.set("0")
E_DietCoke.set("0")
E_Mojito.set("0")
E_Cappuccino.set("0")
E_Fanta.set("0")
E_CocaCola.set("0")
E_ColdCoffee.set("0")

E_HotDog.set("0")
E_VegBurger.set("0")
E_Pasta.set("0")
E_HamBurger.set("0")
E_Sandwich.set("0")
E_Fires.set("0")
E_Spagetti.set("0")
E_Fazitas.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))
cus_name = StringVar()

##########################################Function Declaration####################################################

def iExit():
    root.destroy()

def jExit():
    root.destroy()

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_DietCoke.set("0")
    E_Mojito.set("0")
    E_Cappuccino.set("0")
    E_Fanta.set("0")
    E_CocaCola.set("0")
    E_ColdCoffee.set("0")

    E_HotDog.set("0")
    E_VegBurger.set("0")
    E_Pasta.set("0")
    E_HamBurger.set("0")
    E_Sandwich.set("0")
    E_Fires.set("0")
    E_Spagetti.set("0")
    E_Fazitas.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtSprite.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtDietCoke.configure(state=DISABLED)
    txtMojito.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtFanta.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtColdCoffee.configure(state=DISABLED)
    txtHotDog.configure(state=DISABLED)
    txtVegBurger.configure(state=DISABLED)
    txtPasta.configure(state=DISABLED)
    txtHamBurger.configure(state=DISABLED)
    txtSandwich.configure(state=DISABLED)
    txtFires.configure(state=DISABLED)
    txtSpagetti.configure(state=DISABLED)
    txtFazitas.configure(state=DISABLED)

def menu():
    from tkinter import messagebox
    roo = Tk()
    roo.geometry("600x600+0+0")
    roo.title("MENU")
    roo.configure(background='green')
    
    lblinfo = Label(roo, font=('aria', 18, 'bold'), text="DRINKS\t\t", fg="yellow",bg='green', bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="                 ", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 18, 'bold'), text="PRICE", fg="yellow",bg='green', anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SPRITE\t\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="65", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PEPSI\t\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="75", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="DIET COKE\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="99", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="MOJITO\t\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="130", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="CAPPUCCINO\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="180", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="FANTA\t\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="75", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="COCO-COLA\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="75", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=7, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="COLD-COFFEE\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="89", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=8, column=3)
    
    lblinfo = Label(roo, font=('aria', 18, 'bold'), text="FOOD\t\t", fg="yellow",bg='green', bd=5)
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="                 ", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=10, column=2)
    lblinfo = Label(roo, font=('aria', 18, 'bold'), text="PRICE", fg="yellow",bg='green', anchor=W)
    lblinfo.grid(row=10, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="HOT-DOG\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=11, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="260", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=11, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="VEG-BURGER\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=12, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="175", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=12, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PASTA\t\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=13, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="225", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=13, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="HAMBURGER\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=14, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="480", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=14, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SANDWICH\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=15, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="240", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=15, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="FRIES\t\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=16, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="110", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=16, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SPAGETTI\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=17, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="340", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=17, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="FAZITAS\t\t", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=18, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="210", fg="white",bg='green', anchor=W)
    lblinfo.grid(row=18, column=3)
    
    
    roo.mainloop()

def CostofItem():
    Item1=float(E_Sprite.get())
    Item2=float(E_Pepsi.get())
    Item3=float(E_DietCoke.get())
    Item4=float(E_Mojito.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_Fanta.get())
    Item7=float(E_CocaCola.get())
    Item8=float(E_ColdCoffee.get())

    Item9=float(E_HotDog.get())
    Item10=float(E_VegBurger.get())
    Item11=float(E_Pasta.get())
    Item12=float(E_HamBurger.get())
    Item13=float(E_Sandwich.get())
    Item14=float(E_Fires.get())
    Item15=float(E_Spagetti.get())
    Item16=float(E_Fazitas.get())

    PriceofDrinks =(Item1 * 65) + (Item2 * 75) + (Item3 * 99) + (Item4 * 130) + (Item5 * 180) + (Item6 * 75) + (Item7 * 75) + (Item8 * 89)

    PriceofFood =(Item9 * 260) + (Item10 * 175) + (Item11 * 255) + (Item12 * 480) + (Item13 * 240) + (Item14 * 110) + (Item15 * 340) + (Item16 * 210)



    DrinksPrice = "Rs",str('%.2f'%(PriceofDrinks))
    FoodPrice =  "Rs",str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Rs",str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs",str('%.2f'%((PriceofDrinks + PriceofFood + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood + 1.59) * 0.15)
    TC="Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59 + TT))
    TotalCost.set(TC)


def chkSprite():
    if(var1.get() == 1):
        txtSprite.configure(state = NORMAL)
        txtSprite.focus()
        txtSprite.delete('0',END)
        E_Sprite.set("")
    elif(var1.get() == 0):
        txtSprite.configure(state = DISABLED)
        E_Sprite.set("0")

def chkPepsi():
    if(var2.get() == 1):
        txtPepsi.configure(state = NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0',END)
        E_Pepsi.set("")
    elif(var2.get() == 0):
        txtPepsi.configure(state = DISABLED)
        E_Pepsi.set("0")

def chk_DietCoke():
    if(var3.get() == 1):
        txtDietCoke.configure(state = NORMAL)
        txtDietCoke.delete('0',END)
        txtDietCoke.focus()
    elif(var3.get() == 0):
        txtDietCoke.configure(state = DISABLED)
        E_DietCoke.set("0")

def chk_Mojito():
    if(var4.get() == 1):
        txtMojito.configure(state = NORMAL)
        txtMojito.delete('0',END)
        txtMojito.focus()
    elif(var4.get() == 0):
        txtMojito.configure(state = DISABLED)
        E_Mojito.set("0")

def chk_Cappuccino():
    if(var5.get() == 1):
        txtCappuccino.configure(state = NORMAL)
        txtCappuccino.delete('0',END)
        txtCappuccino.focus()
    elif(var5.get() == 0):
        txtCappuccino.configure(state = DISABLED)
        E_Cappuccino.set("0")

def chk_Fanta():
    if(var6.get() == 1):
        txtFanta.configure(state = NORMAL)
        txtFanta.delete('0',END)
        txtFanta.focus()
    elif(var6.get() == 0):
        txtFanta.configure(state = DISABLED)
        E_Fanta.set("0")

def chk_CocaCola():
    if(var7.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.delete('0',END)
        txtCocaCola.focus()
    elif(var7.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        E_CocaCola.set("0")

def chk_ColdCoffee():
    if(var8.get() == 1):
        txtColdCoffee.configure(state = NORMAL)
        txtColdCoffee.delete('0',END)
        txtColdCoffee.focus()
    elif(var8.get() == 0):
        txtColdCoffee.configure(state = DISABLED)
        E_ColdCoffee.set("0")

def chk_HotDog():
    if(var9.get() == 1):
        txtHotDog.configure(state = NORMAL)
        txtHotDog.delete('0',END)
        txtHotDog.focus()
    elif(var9.get() == 0):
        txtHotDog.configure(state = DISABLED)
        E_HotDog.set("0")

def chk_VegBurger():
    if(var10.get() == 1):
        txtVegBurger.configure(state = NORMAL)
        txtVegBurger.delete('0',END)
        txtVegBurger.focus()
    elif(var10.get() == 0):
        txtVegBurger.configure(state = DISABLED)
        E_VegBurger.set("0")

def chk_Pasta():
    if(var11.get() == 1):
        txtPasta.configure(state = NORMAL)
        txtPasta.delete('0',END)
        txtPasta.focus()
    elif(var11.get() == 0):
        txtPasta.configure(state = DISABLED)
        E_Pasta.set("0")

def chk_HamBurger():
    if(var12.get() == 1):
        txtHamBurger.configure(state = NORMAL)
        txtHamBurger.delete('0',END)
        txtHamBurger.focus()
    elif(var12.get() == 0):
        txtHamBurger.configure(state = DISABLED)
        E_HamBurger.set("0")

def chk_Sandwich():
    if(var13.get() == 1):
        txtSandwich.configure(state = NORMAL)
        txtSandwich.delete('0',END)
        txtSandwich.focus()
    elif(var13.get() == 0):
        txtSandwich.configure(state = DISABLED)
        E_Sandwich.set("0")

def chk_Fires():
    if(var14.get() == 1):
        txtFires.configure(state = NORMAL)
        txtFires.delete('0',END)
        txtFires.focus()
    elif(var14.get() == 0):
        txtFires.configure(state = DISABLED)
        E_Fires.set("0")

def chk_Spagetti():
    if(var15.get() == 1):
        txtSpagetti.configure(state = NORMAL)
        txtSpagetti.delete('0',END)
        txtSpagetti.focus()
    elif(var15.get() == 0):
        txtSpagetti.configure(state = DISABLED)
        E_Spagetti.set("0")

def chk_Fazitas():
    if(var16.get() == 1):
        txtFazitas.configure(state = NORMAL)
        txtFazitas.delete('0',END)
        txtFazitas.focus()
    elif(var16.get() == 0):
        txtFazitas.configure(state = DISABLED)
        E_Fazitas.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(1,50000)
    randomRef= str(x)
    Receipt_Ref.set(randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t'+Receipt_Ref.get() +'\t\tDate: '+ DateofOrder.get() + "\t\t\tTable Number: "+cus_name.get()+'\n')
    txtReceipt.insert(END,'=================================================================='+'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Number of Items \n")
    txtReceipt.insert(END,'=================================================================='+'\n')
    if (E_Sprite.get() != "0"):
        txtReceipt.insert(END,'Sprite:\t\t\t\t\t' + E_Sprite.get() +'\n')
    if (E_Pepsi.get() != "0"):
        txtReceipt.insert(END,'Pepsi:\t\t\t\t\t'+ E_Pepsi.get()+'\n')
    if (E_DietCoke.get() != "0"):
        txtReceipt.insert(END,'DietCoke:\t\t\t\t\t'+ E_DietCoke.get()+'\n')
    if (E_Mojito.get() != "0"):
        txtReceipt.insert(END,'Mojito:\t\t\t\t\t'+ E_Mojito.get()+'\n')
    if (E_Cappuccino.get() != "0"):
        txtReceipt.insert(END,'Cappuccino:\t\t\t\t\t'+ E_Cappuccino.get()+'\n')
    if (E_Fanta.get()!="0"):
        txtReceipt.insert(END,'Fanta:\t\t\t\t\t'+ E_Fanta.get()+'\n')
    if (E_CocaCola.get()!="0"):
        txtReceipt.insert(END,'CocaCola:\t\t\t\t\t'+ E_CocaCola.get()+'\n')
    if (E_ColdCoffee.get()!="0"):
        txtReceipt.insert(END,'ColdCoffee:\t\t\t\t\t'+ E_ColdCoffee.get()+'\n')
    if (E_HotDog.get()!="0"):
        txtReceipt.insert(END,'HotDog:\t\t\t\t\t'+ E_HotDog.get()+'\n')
    if (E_VegBurger.get()!="0"):
        txtReceipt.insert(END,'VegBurger:\t\t\t\t\t'+ E_VegBurger.get()+'\n')
    if (E_Pasta.get()!="0"):
        txtReceipt.insert(END,'Pasta:\t\t\t\t\t'+ E_Pasta.get()+'\n')
    if (E_HamBurger.get()!="0"):
        txtReceipt.insert(END,'HamBurger:\t\t\t\t\t'+ E_HamBurger.get()+'\n')
    if (E_Sandwich.get()!="0"):
        txtReceipt.insert(END,'Sandwich:\t\t\t\t\t'+ E_Sandwich.get()+'\n')
    if (E_Fires.get()!="0"):
        txtReceipt.insert(END,'Fries:\t\t\t\t\t'+ E_Fires.get()+'\n')
    if (E_Spagetti.get()!="0"):
        txtReceipt.insert(END,'Spagetti:\t\t\t\t\t'+ E_Spagetti.get()+'\n')
    if (E_Fazitas.get()!="0"):
        txtReceipt.insert(END,'Fazitas:\t\t\t\t\t'+ E_Fazitas.get()+'\n')
    txtReceipt.insert(END,'=================================================================='+'\n')
    txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t'+CostofDrinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Foods:\t\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+"\n")
    txtReceipt.insert(END,'=================================================================='+'\n')
    txtReceipt.insert(END,'Total Cost:\t\t\t\t'+str(TotalCost.get())+"\n")
    txtReceipt.insert(END,'==========================THANKYOU FOR VISITING================='+'\n')

cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = cus_name)
cname_en.grid(row = 0,column = 1,ipady = 2,ipadx = 20,pady = 5)
#########################################Drinks####################################################################
Sprite=Checkbutton(Drinks_F,text='Sprite\t\t\t',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='green',command=chkSprite).grid(row=0,sticky=W)
Pepsi=Checkbutton(Drinks_F,text='Pepsi',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='green',command=chkPepsi).grid(row=1,sticky=W)
DietCoke=Checkbutton(Drinks_F,text='Diet-Coke',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='green',command=chk_DietCoke).grid(row=2,sticky=W)
Mojito=Checkbutton(Drinks_F,text='Mojito',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='green',command=chk_Mojito).grid(row=3,sticky=W)
Cappuccino=Checkbutton(Drinks_F,text='Cappuccino',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='green',command=chk_Cappuccino).grid(row=4,sticky=W)
Fanta=Checkbutton(Drinks_F,text='Fanta',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='green',command=chk_Fanta).grid(row=5,sticky=W)
CocaCola=Checkbutton(Drinks_F,text='Coca-Cola',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='green',command=chk_CocaCola).grid(row=6,sticky=W)
ColdCoffee=Checkbutton(Drinks_F,text='Cold-Coffee',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='green',command=chk_ColdCoffee).grid(row=7,sticky=W)
##############################################Drink Entry###############################################################



txtSprite = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Sprite)
txtSprite.grid(row=0,column=1)

txtPepsi = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Pepsi)
txtPepsi.grid(row=1,column=1)

txtDietCoke = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_DietCoke)
txtDietCoke.grid(row=2,column=1)

txtMojito= Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Mojito)
txtMojito.grid(row=3,column=1)

txtCappuccino = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Cappuccino)
txtCappuccino.grid(row=4,column=1)

txtFanta = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Fanta)
txtFanta.grid(row=5,column=1)

txtCocaCola = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_CocaCola)
txtCocaCola.grid(row=6,column=1)

txtColdCoffee = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_ColdCoffee)
txtColdCoffee.grid(row=7,column=1)
#############################################Foods######################################################################

HotDog = Checkbutton(Food_F,text="Hot Dog\t\t\t ",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='green',command=chk_HotDog).grid(row=0,sticky=W)
VegBurger = Checkbutton(Food_F,text="Veg-Burger",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='green',command=chk_VegBurger).grid(row=1,sticky=W)
Pasta = Checkbutton(Food_F,text="Pasta ",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='green',command=chk_Pasta).grid(row=2,sticky=W)
HamBurger = Checkbutton(Food_F,text="Rice Plate ",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='green',command=chk_HamBurger).grid(row=3,sticky=W)
Sandwich = Checkbutton(Food_F,text="Sandwich ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='green',command=chk_Sandwich).grid(row=4,sticky=W)
Fires = Checkbutton(Food_F,text="Fries ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='green',command=chk_Fires).grid(row=5,sticky=W)
Spagetti = Checkbutton(Food_F,text="Spagetti ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='green',command=chk_Spagetti).grid(row=6,sticky=W)
Fazitas = Checkbutton(Food_F,text="Fazitas ",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='green',command=chk_Fazitas).grid(row=7,sticky=W)
################################################Entry Box For Cake##########################################################
txtHotDog=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_HotDog)
txtHotDog.grid(row=0,column=1)

txtVegBurger=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_VegBurger)
txtVegBurger.grid(row=1,column=1)

txtPasta=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Pasta)
txtPasta.grid(row=2,column=1)

txtHamBurger=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_HamBurger)
txtHamBurger.grid(row=3,column=1)

txtSandwich=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Sandwich)
txtSandwich.grid(row=4,column=1)

txtFires=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Fires)
txtFires.grid(row=5,column=1)

txtSpagetti=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Spagetti)
txtSpagetti.grid(row=6,column=1)

txtFazitas=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Fazitas)
txtFazitas.grid(row=7,column=1)
###########################################ToTal Cost################################################################################
lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Drinks\t',bg='green',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='yellow',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Foods  ',bg='green',
                fg='black',justify=CENTER)
lblCostofFood.grid(row=1,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='yellow',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='green',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='yellow',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
###########################################################Payment information###################################################

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text=' Paid Tax\t\t',bg='green',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='yellow',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text=' Sub Total',bg='green',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='yellow',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text=' Total',bg='green',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='yellow',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(Receipt_F,width=66,height=21,bg='yellow',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)


###########################################BUTTONS################################################################################
btnprice=Button(Buttons_F,padx=26,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='MENU',
                        bg='green',command=menu).grid(row=0,column=0)
btnTotal=Button(Buttons_F,padx=26,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='TOTAL',
                        bg='green',command=CostofItem).grid(row=0,column=1)
btnReceipt=Button(Buttons_F,padx=26,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='BILL',
                        bg='green',command=Receipt).grid(row=0,column=2)
btnReset=Button(Buttons_F,padx=26,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='RESET',
                        bg='green',command=Reset).grid(row=0,column=3)
btnExit=Button(Buttons_F,padx=26,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='EXIT',
                        bg='green',command=iExit).grid(row=0,column=4)






root.mainloop()


# In[ ]:





# In[ ]:




