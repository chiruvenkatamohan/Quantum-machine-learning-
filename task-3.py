print("\n" + "="*50)
print("TASK 3: BELL STATES AND ENTANGLEMENT ENTROPY")
print("="*50)

def tensor_product(a, b):
    """Compute tensor product of two vectors"""
    return np.kron(a, b)

# Create Bell states using tensor products
bell_00 = (tensor_product(qubit_0, qubit_0) + tensor_product(qubit_1, qubit_1)) / np.sqrt(2)
bell_01 = (tensor_product(qubit_0, qubit_1) + tensor_product(qubit_1, qubit_0)) / np.sqrt(2)
bell_10 = (tensor_product(qubit_0, qubit_0) - tensor_product(qubit_1, qubit_1)) / np.sqrt(2)
bell_11 = (tensor_product(qubit_0, qubit_1) - tensor_product(qubit_1, qubit_0)) / np.sqrt(2)

print("Bell state |Φ⁺⟩ =", bell_00)
print("Bell state |Φ⁻⟩ =", bell_10)

def entanglement_entropy(state):
    """Calculate entanglement entropy for 2-qubit system"""
    # Reshape state into 2x2 matrix
    psi_matrix = state.reshape(2, 2)
    # Compute reduced density matrix (trace over second qubit)
    rho_a = psi_matrix @ psi_matrix.conj().T
    # Get eigenvalues
    eigenvals = np.linalg.eigvals(rho_a)
    eigenvals = eigenvals[eigenvals > 1e-10]  # Remove zeros
    # Calculate von Neumann entropy
    entropy = -np.sum(eigenvals * np.log2(eigenvals))
    return entropy

print(f"\nEntanglement entropy of |Φ⁺⟩: {entanglement_entropy(bell_00):.3f}")
print(f"Entanglement entropy of |Φ⁻⟩: {entanglement_entropy(bell_10):.3f}")

# Compare with separable state
separable = tensor_product(qubit_0, qubit_0)
print(f"Entanglement entropy of |00⟩: {entanglement_entropy(separable):.3f}")
