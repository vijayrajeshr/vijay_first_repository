#calculator
from tkinter import*

def onclick__addition():
    n1=int(input__1.get())
    n2=int(input__2.get())
    ans=n1+n2
    print(ans)
       

root=Tk()

Label__1=Label(root,text="Enter first integer  : ").pack()
input__1=Entry(root,width=45)

Label__2=Label(root,text="Enter second integer : ").pack()
input__2=Entry(root,width=45)

input__1.pack()
input__2.pack()

add_button=Button(root,text="ADD",command=onclick__addition)
add_button.pack()

#Label__answer=Label(root,text=" ANSWER = ")
#Label__answer.pack()

root.mainloop()