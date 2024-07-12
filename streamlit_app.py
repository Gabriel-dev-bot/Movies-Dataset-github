# streamlit_app.py

import streamlit as st
import pandas as pd

# Load the Movies Dataset
@st.cache
def load_data():
    data = pd.read_csv('movies_metadata.csv')
    return data

# Create a Streamlit app
st.title("The Movies Dataset")
st.write("This app displays movie data from Kaggle's The Movies Dataset.")

# Load the data
data = load_data()

# Display the data
st.write("### Movie Data")
st.write(data)

# Add a text input to filter movies by title
st.write("### Filter Movies by Title")
title_filter = st.text_input("Enter a movie title:")

# Filter the data based on the user input
if title_filter:
    filtered_data = data[data['title'].str.contains(title_filter, case=False)]
    st.write("### Filtered Movie Data")
    st.write(filtered_data)
else:
    st.write("No filter applied. Showing all movies.")

# Add a dropdown to select a genre
st.write("### Filter Movies by Genre")
genre_filter = st.selectbox("Select a genre:", data['genres'].unique())

# Filter the data based on the selected genre
if genre_filter:
    filtered_data = data[data['genres'].str.contains(genre_filter, case=False)]
    st.write("### Filtered Movie Data by Genre")
    st.write(filtered_data)

# Display ratings
st.write("### Movie Ratings")
st.write(data[['title', 'vote_average', 'vote_count']])


# Display links
st.write("### Movie Links")
st.write(data[['title', 'homepage', 'imdb_id']])
