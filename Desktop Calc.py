from tkinter import*

def iCalc( source, side) :
    storeObj = Frame(source, borderwidth = 4, bd = 4, bg = "powder blue")
    storeObj.pack(side=side, expand=YES, fill =BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app (Frame) :
    def _init_(self):
        Frame._init_(self)
        self.option_add('*Font', 'times new roman 22 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Desktop Calc')

        display = StringVar()
        Entry(self, relief=GROOVE,
                textvariable=display, justify='right', bd=30, bg="powder blue").pack(side=TOP, expand=YES,
                        fill=BOTH)
        for clearBut in (["CE"] , ["C"]):
            erase = iCalc(self,TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))
        
        for Numbut in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for iEquals in NumBut:
                button(FunctionNum, LEFT, iEquals,
                       lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))

        EqualsButton = iCalc(self,BOTTOM)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualsButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                        lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btneiEquals = button(EqualsButton, LEFT, iEquals,
                    lambda storeObj=display, s=' %s'%iEquals: storeOb.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            displa.set("UNDEFINED")
                                
                

if __name__ == '_main_':
    app().mainloop()
