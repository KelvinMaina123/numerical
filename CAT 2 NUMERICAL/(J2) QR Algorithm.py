import numpy as np

def qr_algorithm(A, num_iterations: int):
    A_k = A.copy()
    
    for _ in range(num_iterations):
        # Perform QR decomposition
        Q, R = np.linalg.qr(A_k)
        # Update A_k
        A_k = np.dot(R, Q)
    
    # Eigenvalues are the diagonal elements of A_k
    eigenvalues = np.diag(A_k)
    return eigenvalues

# Define the matrix A
A = np.array([[4, 1, 1], [1, 3, -1], [1, -1, 2]])

# Number of iterations
num_iterations = 100

# Compute the eigenvalues
eigenvalues = qr_algorithm(A, num_iterations)
print("Eigenvalues:", eigenvalues)
