from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Function for opening the 
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("PDF files",
														"*.pdf*"),
													("all files",
														"*.*")))
	
	# Change label contents
    label_file_explorer.configure(text="File Opened:\n "+filename)
    label_file_explorer.after(2000, lambda: label_file_explorer.configure(text='Please wait...')) # after 1000ms
																						
# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("390x200")

#Set window background color
window.config(background = "white")


# Create a File Explorer label
label_file_explorer = Label(window, 
							text = "Choose a file to scan",
							width = 55, height = 4, 
							fg = "blue")

# file explorer button w/ styling	
button_explore = Button(window, 
						text = "Browse Files",
						command = browseFiles,
                        activeforeground = "blue",
                        pady = 5,
                        padx = 5,
                        bd = 1,
                        width = 10) 

# exit button w/ styling
button_exit = Button(window, 
					text = "Exit",
					command = exit,
                    width = 10,
                    bd = 1) 

# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2, pady = 15)

button_exit.grid(column = 1,row = 3)

# Let the window wait for any events
window.mainloop()
