from tkinter import *
root=Tk()
root.title("Multi-Dimensionala Arrays")
root.geometry("500x500")

arry_1d=["Watermelon","Strawberry","Grapes","Dragon Fruit","Lychee","Blueberry","Apple"]
print(arry_1d)
print(arry_1d[2])
print(arry_1d[4])

arry_2d=[["English","A*"],["Math","A"],["Bio","B"],["EM","F"]]
print(arry_2d)
print(arry_2d[1])
print(arry_2d[1][0])

print(arry_2d[2])
print(arry_2d[3][1])

root.mainloop()