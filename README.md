# Movie Recommendation System

A content-based movie recommendation system built using Machine Learning and Streamlit. This project recommends similar movies based on user selection and displays movie posters using the TMDB API.

## Features

- Recommends movies based on similarity
- Displays movie posters using TMDB API
- Simple and interactive Streamlit web app
- Uses Machine Learning (Cosine Similarity)
- Fast and lightweight system

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- TMDB API

## Project Structure

movie-recommender-system/
├── app.py
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── README.md

## Installation

Clone the repository:

git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system

Create virtual environment (optional):

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install streamlit pandas numpy scikit-learn requests pillow

## Run the Application

streamlit run app.py

Then open:

http://localhost:8501

## API Setup (TMDB)

Create an account on TMDB:
https://www.themoviedb.org/

Generate API key and add it in your code:

api_key = "YOUR_API_KEY"

## How It Works

The system processes movie data and creates feature vectors. It calculates similarity between movies using cosine similarity. When a user selects a movie, the system finds and displays the most similar movies along with their posters.

## Future Improvements

- Add collaborative filtering
- Improve recommendation accuracy
- Enhance UI design
- Deploy on cloud platforms

## Author

Rosoraj Kongbrailatpam  
MCA Student  
Skills: Python, Machine Learning, Data Analysis

## License

This project is open-source and free to use.
