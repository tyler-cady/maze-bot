import matplotlib.pyplot as plt

def read_and_plot_path(file_path):
    # Read values from the file
    with open(file_path, 'r') as file:
        values = file.read().strip().split(',')
        values = [int(value) for value in values]

    # Group values in chunks of 4
    groups_of_4 = [values[i:i + 4] for i in range(0, len(values), 4)]
    
    # Starting coordinates
    x, y = 0, 0
    path = [(x, y)]
    
    # Calculate the path
    for group in groups_of_4:
        if len(group) == 4:
            y += group[0]
            x += group[1]
            path.append((x, y))
            x -= group[2]
            path.append((x, y))
            y -= group[3]
            path.append((x, y))

    # Extract x and y coordinates for plotting
    x_coords, y_coords = zip(*path)
    
    # Plot the path
    plt.figure(figsize=(10, 6))
    plt.plot(x_coords, y_coords, marker='o')
    plt.title('Path of the Object')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
    
    return path

# Example usage
file_path = 'data.csv'
path = read_and_plot_path(file_path)
print(path)