import tkinter as tk
import tkinter.filedialog as fd
from functools import partial


def openFileFunction():
    filepath = fd.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "r") as inputFile:
        buttonName = filepath[filepath.rfind("/")+1:]
        for item in fileButtonDictionary:
            if item == buttonName:
                return

        editorText.delete("1.0", tk.END)

        text = inputFile.read()
        editorText.insert(tk.END, text)

        tempButton = tk.Button(master=fileBarFrame, text=buttonName,
                               width=14, command=partial(fileButtonFunction,
                                                         buttonName))
        tempButton.pack(side=tk.LEFT)
        fileButtonDictionary[buttonName] = tempButton
        filepathDictionary[buttonName] = filepath

        global activeFile
        activeFile = buttonName


def saveFunction():
    filepath = filepathDictionary[activeFile]
    with open(filepath, "w") as outputFile:
        text = editorText.get("1.0", tk.END)
        outputFile.write(text)


def saveAsFunction():
    filepath = fd.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as outputFile:
        text = editorText.get("1.0", tk.END)
        outputFile.write(text)
    return filepath


def openInTabs(filepath):
    if not filepath:
        return
    with open(filepath, "r") as inputFile:
        buttonName = filepath[filepath.rfind("/")+1:]
        for item in fileButtonDictionary:
            if item == buttonName:
                return

        editorText.delete("1.0", tk.END)

        text = inputFile.read()
        editorText.insert(tk.END, text)

        tempButton = tk.Button(master=fileBarFrame, text=buttonName,
                               width=14, command=partial(fileButtonFunction,
                                                         buttonName))
        tempButton.pack(side=tk.LEFT)
        fileButtonDictionary[buttonName] = tempButton
        filepathDictionary[buttonName] = filepath

        global activeFile
        activeFile = buttonName


def fileButtonFunction(buttonName):
    global activeFile
    if activeFile == buttonName:
        return
    activeFile = buttonName
    filepath = filepathDictionary[activeFile]
    with open(filepath, "r") as inputFile:
        text = inputFile.read()
        editorText.delete("1.0", tk.END)
        editorText.insert(tk.END, text)


root = tk.Tk()
root.title("Text Editor")

root.rowconfigure(2, minsize=600, weight=1)
root.columnconfigure(0, minsize=300, weight=1)

mainBarFrame = tk.Frame(master=root, background="#454545")
fileBarFrame = tk.Frame(master=root, background="#454545")
textFrame = tk.Frame(master=root)

mainBarFrame.grid(row=0, column=0, sticky="ew")
fileBarFrame.grid(row=1, column=0, sticky="ew")
textFrame.grid(row=2, column=0, sticky="nsew")

# Main bar frame widgets.
openButton = tk.Button(master=mainBarFrame, text="Open",
                       width=14, command=openFileFunction, bg="#454545",
                       fg="white", borderwidth=0)
openButton.grid(row=0, column=0)

saveButton = tk.Button(master=mainBarFrame, text="Save",
                       width=14, command=saveFunction, bg="#454545",
                       fg="white", borderwidth=0)
saveButton.grid(row=0, column=1)

saveAsButton = tk.Button(
    master=mainBarFrame, text="Save As...", width=14, command=saveAsFunction,
    bg="#454545", fg="white", borderwidth=0)
saveAsButton.grid(row=0, column=2)

# File bar frame widgets
activeFile = "null"
fileButtonDictionary = {}
filepathDictionary = {}

# Text frame widgets
editorText = tk.Text(master=textFrame, bg="black",
                     fg="white", insertbackground="white")
editorText.pack(fill=tk.BOTH, expand=tk.TRUE)


root.mainloop()
