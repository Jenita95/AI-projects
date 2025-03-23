import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies = pd.DataFrame({
    'title': ['Inception', 'Interstellar', 'The Matrix', 'The Dark Knight', 'Avengers: Endgame'],
    'description': [
        'A thief who enters dreams to steal secrets.',
        'A space mission to save humanity.',
        'A hacker discovers a dystopian reality.',
        'A vigilante fights crime in Gotham City.',
        'Superheroes unite to save the universe.'  ]
})
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
def recommend_movie(title, movies, cosine_sim):
    if title not in movies['title'].values:
        return "Movie not found in database. Please try another title."
    idx = movies.index[movies['title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:3]
    recommended_movies = [movies.iloc[i[0]]['title'] for i in sim_scores]
    return recommended_movies
user_input = input("Enter a movie title: ")
recommendations =recommend_movie(user_input, movies, cosine_sim)
print(f"Recommended movies for '{user_input}': {recommendations}")
