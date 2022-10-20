from multiprocessing.sharedctypes import Value
from translate import Translator
import tkinter
from language import languages;
  
# Create the default window
root = tkinter.Tk()
root.title("Translator")
root.geometry('700x500')
  
# Create the list of options

options_list = []

for x in range (len(languages)):
    options_list.append(languages[x]['name'])


# variables 
inputBox = tkinter.Text(root, height = 5, width = 52)
inputBox.pack(pady=10)

value_inside = tkinter.StringVar(root)
value_inside.set("Select an Target Value")
question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
question_menu.pack(pady=5)



  
  
  
def print_answers():
    
    selectLang = ''
    # print("Selected Option: {}".format(value_inside.get()))
    key = "name"
    val = value_inside.get()
    d = next((d for d in languages if d.get(key) == val), None)
    # print(d)
    translator = Translator(to_lang=d['code'])
    inputText=inputBox.get('1.0', 'end')
    translation = translator.translate(inputText)
    outputBox.config(state='normal')
    outputBox.delete('1.0',tkinter.END)
    outputBox.insert(tkinter.END,translation)
    outputBox.config(state='disabled')

    
    return None
  
  
# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = tkinter.Button(root, text='Convert', command=print_answers)
submit_button.pack()

outputBox = tkinter.Text(root,state='disabled', height = 5, width = 52)
outputBox.pack(pady=5)
  
root.mainloop()



