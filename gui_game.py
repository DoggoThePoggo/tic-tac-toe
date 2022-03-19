from msilib.schema import CheckBox
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



#--------#
# Styles #
#--------#

main_frame_style = {
    'bg': 'white'
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

entry_style = {
    'relief': 'solid'
}

# Change button color if mouse is hovering
def button_enter(e):    
    e.widget['bg'] = '#1c7abd'

def button_leave(e):
    e.widget['bg'] = button_style['bg']



#------------#
# Start Menu #
#------------#

# Top frame for labels
start_frame_top = tk.Frame(root)
start_frame_top.config(main_frame_style)

welcome_label = tk.Label(start_frame_top, text='Tic-Tac-Toe')
welcome_label.config(h1_style)

description_label = tk.Label(start_frame_top, text='For cool kids to play Tic Tac Toe on Windows')
description_label.config(h3_style)

def coolness_checker():
    if start_button['state'] == 'disabled':
        start_button['state'] = 'normal'
    else:
        start_button['state'] = 'disabled'

checkbox = tk.IntVar()
coolness_checkbox = tk.Checkbutton(start_frame_top, text='I swear I am a cool kid', command=coolness_checker, variable=checkbox)
    
coolness_checkbox.config(h3_style,font=('calibri',12))

welcome_label.grid()
description_label.grid()
coolness_checkbox.grid()

# Btm frame for buttons
start_frame_btm = tk.Frame(root)
start_frame_btm.config(main_frame_style)

def pack_setup():
    start_frame_top.forget()
    start_frame_btm.forget()
    setup_frame_top.pack(pady=(175,0))
    setup_frame_btm.pack(side='bottom', fill='both')

start_button = tk.Button(start_frame_btm, text='Start', state='disabled', command=pack_setup)
quit_button = tk.Button(start_frame_btm, text='Quit', command=root.quit)

start_button.bind('<Enter>', button_enter)
start_button.bind('<Leave>', button_leave)

quit_button.bind('<Enter>', button_enter)
quit_button.bind('<Leave>', button_leave)

start_button.config(button_style, width=12)
quit_button.config(button_style, width=12)

start_button.pack(side='left', padx=25, pady=25)
quit_button.pack(side='right', padx=25, pady=25)



#-------#
# Setup #
#-------#

# Top frame for labels
setup_frame_top = tk.Frame(root)
setup_frame_top.config(main_frame_style)

instructions = tk.Label(setup_frame_top, text='Please enter your names')
instructions.config(h1_style)

player1_name_label = tk.Label(setup_frame_top, text='Player 1:')
player2_name_label = tk.Label(setup_frame_top, text='Player 2:')
player1_name_label.config(h3_style)
player2_name_label.config(h3_style)

def field_checker(*args):
    player1_name = player1_name_var.get().strip()
    player2_name = player2_name_var.get().strip()

    error_box.grid_forget()
    
    if player1_name and player2_name:
        if player1_name == player2_name:
            error_box.grid(row=3, columnspan=2, pady=(25,0))
            next_button['state'] = 'disabled'
        else:
            next_button['state'] = 'normal'
            
    else:
        next_button['state'] = 'disabled'

player1_name_var = tk.StringVar()
player1_name_var.trace('w', field_checker)
player1_name_entry = tk.Entry(setup_frame_top, textvariable=player1_name_var, justify='center')

player2_name_var = tk.StringVar()
player2_name_var.trace('w', field_checker)
player2_name_entry = tk.Entry(setup_frame_top, textvariable=player2_name_var, justify='center')

player1_name_entry.config(entry_style)
player2_name_entry.config(entry_style)

error_box = tk.Label(setup_frame_top, text='Both names cannot be identical')
error_box.config(h3_style)

instructions.grid(column=0, row=0, columnspan=2)

player1_name_label.grid(column=0, row=1)
player1_name_entry.grid(column=0, row=2)

player2_name_label.grid(column=1, row=1)
player2_name_entry.grid(column=1, row=2)

# Btm frame for buttons
setup_frame_btm = tk.Frame(root)
setup_frame_btm.config(main_frame_style)

def pack_game():
    setup_frame_top.forget()
    setup_frame_btm.forget()
    game_frame.pack()
    print(player1_name_var)

def unpack_setup():
    setup_frame_top.forget()
    setup_frame_btm.forget()
    pack_start()

next_button = tk.Button(setup_frame_btm, text='Next', state='disabled', command=pack_game)
back_button = tk.Button(setup_frame_btm, text='Back', command=unpack_setup)

next_button.bind('<Enter>', button_enter)
back_button.bind('<Enter>', button_enter)
next_button.bind('<Leave>', button_leave)
back_button.bind('<Leave>', button_leave)

next_button.config(button_style, width=12)
back_button.config(button_style, width=12)

next_button.pack(side='left', padx=25, pady=25)
back_button.pack(side='right', padx=25, pady=25)


#------#
# Game #
#------#

game_frame = tk.Frame(root)
funny_label = tk.Label(game_frame, text='Hi')
funny_label.pack()

def pack_start():
    start_frame_top.pack(pady=(175,0))
    start_frame_btm.pack(side='bottom', fill='both')
    checkbox.set(0) # ensure checkbox is clear
    start_button['state'] = 'disabled' # ensure start button is disabled

# Execute mainloop

pack_start()
root.mainloop()