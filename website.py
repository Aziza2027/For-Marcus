import pandas as pd
import streamlit as s

text = 'My first chart'

s.title(text)

data = {'Category': ['Apples', 'Bananas', 'Grapes'],
        'Quantity': [5, 8, 12]}


# Convert the dataset into a DataFrame
df = pd.DataFrame(data)

s.bar_chart(df.set_index('Category')['Quantity'])






