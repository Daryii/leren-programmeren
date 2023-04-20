from functies import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox # if you want to send messages to the user.

# functions
def calculate():
    textToBeCalculated = calculateInput.get('1.0', 'end') # get all the text from inputfield
    characterLabel.config(text=f"karakters: {getNumberOfCharacters(textToBeCalculated)}")
    sentencesLabel.config(text =f"Zinnen: {getNumberOfSentences(textToBeCalculated)}")
    woordenlabel.config(text = f"aantal_woorden:{getNumberOfWords(textToBeCalculated)}")
    AVI_Score.config(text = f"AVI_Score:{getAVIscore(textToBeCalculated)}")
    

#variables TK
root = tk.Tk()              # create tkInter window
root.title('Text analyser') # set title
root.geometry('600x600')    # set dimensio
calculateInput = tk.Text(root, width = 70, height = 30, background='lightgrey')       # generate imput element
calculateButton = ttk.Button(root, text='Bereken score(s)', command=calculate)        # generate button when pressed -> calculate
characterLabel = tk.Label(root, text=f'Karakters:', width=20, bg='black', fg='white') # generate characterLabel
sentencesLabel = tk.Label(root, text=f'Zinnen:', width=20, bg='black', fg='white')    # generate sentencesLabel
woordenlabel = tk.Label(root, text=f'aantal_woorden:', width=20, bg='black', fg='white')   
# AVI_Score
AVI_Score = tk.Label(root, text=f'AVI_Score:', width=20, bg='black', fg='white')


calculateInput.place(x=20, y=20)   # place is one of the ways to put elements on root (window).
calculateButton.place(x=20, y=520)
characterLabel.place(x=180, y=560)
sentencesLabel.place(x=20, y=560)
woordenlabel.place(x=340 , y=560)
AVI_Score.place(x = 490 , y=560)
# start program
root.mainloop() # runs until stopped with default stop button.
