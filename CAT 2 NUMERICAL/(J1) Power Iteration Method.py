import numpy as np

def power_iteration(A, num_simulations: int):
    # Randomly initialize the vector b
    b_k = np.random.rand(A.shape[1])
    
    for _ in range(num_simulations):
        # Calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        
        # Re-normalize the vector
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm
    
    # Eigenvalue is the Rayleigh quotient
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k)) / np.dot(b_k.T, b_k)
    
    return eigenvalue, b_k

# Define the matrix A
A = np.array([[4, 1, 1], [1, 3, -1], [1, -1, 2]])

# Number of iterations
num_simulations = 1000

# Compute the largest eigenvalue and its corresponding eigenvector
eigenvalue, eigenvector = power_iteration(A, num_simulations)
print("Eigenvalue:", eigenvalue)
print("Eigenvector:", eigenvector)
