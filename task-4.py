print("\n" + "="*50)
print("TASK 4: COMMUTATION RELATIONS AND EULER ANGLES")
print("="*50)

def commutator(A, B):
    """Compute commutator [A,B] = AB - BA"""
    return A @ B - B @ A

def anticommutator(A, B):
    """Compute anticommutator {A,B} = AB + BA"""
    return A @ B + B @ A

# Verify Pauli commutation relations
print("Commutation relations:")
print("[σₓ, σᵧ] =", commutator(pauli_x, pauli_y))
print("[σᵧ, σᵨ] =", commutator(pauli_y, pauli_z))
print("[σᵨ, σₓ] =", commutator(pauli_z, pauli_x))

print("\nAnticommutation relations:")
print("{σₓ, σᵧ} =", anticommutator(pauli_x, pauli_y))
print("{σₓ, σₓ} =", anticommutator(pauli_x, pauli_x))

# Euler angle decomposition for single-qubit gates
def euler_decomposition(theta, phi, lam):
    """Decompose single-qubit gate using Euler angles"""
    return (np.cos(theta/2) * np.eye(2) -
            1j * np.sin(theta/2) * (np.cos(phi) * pauli_x +
                                   np.sin(phi) * pauli_y)) @ \
           np.array([[np.exp(-1j*lam/2), 0], [0, np.exp(1j*lam/2)]])

# Example: Hadamard gate decomposition
hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
euler_h = euler_decomposition(np.pi/2, 0, np.pi)
print(f"\nHadamard gate:\n{hadamard}")
print(f"Euler decomposition:\n{euler_h}")
print(f"Difference: {np.max(np.abs(hadamard - euler_h)):.10f}")
