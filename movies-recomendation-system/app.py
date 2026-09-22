import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------
# Load files
# --------------------------------

movies = pickle.load(open('movies.pkl', 'rb'))
cv = pickle.load(open('cv.pkl', 'rb'))
vectors = pickle.load(open('vectors.pkl', 'rb'))


# --------------------------------
# Recommendation Function
# --------------------------------

def recommend(movie):

    index = movies[movies['title'] == movie].index[0]

    similarity = cosine_similarity(
        vectors[index],
        vectors
    ).flatten()

    distances = sorted(
        list(enumerate(similarity)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in distances[1:6]:
        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations


# --------------------------------
# Streamlit Page Configuration
# --------------------------------

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)


# --------------------------------
# Custom CSS
# --------------------------------

st.markdown("""
<style>

    /* Background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a,
            #172554
        );
    }

    /* Main container */
    .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 18px;
        margin-bottom: 35px;
    }

    /* Recommendation heading */
    .recommend-title {
        color: white;
        font-size: 28px;
        font-weight: 700;
        margin-top: 35px;
        margin-bottom: 20px;
    }

    /* Movie cards */
    .movie-item {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: white;
        padding: 16px 20px;
        margin: 12px 0;
        border-radius: 14px;
        border-left: 4px solid #8b5cf6;
        font-size: 17px;
        transition: 0.2s;
    }

    .movie-item:hover {
        background: rgba(255, 255, 255, 0.13);
        transform: translateX(4px);
    }

    /* Selectbox label */
    label {
        color: #e2e8f0 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(
            90deg,
            #7c3aed,
            #9333ea
        );
        color: white;
        font-size: 17px;
        font-weight: 700;
        margin-top: 15px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #9333ea,
            #a855f7
        );
        transform: translateY(-2px);
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------
# Header
# --------------------------------

st.markdown(
    '<div class="main-title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover movies similar to your favorite movie 🍿'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------
# Movie Selection
# --------------------------------

movie = st.selectbox(
    "🎥 Select a movie",
    movies['title'].values
)


# --------------------------------
# Recommend Button
# --------------------------------

if st.button("✨ Recommend Movies"):

    recommendations = recommend(movie)

    st.markdown(
        '<div class="recommend-title">'
        '🍿 Recommended Movies'
        '</div>',
        unsafe_allow_html=True
    )

    for m in recommendations:

        st.markdown(
            f'<div class="movie-item">🎬 {m}</div>',
            unsafe_allow_html=True
        )