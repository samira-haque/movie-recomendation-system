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

The most similar movies are then displayed as recommendations.

### 7. Streamlit Application

The trained/processed data is saved using Pickle and loaded into the Streamlit application.

The user can select a movie from the interface and receive recommendations instantly.

---

## 🖥️ Application

The project uses **Streamlit** to provide an interactive interface.

Basic workflow:

```text
Open Application
      ↓
Select a Movie
      ↓
Click Recommendation Button
      ↓
Calculate Similarity
      ↓
Find Similar Movies
      ↓
Display Recommendations
```

---

## 📁 Project Structure

```text
movie-recomendation-system/
│
├── movies-recomendation-system/
│   │
│   ├── app.py
│   ├── *.ipynb
│   ├── movies.pkl
│   ├── cv.pkl
│   ├── vectors.pkl
│   └── other project files
│
└── README.md
```

> File names may vary depending on the current version of the project.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/samira-haque/movie-recomendation-system.git
```

### 2. Open the Project

```bash
cd movie-recomendation-system
```

### 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn streamlit
```

If NLTK is used in the notebook/application:

```bash
pip install nltk
```

### 4. Run the Streamlit Application

Navigate to the folder containing `app.py` and run:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example

Suppose the user selects:

```text
The Dark Knight
```

The system analyzes its movie features and calculates similarity with other movies.

It may then return movies with similar characteristics, such as:

```text
Recommended Movies
------------------
Batman Begins
The Dark Knight Rises
Man of Steel
Watchmen
...
```

The exact recommendations depend on the movie metadata and similarity calculations.

---

## ⭐ Key Features

* 🎬 Content-based movie recommendation
* 🤖 Machine Learning implementation
* 🧠 NLP-based text processing
* 🔢 CountVectorizer feature extraction
* 📐 Cosine Similarity
* ⚡ Fast recommendation using preprocessed data
* 🖥️ Interactive Streamlit interface
* 💾 Pickle-based model/data storage
* 🎓 Suitable for demonstrating Machine Learning concepts

---

## 📚 Machine Learning Concepts Demonstrated

This project demonstrates several important concepts from Machine Learning and NLP:

* Data preprocessing
* Feature engineering
* Text preprocessing
* Feature extraction
* Bag-of-Words representation
* Vectorization
* Similarity measurement
* Content-Based Filtering
* Model/data serialization
* Web application deployment

---

## ⚠️ Limitations

The current system is a **content-based recommender**, so it mainly depends on movie metadata.

Some limitations include:

* It does not learn directly from individual user ratings.
* Recommendations depend on the quality of movie metadata.
* It may recommend movies that are similar in content but not necessarily identical to a user's personal taste.
* New movies with limited metadata may receive less accurate recommendations.

---

## 🔮 Future Improvements

The system can be improved in several ways:

* Implement **TF-IDF** instead of basic CountVectorizer.
* Use word embeddings such as **Word2Vec** or transformer-based embeddings.
* Add user ratings and viewing history.
* Implement **Collaborative Filtering**.
* Develop a **Hybrid Recommendation System**.
* Add movie posters and additional movie information.
* Add genre and rating filters.
* Improve recommendation evaluation using metrics such as **Precision@K** and **Recall@K**.
* Deploy the application online.

---

## 🎓 Academic Purpose

This project was developed as a Machine Learning course project to demonstrate how machine learning and natural language processing techniques can be applied to a real-world recommendation problem.

The project focuses on understanding the complete pipeline from **data preprocessing to feature extraction, similarity calculation, recommendation generation, and deployment through a web application**.

---

## 👩‍💻 Author

**Samira Haque**

Computer Science Student

GitHub:
https://github.com/samira-haque

---

## 📜 License

This project is created for educational and academic purposes.
