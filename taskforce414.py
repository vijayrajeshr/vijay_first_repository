from tkinter import*

def onclick():
    given_text=input__1.get()
    print(given_text)
    
root = Tk()

label__text= Label(root,text="\n\tEnter text here :")

input__1=Entry(root,width=100)
input__1.pack()

submit__button= Button(root,text="Submit Button!!!",command=onclick)
submit__button.pack()


root.mainloop()