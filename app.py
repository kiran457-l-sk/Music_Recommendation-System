import streamlit as st
import joblib
import pandas as pd

def recommend(track):
    music_index = music[music['track_name'] == track].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_music = []
    for i in music_list:
        recommended_music.append(music.iloc[i[0]].track_name)
    return recommended_music

music_dict = joblib.load('music_dict')
music = pd.DataFrame(music_dict)
similarity = joblib.load('similarity.joblib')

st.title("Music Recommender System")
selected_music_name = st.selectbox("Select a track:", music['track_name'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_music_name)
    for i in recommendations:
        st.write(i)
