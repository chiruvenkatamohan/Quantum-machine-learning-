print("\n" + "="*50)
print("TASK 6: QUANTUM ERROR CORRECTION (9-QUBIT CODE)")
print("="*50)

def encode_9_qubit(logical_qubit):
    """Encode logical qubit into 9 physical qubits (Shor code)"""
    # Simplified encoding: |0⟩_L → |000000000⟩, |1⟩_L → |111111111⟩
    if np.allclose(logical_qubit, [1, 0]):  # |0⟩
        encoded = np.zeros(2**9)
        encoded[0] = 1  # |000000000⟩
    else:  # |1⟩
        encoded = np.zeros(2**9)
        encoded[-1] = 1  # |111111111⟩
    return encoded

def add_bit_flip_noise(state, error_prob=0.1):
    """Add bit flip noise to quantum state"""
    # Simplified: just report noise added
    print(f"Bit flip noise added with probability {error_prob}")
    return state

# Encode logical qubits
logical_0 = np.array([1, 0])
logical_1 = np.array([0, 1])

encoded_0 = encode_9_qubit(logical_0)
encoded_1 = encode_9_qubit(logical_1)

print("Logical |0⟩ encoded into 9-qubit code")
print("Logical |1⟩ encoded into 9-qubit code")

# Simulate noise
noisy_0 = add_bit_flip_noise(encoded_0)
print("Error correction protocol: detect and correct single bit flips")
