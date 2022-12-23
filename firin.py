import math

# Define the submarine's initial position and orientation
submarine_position = (0, 0)  # (x, y) coordinates
submarine_orientation = 0  # Angle in radians, with 0 pointing to the right
submarine_speed = 1000 KMPH

# Define the torpedo's initial position and orientation
torpedo_position = submarine_position  # (x, y) coordinates
torpedo_orientation = submarine_orientation  # Angle in radians

# Define the torpedo's speed and turning rate
torpedo_speed = 10  # Units per second
torpedo_turn_rate = math.pi / 2  # Radians per second

# Define the time step for the simulation
time_step = 0.1  # Seconds

# Loop for a certain number of time steps
for i in range(100):
    # Update the submarine's orientation
    submarine_orientation += submarine_turn_rate * time_step

    # Update the torpedo's position and orientation
    torpedo_position = (torpedo_position[0] + torpedo_speed * time_step * math.cos(torpedo_orientation),
                        torpedo_position[1] + torpedo_speed * time_step * math.sin(torpedo_orientation))
    torpedo_orientation += torpedo_turn_rate * time_step

    # Print the submarine's position, orientation, and speed
    print(f"Submarine position: {submarine_position}, Orientation: {submarine_orientation:.2f} rad")
    print(f"Torpedo position: {torpedo_position}, Orientation: {torpedo_orientation:.2f} rad, Speed: {torpedo_speed:.2f} m/s")
