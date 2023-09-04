import random
from PIL import Image
import streamlit as s

# Set up the Streamlit app
s.title('Dice Roller')


# Create a button to roll the dice
roll_button = s.button('Roll the Dice')

# Define a dictionary to map values to dice face image file names
dice_faces = {
    1: 'dice1.png',
    2: 'dice2.png',
    3: 'dice3.png',
    4: 'dice4.png',
    5: 'dice5.png',
    6: 'dice6.png'
}

# Initialize an image variable
dice_image = None

# Check if the button is clicked
if roll_button:
    value = random.randint(1, 6)
    text = '# ' + str(value)
    s.markdown(text)
    
    # Load and display the corresponding dice face image
    image_path = './img/' + dice_faces.get(value, 'dice_unknown.png')  # Use a default image for unknown values

    dice_image = Image.open(image_path) # .resize((100,10))
    s.image(dice_image, width=200)



