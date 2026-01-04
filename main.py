from Tkinter import *
import sys

countclk = 0
root = Tk()
perclick = 1
upgmultp = 3
upgcost = 5

def click():
    global countclk
    countclk += perclick
    ccT.config(text=countclk)
    print(countclk)

def exitClk():
    sys.exit()

def upgrade():
    global perclick
    global countclk
    global upgmultp
    global upgcost
    if countclk >= upgcost:
        countclk -= upgcost
        perclick += upgmultp
        upgmultp *= 2
        upgcost *= 2
        ccT.config(text=countclk)
        multpT.config(text='+' + str(upgmultp))
        costT.config(text='-' + str(upgcost))

root['bg'] = '#fafafa'
root.title("Open Clicker")
root.geometry("300x250")
root.wm_attributes('-alpha', 0.9)
root.resizable(width=False, height=False)

ccTT = Label(root, text='Count clicks:')
ccTT.pack()

ccT = Label(root, text=countclk, bg='yellow')
ccT.pack()

clickbutt = Button(root, text='Click me!', command=click)
clickbutt.pack()

upgButt = Button(root, text='Upgrade', bg='green', command=upgrade)
upgButt.pack()

costT = Label(root, text='-' + str(upgcost))
multpT = Label(root, text='+' + str(upgmultp))
costT.pack()
multpT.pack()

quitbutt = Button(root, text='Exit', bg='red', command=exitClk)
quitbutt.pack(side='bottom')

root.mainloop()