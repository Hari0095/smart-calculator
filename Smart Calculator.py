from tkinter import*
root=Tk()
root.title('Smart Calculator')
root.iconbitmap(r'C:\Users\don\Downloads\favicon.ico')
root.config(bg='#3a3a3a')
root.resizable(False,False)
root.expression=''
input=Entry(root, width=18,borderwidth=0,bg='#3a3a3a',fg='#7DF9FF',font=('Segoe UI',22,'bold'),justify='right')
input.grid(row=0, column=0, columnspan=4,padx=10, pady=10)

def click(num):
    current=input.get()
    input.delete(0,END)
    input.insert(0,str(current)+str(num))

def clear():
    input.delete(0,END)

def equal():
   try:
       result= str(eval(input.get()))
       input.delete(0,END)
       input.insert(0,result)
   except Exception:
       input.delete(0,END)
       input.insert(0,'Error')

def key_press(event):
    key=event.char
    if key in '0123456789+-*/':
        click(key)
    elif event.keysym == 'Return':
        equal()
    elif event.keysym == 'Escape':
        clear()
    elif event.keysym == 'BackSpace':
        current = input.get()
        input.delete(0,END)
        input.delete(0,current[:-1])
        
root.bind('<Key>', key_press)
    

button_0=Button(root, text='0', padx=30, pady=20, relief=RAISED, font=('Segon UI',14),bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(0))
button_1=Button(root, text='1', padx=30, pady=20, relief=RAISED, font=('Segon UI',14), bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(1))
button_2=Button(root, text='2', padx=30, pady=20, relief=RAISED,font=('Segon UI',14), bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(2))
button_3=Button(root, text='3', padx=30, pady=20, relief=RAISED,font=('Segon UI',14), bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(3))
button_4=Button(root, text='4', padx=30, pady=20, relief=RAISED, font=('Segon UI',14), bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(4))
button_5=Button(root, text='5', padx=30, pady=20, relief=RAISED,font=('Segon UI',14), bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(5))
button_6=Button(root, text='6', padx=30, pady=20, relief=RAISED,font=('Segon UI',14), bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(6))
button_7=Button(root, text='7', padx=30, pady=20, relief=RAISED,font=('Segon UI',14), bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(7))
button_8=Button(root, text='8', padx=30, pady=20, relief=RAISED, font=('Segon UI',14), bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(8))
button_9=Button(root, text='9', padx=30, pady=20, relief=RAISED, font=('Segon UI',14), bg='#3a3a3a', fg='white',activebackground='#5a5a5a',activeforeground='white',command=lambda:click(9))
button_add=Button(root, text='+', padx=30.49, pady=20, relief=RAISED, font=('Segon UI',14), bg='#7DF9FF', fg='black',activebackground='lightblue',activeforeground='white',command=lambda:click('+'))
button_sub=Button(root, text='-', padx=32, pady=20, relief=RAISED, font=('Segon UI',14), bg='#7DF9FF', fg='black',activebackground='lightblue',activeforeground='white',command=lambda:click('-'))
button_mul=Button(root, text='X', padx=29, pady=20, relief=RAISED, font=('Segon UI',14), bg='#7DF9FF', fg='black',activebackground='lightblue',activeforeground='white',command=lambda:click('*'))
button_div=Button(root, text='/', padx=33, pady=20, relief=RAISED, font=('Segon UI',14), bg='#7DF9FF', fg='black',activebackground='lightblue',activeforeground='white',command=lambda:click('/'))
button_equal=Button(root, text='=', padx=30, pady=20, relief=RAISED, font=('Segon UI',14),bg='#7DF9FF', fg='black',activebackground='lightblue',activeforeground='white', command=equal)
button_clear=Button(root, text='AC',  padx=22, pady=20, relief=RAISED, font=('Segon UI',14), bg='#7DF9FF', fg='black',activebackground='lightblue',activeforeground='white', command=clear)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)


root.mainloop()
