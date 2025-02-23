def fibonacci(n, sequence=None):
    if sequence is None:
        sequence = []
    if n <= 0:
        return sequence
    if len(sequence) < 2:
        sequence.append(len(sequence))
    else:
        sequence.append(sequence[-1] + sequence[-2])
    return fibonacci(n - 1, sequence)
n = 10 
print(fibonacci(n))
