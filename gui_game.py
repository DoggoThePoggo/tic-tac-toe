import tkinter as tk


root = tk.Tk()
root.resizable(False, False)
root.config(bg='white')
# root.tk.call('tk', 'scaling', 1)

app_width, app_height = (500,500)

# Calculate position to start window in the middle-ish
screen_width = int(root.winfo_screenwidth()/2-app_width/2)
screen_height = int(root.winfo_screenheight()/2-app_height/2) 

root.geometry(f'{app_width}x{app_height}+{screen_width}+{screen_height}')

root.title('Pro League Tic Tac Toe (Enhanced Reboot Director\'s cut Extended Edition)')

main_frame_style = {
    'bg': 'white',
    'padx': 30,
    'pady': 30
}

h1_style = {
    'font': ('Segoe UI Semibold', 24),
    'bg': 'white',
    'fg': 'grey10'
}
h3_style = {
    'font': ('Calibri', 16),
    'bg': 'white',
    'fg': 'grey40'
}

button_style = {
    'fg': 'white',
    'bg': '#0f86db',
    'activeforeground': 'white',
    'activebackground': '#0b4e7d',
    'relief': 'groove'
}

# Change button color if mouse is hovering
def button_enter(e):    
    e.widget['bg'] = '#1c7abd'

def button_leave(e):
    e.widget['bg'] = button_style['bg']



#------------#
# Start Menu #
#------------#

start_frame = tk.Frame(root)
start_frame.config(main_frame_style)

# Labels
welcome_label = tk.Label(start_frame, text='Tic Tac Toe')
welcome_label.config(h1_style)

description_label = tk.Label(start_frame, text='For cool kids to play Tic Tac Toe on Windows')
description_label.config(h3_style)

# Buttons
def start_game():
    start_frame.pack_forget()
    setup_frame.pack()

start_button = tk.Button(start_frame, text='Start', command=start_game)
quit_button = tk.Button(start_frame, text='Quit', command=root.quit)

start_button.bind('<Enter>', button_enter)
quit_button.bind('<Enter>', button_enter)
start_button.bind('<Leave>', button_leave)
quit_button.bind('<Leave>', button_leave)

start_button.config(button_style, width=12)
quit_button.config(button_style, width=12)

# Element placements
welcome_label.grid(column=0,  row=0, columnspan=2, padx=15, pady=15)
description_label.grid(column=0,  row=1, columnspan=2, padx=15, pady=15)
quit_button.grid(column=1,  row=2, padx=50, pady=30)
start_button.grid(column=0,  row=2, padx=50, pady=30)



#-------#
# Setup #
#-------#

setup_frame = tk.Frame(root)
setup_frame.config(main_frame_style)

# Labels
instructions = tk.Label(setup_frame, text='Please enter your names!')
instructions.config(h1_style)

player1_name_label = tk.Label(setup_frame, text='Player 1:')
player2_name_label = tk.Label(setup_frame, text='Player 2:')
player1_name_label.config(h3_style)
player2_name_label.config(h3_style)

# Name input and order selection
player1_name_var = tk.StringVar()
player1_name = player1_name_var.get()
player1_name_entry = tk.Entry(setup_frame, textvariable=player1_name_var, justify='center')

player2_name_var = tk.StringVar()
player2_name = player2_name_var.get()
player2_name_entry = tk.Entry(setup_frame, textvariable=player2_name_var, justify='center')

# Element placements
instructions.grid(column=0, row=0, columnspan=2)
player1_name_label.grid(column=0, row=1)
player2_name_label.grid(column=1, row=1)
player1_name_entry.grid(column=0, row=2)
player2_name_entry.grid(column=1, row=2)



#------#
# Game #
#------#

game_frame = tk.Frame(root)




start_frame.pack()
root.mainloop()