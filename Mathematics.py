from tkinter import * 

root= Tk()

root.title("Fibonacii")

root.geometry("400x400")

textbox=Entry(root)

label= Label(root, text="Fibonacii Series : ")

label2= Label(root, text="Fibonacii Sum : ")

def fibonacii():
    num=textbox.get()
    first_no=0
    second_no=1
    sum=0
    sum2=0
    i=1
    while(i <= int(num)):
        label["text"] += str(sum)+" "
        label2["text"] = "Fibonacii Series Sum : " + str(sum2)
        i=i+1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum

        

        
btn=Button(root, text="Show Fibonacii Series", command=fibonacii)


textbox.pack()


btn.pack()


label.pack()



label2.pack()

root.mainloop()