from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_cosine_similarity(vec_1, vec_2):  
    return cosine_similarity(vec_1.reshape(1, -1), vec_2.reshape(1, -1))[0][0]

# finding cosine similarity between two vectors
vec1 = np.array([[12, 41, 60, 11, 21]])
vec2 = np.array([[40, 11, 4, 11, 14]])
print(get_cosine_similarity(vec1, vec2))

# creating a vector similar to vec1
vec3 = np.array([[12, 45, 60, 11, 25]])
print(get_cosine_similarity(vec1, vec3))
