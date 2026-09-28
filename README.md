# 🎬 Movie Recommendation System

A Machine Learning-based **Movie Recommendation System** that recommends movies similar to a movie selected by the user. The system uses **Content-Based Filtering**, **Natural Language Processing (NLP)**, **CountVectorizer**, and **Cosine Similarity** to identify movies with similar characteristics.

The project also includes an interactive **Streamlit web application** where users can select a movie and receive recommendations through a simple and user-friendly interface.

---

## 📌 Project Overview

With thousands of movies available on different platforms, finding a movie that matches a user's interests can be difficult.

This project solves that problem by analyzing movie-related information such as **genres, keywords, cast, crew, and overview**. These features are combined into a single text representation and converted into numerical vectors.

The system then calculates the similarity between movies using **Cosine Similarity** and recommends movies that are most similar to the selected movie.

---

## 🎯 Objectives

The main objectives of this project are:

* To build a movie recommendation system using Machine Learning techniques.
* To understand and implement **Content-Based Filtering**.
* To apply NLP techniques to movie metadata.
* To convert textual movie information into numerical features.
* To calculate similarity between movies.
* To provide relevant movie recommendations.
* To develop an interactive web interface using Streamlit.

---

## 🧠 Machine Learning Approach

This project uses **Content-Based Filtering**.

Instead of depending on user ratings or other users' preferences, the system analyzes the **content/features of movies**.

For example, if a user selects an action movie containing specific genres, keywords, actors, and directors, the system searches for other movies with similar characteristics.

### Recommendation Pipeline

```text
Movie Dataset
      ↓
Data Cleaning
      ↓
Feature Selection
      ↓
Feature Combination / Tags
      ↓
Text Preprocessing
      ↓
CountVectorizer
      ↓
Numerical Feature Vectors
      ↓
Cosine Similarity
      ↓
Similarity Ranking
      ↓
Top Similar Movies
      ↓
Streamlit Web Application
```

---

## 🔬 Technologies Used

| Technology        | Purpose                                     |
| ----------------- | ------------------------------------------- |
| Python            | Main programming language                   |
| Pandas            | Data manipulation and preprocessing         |
| NumPy             | Numerical operations                        |
| Scikit-learn      | Machine Learning and similarity calculation |
| CountVectorizer   | Text feature extraction                     |
| Cosine Similarity | Measuring movie similarity                  |
| Streamlit         | Web application interface                   |
| Pickle            | Saving and loading processed model objects  |
| Jupyter Notebook  | Data analysis and model development         |

---

## 📊 Dataset

The system is based on movie metadata containing information such as:

* Movie title
* Genres
* Keywords
* Cast
* Crew
* Movie overview/description

The dataset is used to create a combined **tag/feature representation** for every movie.

---

## ⚙️ How the System Works

### 1. Data Collection

Movie information is loaded into a Pandas DataFrame.

### 2. Data Preprocessing

The data is cleaned and relevant movie features are selected.

Missing or unnecessary information is handled before building the recommendation model.

### 3. Feature Engineering

Important movie features are combined into a single textual feature.

For example:

```text
Genres + Keywords + Cast + Crew + Overview
```

This combined information represents the characteristics of each movie.

### 4. Text Vectorization

The textual information cannot be directly used by a machine learning algorithm.

Therefore, **CountVectorizer** is used to convert the movie tags into numerical vectors.

Conceptually:

```text
Movie A → [1, 0, 2, 1, 0, ...]
Movie B → [0, 1, 1, 0, 2, ...]
Movie C → [1, 0, 1, 1, 0, ...]
```

### 5. Cosine Similarity

After converting the movie information into vectors, **Cosine Similarity** is used to measure how similar two movies are.

A higher similarity value means the movies have more similar content.

### 6. Recommendation

When the user selects a movie, the system compares that movie with other movies and ranks them according to their similarity score.

The most similar movies are then
