from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkcalendar import *
window=Tk()

#title of the page
window.title("Book your tickets")

# background colour
#window.config(bg="#FFEFDB")

# setting the window in center screen
#w=500
#h=500
#sw=window.winfo_screenwidth()
#sh=window.winfo_screenheight()
#x=(sw/2)-w/2
#y=(sh/2)-h/2
#window.geometry("%dx%d+%d+%d"%(w,h,sw,sh))
window.geometry("1366x738")

busno=Label(window,text="90A",font=("Helvetica",30,"bold"),fg="black",bg="grey")
busno.pack(pady=100)

#creating icon
window.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")

#creating menu bar
def place():
    n4=Toplevel(window)
    n4.geometry("1366x738")
    n4.title("Book your tickets")
    n4.config(bg="grey")
    n4.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")
    p=Label(n4,font=("Helvetica",25,"bold"),bg="grey",fg="black",text="Gandhipuram \n Saibaba colony \n Thottipalayam \n R.S puram \n Ramnagar \n Lakshmi Mills \n Hopes College \n Neelambur \n Sitra-Airport")
    p.pack(pady=130)
def time():
    n5=Toplevel(window)
    n5.geometry("1366x738")
    n5.title("Book your tickets")
    n5.config(bg="grey")
    n5.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")

def about():
    n6=Toplevel(window)
    n6.geometry("1366x738")
    n6.title("Book your tickets")
    n6.config(bg="grey")
    n6.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")


    #inserting image
    image1 = Image.open(r"C:\Users\admin\Downloads\safety.jpg")
    re= image1.resize((230,230))
    test = ImageTk.PhotoImage(re)

    label1 =Label(n6,image=test)
    label1.image = test

    # Position image
    label1.place(x=40, y=10)
   
    safe=Label(n6,text="\n\nSAFTY \n extra efforts to ensure safty\n\n\n\n ",font=("Helvetica",25,"bold"),bg="grey",fg="black")
    safe.pack(padx=60)

    #inserting image
    image1 = Image.open(r"C:\Users\admin\Downloads\time.png")

    re= image1.resize((230,230))
    test = ImageTk.PhotoImage(re)

    label1 =Label(n6,image=test)
    label1.image = test

    # Position image
    label1.place(x=40, y=300)
   
    time=Label(n6,text="ON TIME \n Our bus has proven track\n record of regularly being on time\n\n\n\n",font=("Helvetica",25,"bold"),bg="grey",fg="black")
    time.pack(padx=60)

    #inserting image
    image1 = Image.open(r"C:\Users\admin\Downloads\seat.png")

    re= image1.resize((230,230))
    test = ImageTk.PhotoImage(re)

    label1 =Label(n6,image=test)
    label1.image = test

    # Position image
    label1.place(x=40, y=600)
   
    comfort=Label(n6,text="COMFORTABLE \n Our bus stands for comfort\n and best in class service experience",font=("Helvetica",25,"bold"),bg="grey",fg="black")
    comfort.pack(padx=60)
   
def review():
    def close():
        n7.destroy()
    def sub():
        n8=Toplevel(n7)
        n8.geometry("1366x738")
        n8.title("Book your tickets")
        n8.config(bg="grey")
        n8.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")

        l=Label(n8,text="Thanks for your review",font=("Helvetica",50,"bold"),bg="grey",fg="black")
        l.pack(pady=300)
        #bc=Button(n8,text="Close",command=n8.destroy(),font=("Helvetica",30,"bold"),bg="grey",fg="black",padx=10,pady=10,activebackground="grey",activeforeground="white",width=5,height=1)
        #bc.pack(pady=5)
        if(c1.get()==1):
            a=m.cget("text")
            #messagebox.showinfo(n7,a)
        elif(c1.get()==2):
            a=m1.cget("text")
            #messagebox.showinfo(n7,a)
        elif(c1.get()==3):
            a=m1.cget("text")
            #messagebox.showinfo(n7,a)
        else:
            a=m1.cget("text")
            #messagebox.showinfo(n7,a)
    n7=Toplevel(window)
    n7.geometry("1366x738")
    n7.title("Book your tickets")
    n7.config(bg="grey")
    n7.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")
    l=Label(n7,text="How was your travell experience?",font=("Helvetica",50,"bold"),bg="grey",fg="black",activebackground="grey",activeforeground="black")
    l.pack(pady=50)
    c1=IntVar()
    m=Radiobutton(n7,text="Very good",state="active",font=("Helevetica",30,"bold"),bg="grey",fg="black",variable=c1,value=1)
    m.pack(pady=10)
    m1=Radiobutton(n7,text="Good     ",state="active",font=("Helvetica",30,"bold"),bg="grey",fg="black",variable=c1,value=2)
    m1.pack(pady=10)
    m2=Radiobutton(n7,text="Bad      ",state="active",font=("Helvetica",30,"bold"),bg="grey",fg="black",variable=c1,value=3)
    m2.pack(pady=10)
    m3=Radiobutton(n7,text="Very bad",state="active",font=("Helvetica",30,"bold"),bg="grey",fg="black",variable=c1,value=4)
    m3.pack(pady=10)

    b=Button(n7,text="Submit",command=sub,font=("Helvetica",30,"bold"),bg="grey",fg="black",padx=10,pady=10,activebackground="grey",activeforeground="white",width=5,height=1)
    #b.grid(row=3,column=3)
    b.pack(pady=10)
    b1=Button(n7,text="Close",command=close,font=("Helvetica",30,"bold"),bg="grey",fg="black",padx=10,pady=10,activebackground="grey",activeforeground="white",width=5,height=1)
    #b1.grid(row=3,column=4)
    b1.pack(pady=10)
menubar=Menu(window)
businfo=Menu(menubar,tearoff=0)
businfo.add_command(label="places",command=place)
businfo.add_separator()
#businfo.add_command(label="timming",command=time)
#businfo.add_separator()
businfo.add_command(label="Exit",command=window.destroy)
menubar.add_cascade(label="Bus info",menu=businfo)
window.config(menu=menubar)
menubar.add_cascade(label="About",command=about)
menubar.add_cascade(label="Reviews",command=review)
menubar.add_cascade(label="Exit",command=window.destroy)


#fuction for button "Click here to book tickets"
def bookticket():
    n=Toplevel(window)
    n.geometry("1366x738")
    n.title("Book your tickets")
    n.config(bg="grey")
    n.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")


    #label from
    l=Label(n,text="From",font=("Helvetica",50,"bold"),bg="grey",fg="black")
    l.pack(pady=10)

    #entry box for from
    a=StringVar()
    from_entry=Entry(n,width=110,textvariable=a)
    from_entry.pack(pady=10)

   

    def update(f):
        from_listbox.delete(0,END)
        for i in f:
            from_listbox.insert(END,i)
    def fill(event):
        from_entry.delete(0,END)
        i=from_listbox.curselection()
        a1=from_listbox.get(ANCHOR)
        a.set(a1)
    def check(event):
        typed=from_entry.get()
        if typed=="":
            data=f
        else:
            data=[]
            for i in f:
                if typed.lower()== i.lower():
                    data.append(i)
        update(data)
       

    #list box for from
    from_listbox=Listbox(n,width=110)
    from_listbox.pack(pady=10)

    f=['Gandhipuram','Saibaba colony','Thottipalayam','R.S puram','Ramnagar']
    update(f)

    from_listbox.bind("<<ListboxSelect>>",fill)
    from_entry.bind("<KeyRelease>",check)

    #to
    #label to
    l2=Label(n,text="To",font=("Helvetica",50,"bold"),bg="grey",fg="black")
    l2.pack(pady=10)

    #entry box for to
    x=StringVar()
    to_entry=Entry(n,width=110,textvariable=x)
    to_entry.pack(pady=10)

   

    def update_to(f):
        to_listbox.delete(0,END)
        for index in f:
            to_listbox.insert(END,index)
    def fill_to(event):
        to_entry.delete(0,END)
        index=to_listbox.curselection()
        a3=to_listbox.get(ANCHOR)
        x.set(a3)
    def check_to(event):
        typed_to=to_entry.get()
        if typed_to=="":
            data_to=f
        else:
            data_to=[]
            for i in f:
                if typed_to.lower()== i.lower():
                    data_to.append(i)
        update_to(data_to)
       

    #list box for to
    to_listbox=Listbox(n,width=110)
    to_listbox.pack(pady=10)

    f=['Lakshmi Mills','Hopes College','Neelambur','Sitra-Airport']
    update_to(f)

    to_listbox.bind("<<ListboxSelect>>",fill_to)
    to_entry.bind("<KeyRelease>",check_to)

    def ok_place():
        _from=from_entry.get()
        to= to_entry.get()
        if _from=="" or to=="" :
            messagebox.showinfo("","Kidly select from and to ")
        else:
            n1=Toplevel(n)
            n1.geometry("1366x738")
            n1.title("Book your tickets")
            n1.config(bg="grey")
            n1.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")


            #label When
            #date_label=Label(n1,text="When?",font=("Helvetica",50,"bold"),bg="grey",fg="black")
            #date_label.pack(pady=20)
           
            #function fo date
            def mycal():
                #messagebox for date
                messagebox.showinfo("Date",cal.get_date())
                #page 4
                n2=Toplevel(n)
                n2.geometry("1366x738")
                n2.title("Book your tickets")
                n2.config(bg="grey")
                n2.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")

                #label for number of people
                ppl_label=Label(n2,text="Choose the number of tickets",font=("Helvetica",50,"bold"),bg="grey",fg="black")
                ppl_label.pack(pady=30)
                #spinbox for no. of tickets
                spinbox=Spinbox(n2,from_=1,to=100,width=100)
                spinbox.pack(pady=20)
                # function for no. of ppl
                def ppl():
                    sb=spinbox.get()
                    messagebox.showinfo("Tickets","Your booking "+sb+" tickets")
                    n3=Toplevel(n)
                    n3.geometry("1366x738")
                    n3.title("Book your tickets")
                    n3.config(bg="grey")
                    n3.iconbitmap(r"C:\Users\admin\Downloads\bus-stop.ico")

                    #frame for bill
                    f=Frame(n3,highlightbackground="black",highlightthickness=5,bg="grey",padx=90,pady=50)
                    f.pack(padx=10,pady=10)
                    #label for from
                    from_label=Label(f,text="From: "+from_entry.get(),font=("Helvetica",30,"bold"),bg="grey",fg="black")
                    from_label.pack(pady=30)
                    #label for to
                    to_label=Label(f,text="To: "+to_entry.get(),font=("Helvetica",30,"bold"),bg="grey",fg="black")
                    to_label.pack(pady=30)
                    #label for date
                    date_label=Label(f,text="Date: "+cal.get_date(),font=("Helvetica",30,"bold"),bg="grey",fg="black")
                    date_label.pack(pady=30)
                    #label for no of tickets
                    ppl_label=Label(f,text="Number of tickets: "+spinbox.get(),font=("Helvetica",30,"bold"),bg="grey",fg="black")
                    ppl_label.pack(pady=30)
                   
                    #label for total amount
                    amount_label=Label(f,text="Total amount: ",font=("Helvetica",30,"bold"),bg="grey",fg="black")
                    amount_label.pack(pady=30)
                    np=int(spinbox.get())
                    if from_entry.get()== "Gandipuram" and to_entry.get()== "Lakshmi Mills" :
                        amount_label.config(text="Total amount: "+str (15*np))
                    if from_entry.get()== "Gandhipuram" and to_entry.get()== "Hopes College" :
                        amount_label.config(text="Total amount: "+str (20*np))
                    if from_entry.get()== "Gandhipuram" and to_entry.get()== "Neelambur" :
                        amount_label.config(text="Total amount: "+str (25*np))
                    if from_entry.get()== "Gandhipuram" and to_entry.get()== "Sitra-Airport" :
                        amount_label.config(text="Total amount: "+str (30*np))
                    if from_entry.get()== "Saibaba Colony" and to_entry.get()== "Lakshmi Mills" :
                        amount_label.config(text="Total amount: "+str (35*np))
                    if from_entry.get()== "Saibaba Colony" and to_entry.get()== "Hopes College" :
                        amount_label.config(text="Total amount: "+str (40*np))
                    if from_entry.get()== "Saibaba Colony" and to_entry.get()== "Neelambur" :
                        amount_label.config(text="Total amount: "+str (45*np))
                    if from_entry.get()== "Saibaba Colony" and to_entry.get()== "Sitra-Airport" :
                        amount_label.config(text="Total amount: "+str (50*np))
                    if from_entry.get()== "Thottipalayam" and to_entry.get()== "Lakshmi Mills" :
                        amount_label.config(text="Total amount: "+str (10*np))
                    if from_entry.get()== "Thottipalayam" and to_entry.get()== "Hopes College" :
                        amount_label.config(text="Total amount: "+str (15*np))
                    if from_entry.get()== "Thottipalayam" and to_entry.get()== "Neelambur" :
                        amount_label.config(text="Total amount: "+str (20*np))
                    if from_entry.get()== "Thottipalayam" and to_entry.get()== "Sitra-Airport" :
                        amount_label.config(text="Total amount: "+str (25*np))
                    if from_entry.get()== "R.S Puram" and to_entry.get()== "Lakshmi Mills" :
                        amount_label.config(text="Total amount: "+str (30*np))
                    if from_entry.get()== "R.S Puram" and to_entry.get()== "Hopes College" :
                        amount_label.config(text="Total amount: "+str (35*np))
                    if from_entry.get()== "R.S Puram" and to_entry.get()== "Neelambur" :
                        amount_label.config(text="Total amount: "+str (40*np))
                    if from_entry.get()== "R.S Puram" and to_entry.get()== "Sitra-Airport" :
                        amount_label.config(text="Total amount: "+str (45*np))
                    if from_entry.get()== "Ramnagar" and to_entry.get()== "Lakshmi Mills" :
                        amount_label.config(text="Total amount: "+str (50*np))
                    if from_entry.get()== "Ramnagar" and to_entry.get()== "Hopes College" :
                        amount_label.config(text="Total amount: "+str (40*np))
                    if from_entry.get()== "Ramnagar" and to_entry.get()== "Neelambur" :
                        amount_label.config(text="Total amount: "+str (50*np))
                    if from_entry.get()== "Ramnagar" and to_entry.get()== "Sitra-Airport" :
                        amount_label.config(text="Total amount: "+str (50*np))
                    #functon for payment
                    def pay():
                        pass

                    #button for payment
                    pay=Button(n3,text="Proceed to pay",font=("Helvetica",30,"bold"),bg="grey",fg="black",padx=10,pady=10,activebackground="grey",activeforeground="white",command=pay)
                    pay.pack(pady=30)    
                #button for ok (no. of ppl)
                ppl_button=Button(n2,text="Ok",font=("Helvetica",30,"bold"),bg="grey",fg="black",padx=10,pady=10,activebackground="grey",activeforeground="white",command=ppl)
                ppl_button.pack(pady=10)
                
            #label for when?
            lw=Label(n1,text="When?",font=("Helvetica",30,"bold"),bg="grey",fg="black")
            lw.pack(pady=40)       
            #calendar
            cal=Calendar(n1,selectionmode="day",year=2023,month=2,day=6,cursor="hand1",date_pattern="dd/MM/yyyy",padx=100,pady=100)
            cal.pack(pady=70)
                                       
             #button for calendar ok button
            ok_date=Button(n1,text="Ok",font=("Helvetica",30,"bold"),bg="grey",fg="black",padx=10,pady=10,activebackground="grey",activeforeground="white",command=mycal)
            ok_date.pack(pady=30)
           
       

    #button for ok
    ok_button=Button(n,text="Ok",font=("Helvetica",30,"bold"),bg="grey",fg="black",padx=10,pady=10,activebackground="grey",activeforeground="white",command=ok_place,width=5,height=1)
    ok_button.pack(pady=10)
   
   
   


#label
#l=Label(window,text="90A",font=("Helvetica",30,"bold"),fg="black",bg="grey")
#l=Label(window,text="Experience the joy of travelling ",font=("French Script MT",50,"bold"),bg="#FFEFDB",fg="#CD3333")
#l.pack(pady=300)

#button for booking ticket
b=Button(window,text="Click here to book tickets",font=("Helvetica",30,"bold"),fg="black",bg="grey",padx=10,pady=10,activebackground="white",activeforeground="grey",command=bookticket)
b.pack(pady=200)
window.mainloop()

