from tkinter import *

mainWindow = Tk()
mainWindow.title("Morse Code Encoder")
mainWindow.geometry("300x200")

encodedMessage = []

def encodeMsg(event = None):
    capsMsg = msgEntry.get().upper()
    print(capsMsg)
    for letters in range(len(capsMsg)):
        if (capsMsg[letters] == "A"):
            encodedMessage.append(".-")
        if (capsMsg[letters] == "B"):
            encodedMessage.append("-...")    
        if (capsMsg[letters] == "C"):
            encodedMessage.append("-.-.")    
        if (capsMsg[letters] == "D"):
            encodedMessage.append("-..")    
        if (capsMsg[letters] == "E"):
            encodedMessage.append(".")    
        if (capsMsg[letters] == "F"):
            encodedMessage.append("..-.")    
        if (capsMsg[letters] == "G"):
            encodedMessage.append("--.")    
        if (capsMsg[letters] == "H"):
            encodedMessage.append("....")    
        if (capsMsg[letters] == "I"):
            encodedMessage.append("..")    
        if (capsMsg[letters] == "J"):
            encodedMessage.append(".---")    
        if (capsMsg[letters] == "K"):
            encodedMessage.append("-.-")    
        if (capsMsg[letters] == "L"):
            encodedMessage.append(".-..")    
        if (capsMsg[letters] == "M"):
            encodedMessage.append("--")    
        if (capsMsg[letters] == "N"):
            encodedMessage.append("-.")    
        if (capsMsg[letters] == "O"):
            encodedMessage.append("---")    
        if (capsMsg[letters] == "P"):
            encodedMessage.append(".--.")    
        if (capsMsg[letters] == "Q"):
            encodedMessage.append("--.-")    
        if (capsMsg[letters] == "R"):
            encodedMessage.append(".-.")        
        if (capsMsg[letters] == "S"):
            encodedMessage.append("...")    
        if (capsMsg[letters] == "T"):
            encodedMessage.append("-")    
        if (capsMsg[letters] == "U"):
            encodedMessage.append("..-")    
        if (capsMsg[letters] == "V"):
            encodedMessage.append("...-")    
        if (capsMsg[letters] == "W"):
            encodedMessage.append(".--")    
        if (capsMsg[letters] == "X"):
            encodedMessage.append("-..-")    
        if (capsMsg[letters] == "Y"):
            encodedMessage.append("-.--")    
        if (capsMsg[letters] == "Z"):
            encodedMessage.append("--..")    

        if (capsMsg[letters] == " "):
            encodedMessage.append(" | ")    
        
        if (capsMsg[letters] == "1"):
            encodedMessage.append(".----")    
            
        if (capsMsg[letters] == "2"):
            encodedMessage.append("..---")    
            
        if (capsMsg[letters] == "3"):
            encodedMessage.append("...--")    
            
        if (capsMsg[letters] == "4"):
            encodedMessage.append("....-")    
            
        if (capsMsg[letters] == "5"):
            encodedMessage.append(".....")    
            
        if (capsMsg[letters] == "6"):
            encodedMessage.append("-....")    
            
        if (capsMsg[letters] == "7"):
            encodedMessage.append("--...")    
            
        if (capsMsg[letters] == "8"):
            encodedMessage.append("---..")    
            
        if (capsMsg[letters] == "9"):
            encodedMessage.append("----.")    
            
        if (capsMsg[letters] == "0"):
            encodedMessage.append("-----")
            
    for i in range(len(encodedMessage)):
        print(encodedMessage[i], end=' ')
        
    encodedMessageLbl.config(text = encodedMessage)
    encodedMessage.clear()

msgEntry = Entry(mainWindow, width = 15, font=(None, 18))
msgEntry.focus()
msgEntry.pack(pady = 15)

encodeBtn = Button(mainWindow, text = "Encode", command = encodeMsg, font=(None, 18))
encodeBtn.pack()
mainWindow.bind("<Return>", encodeMsg)

encodedMessageLbl = Label(mainWindow, text = "", font=(None, 24))
encodedMessageLbl.pack(pady = 15)

mainWindow.mainloop()