import os

def parse(file_path):
    """Parses a file and returns a matrix of integers."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    with open(file_path, 'r') as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            matrix.append([int(x) for x in line.split()])
        
        return matrix
