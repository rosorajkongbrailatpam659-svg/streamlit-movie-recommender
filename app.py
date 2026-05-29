import pickle
import streamlit as st
import requests


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)


# ---------------- FETCH POSTER FUNCTION ---------------- #

def fetch_poster(movie_id):

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

        data = requests.get(url)

        data = data.json()

        poster_path = data.get('poster_path')

        # If poster not found
        if poster_path is None:
            return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

        # Full poster URL
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

        return full_path

    except Exception as e:

        print(e)

        return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"


# ---------------- RECOMMEND FUNCTION ---------------- #

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    # Skip movies without posters
    for i in movies_list[1:20]:

        movie_id = movies.iloc[i[0]].movie_id

        poster = fetch_poster(movie_id)

        # Skip broken posters
        if "No-Image" not in poster:

            recommended_movie_names.append(
                movies.iloc[i[0]].title
            )

            recommended_movie_posters.append(
                poster
            )

        # Stop after 5 movies
        if len(recommended_movie_names) == 5:
            break

    return recommended_movie_names, recommended_movie_posters


# ---------------- LOAD DATA ---------------- #

movies = pickle.load(open('model/movie_list.pkl', 'rb'))

similarity = pickle.load(open('model/similarity.pkl', 'rb'))


# ---------------- TITLE ---------------- #

st.markdown(
    """
    <h1 style='text-align: center; color: white;'>
        🎬 Movie Recommender System
    </h1>
    """,
    unsafe_allow_html=True
)


# ---------------- DROPDOWN ---------------- #

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)


# ---------------- BUTTON ---------------- #

if st.button('Recommend'):

    with st.spinner('Loading recommendations...'):

        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

        st.write("")

        # Create columns
        col1, col2, col3, col4, col5 = st.columns(5)

        # Movie 1
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])

        # Movie 2
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        # Movie 3
        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])

        # Movie 4
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])

        # Movie 5
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
