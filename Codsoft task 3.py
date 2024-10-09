import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

movie_titles = ['Sector 36', 'Spaceman', 'Trap', 'The Dark Knight', 'Pulp Fiction']

num_users = 5  
num_movies = len(movie_titles)
user_ratings = np.zeros((num_users, num_movies)) 

def collect_user_ratings():
    print("Please enter ratings for the following movies (1-5, 0 for not rated):")
    for i, movie in enumerate(movie_titles):
        while True:
            try:
                rating = int(input(f"{movie}: "))
                if rating in range(0, 6): 
                    user_ratings[0, i] = rating 
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 5.")

def calculate_similarity(ratings_matrix):
    return cosine_similarity(ratings_matrix)

def get_recommendations(user_index, user_ratings, similarity_matrix, movie_titles):
    user_ratings_for_user = user_ratings[user_index]

    weighted_sum_ratings = np.zeros(user_ratings.shape[1])
    sim_sum = np.zeros(user_ratings.shape[1])

    for other_user_index in range(user_ratings.shape[0]):
        if other_user_index == user_index:
            continue
        
        similarity = similarity_matrix[user_index, other_user_index]

        for movie_index in range(user_ratings.shape[1]):
            if user_ratings[other_user_index, movie_index] != 0:
                weighted_sum_ratings[movie_index] += similarity * user_ratings[other_user_index, movie_index]
                sim_sum[movie_index] += similarity

    predicted_ratings = np.zeros(user_ratings.shape[1])
    for i in range(user_ratings.shape[1]):
        if sim_sum[i] != 0:
            predicted_ratings[i] = weighted_sum_ratings[i] / sim_sum[i]

    recommendations = []
    for i in range(len(predicted_ratings)):
        if user_ratings_for_user[i] == 0: 
            recommendations.append((movie_titles[i], predicted_ratings[i]))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

collect_user_ratings()

user_ratings[1] = [4, 0, 0, 3, 2]  
user_ratings[2] = [0, 5, 4, 0, 0]  
user_ratings[3] = [3, 0, 0, 5, 4]  
user_ratings[4] = [0, 4, 3, 0, 5]  

similarity_matrix = calculate_similarity(user_ratings)

user_index = 0
recommendations = get_recommendations(user_index, user_ratings, similarity_matrix, movie_titles)

print(f"\nRecommendations for Your Ratings:")
for movie, score in recommendations:
    print(f"{movie}: Predicted rating = {score:.2f}")
