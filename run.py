import random
import streamlit as s

s.title('Dice Roller ')

s.markdown('# This is Marcus')

roll_button = s.button('Roll the Dice')



if roll_button:
    value = random.randint(1,6)
    text = 'Dice value is ' + str(value)
    # s.write(text)

    s.markdown(f"# {value} :game_die:")

