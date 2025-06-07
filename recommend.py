import pandas as pd
import numpy as np
import os

print(os.path.exists('data/ratings.csv'))  # Output: True hona chahiye agar file exist karti hai

from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the ratings data
ratings = pd.read_csv('data/ratings.csv')  # Columns: userId, movieId, rating

# Step 2: Create User-Movie Matrix
user_movie_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

# Step 3: Calculate Similarity between users
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)


# Step 4: Function to recommend movies
def recommend_movies(user_id, num_recommendations=5):
    # Step 4.1: Find similar users (except the user itself)
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]

    # Step 4.2: Get this user's rated movies
    user_ratings = user_movie_matrix.loc[user_id]

    recommendations = pd.Series(dtype='float64')

    # Step 4.3: Check what similar users rated highly
    for sim_user in similar_users:
        sim_score = user_similarity_df.at[user_id, sim_user]
        sim_user_ratings = user_movie_matrix.loc[sim_user]

        for movie_id, rating in sim_user_ratings.items():
            if user_ratings[movie_id] == 0 and rating >= 4.0:
                recommendations.at[movie_id] = recommendations.get(movie_id, 0) + rating * sim_score

    return recommendations.sort_values(ascending=False).head(num_recommendations)


# Step 5: Run the recommender
user_id = 1
print(f"Recommended movies for User {user_id}:\n")
print(recommend_movies(user_id))



user_id = 1
recommended = recommend_movies(user_id, num_recommendations=3)
print(f"Top 3 recommended movies for User {user_id}:")
print(recommended)
