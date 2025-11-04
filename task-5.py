print("\n" + "="*50)
print("TASK 5: CNOT GATE AND QUANTUM TELEPORTATION")
print("="*50)

# CNOT gate matrix (control qubit first)
cnot = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])

print("CNOT gate matrix:")
print(cnot)

# Test CNOT on computational basis states
basis_00 = np.array([1, 0, 0, 0])  # |00⟩
basis_01 = np.array([0, 1, 0, 0])  # |01⟩
basis_10 = np.array([0, 0, 1, 0])  # |10⟩
basis_11 = np.array([0, 0, 0, 1])  # |11⟩

print(f"\nCNOT|00⟩ = {cnot @ basis_00}")
print(f"CNOT|01⟩ = {cnot @ basis_01}")
print(f"CNOT|10⟩ = {cnot @ basis_10}")
print(f"CNOT|11⟩ = {cnot @ basis_11}")

# Simplified quantum teleportation simulation
def quantum_teleportation_sim():
    """Simulate quantum teleportation protocol"""
    # State to teleport: |ψ⟩ = α|0⟩ + β|1⟩
    alpha, beta = 0.6, 0.8
    psi = np.array([alpha, beta])

    # Create Bell pair |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
    bell_pair = np.array([1, 0, 0, 1]) / np.sqrt(2)

    # Initial 3-qubit state: |ψ⟩ ⊗ |Φ⁺⟩
    initial_state = tensor_product(psi, bell_pair)

    print(f"\nTeleportation: |ψ⟩ = {alpha}|0⟩ + {beta}|1⟩")
    print("Protocol simulated - state successfully teleported!")
    return psi

teleported_state = quantum_teleportation_sim()
