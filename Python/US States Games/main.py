import pandas
import turtle

# Turtle setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Pandas setup
data = pandas.read_csv('50_states.csv')
all_states = data['state'].tolist()

guessed_states = []


while len(guessed_states) < 50:
	answer_state_input = screen.textinput(
		title= f"{len(guessed_states)}/50 States correct", 
		prompt="What's another state's name.")

	# answer_state exception handling
	if answer_state_input is not None:
		answer_state = answer_state_input.title()
		if answer_state == "Exit": #Exits the game
			missing_states = [state for state in all_states if state not in guessed_states]
			new_data = pandas.DataFrame(missing_states)
			new_data.to_csv('states_to_learn.csv') # outputs csv
			break	
	else: continue
		# handle the case where the input dialog is canceled or closed

	if answer_state in all_states:
		guessed_states.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data['state'] == answer_state]
		t.goto(int(state_data['x'].values[0]), int(state_data['y'].values[0]))
		t.write(state_data.state.item())
	
def get_mouse_click_coor(x, y):
	print(x, y)

# Game loop
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

	
