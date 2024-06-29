import os
import json

def display_color_mapping():
    for color in colors:
        print(f"n: {color['n']}, name: {color['name']}")

def save_canvas(filename, canvas):
    with open(os.path.join(map_folder, f"{filename}.json"), 'w') as file:
        json.dump(canvas, file, indent=2)

def input_via_loop():
    for z in range(4):
        for y in range(4):
            for x in range(4):
                n = int(input(f"Enter the number (n) for position [{z}][{y}][{x}]: "))
                for color in colors:
                    if color['n'] == n:
                        canvas[z][y][x] = color['c']
                        break
                else:
                    print(f"Invalid number {n}, using None for color.")
                    canvas[z][y][x] = None

def input_via_coordinates():
    while True:
        z = int(input("Enter the Z coordinate (0-3): "))
        y = int(input("Enter the Y coordinate (0-3): "))
        x = int(input("Enter the X coordinate (0-3): "))
        n = int(input("Enter the number (n) for this position: "))

        if 0 <= z < 4 and 0 <= y < 4 and 0 <= x < 4:
            for color in colors:
                if color['n'] == n:
                    canvas[z][y][x] = color['c']
                    break
            else:
                print(f"Invalid number {n}, using None for color.")
                canvas[z][y][x] = None

            # Ask if the user wants to continue
            if input("Continue? (y/n): ").lower() != 'y':
                break
        else:
           print("Invalid coordinates, please try again.")

def main():
    filename = input("Enter the filename to save the map (without .json): ")
    filename += ".json"
    with open(file.name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    map_folder = 'map'
    if not os.path.exists(map_folder):
        os.makedirs(map_folder)
    
    canvas = [[[None] * 4 for _ in range(4)] for _ in range(4)]
    
    display_color_mapping()

    print("\nMethod 1: Enter numbers for each position via loop.")
    input_via_loop()

    print("\nMethod 2: Enter coordinates and number for specific positions.")
    input_via_coordinates()

    save_canvas(filename, canvas)
    print(f"Canvas saved to {map_folder}/{filename}")