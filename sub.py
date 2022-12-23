import math

# Define the submarine's physical properties
mass = 1000  # Kilograms
volume = 10  # Cubic meters
density = mass / volume  # Kilograms per cubic meter

# Define the submarine's initial position and orientation
position = (0, 0)  # (x, y) coordinates
orientation = 0  # Angle in radians, with 0 pointing to the right

# Define the submarine's speed and turning rate
speed = 1  # Units per second
turn_rate = math.pi / 2  # Radians per second

# Define the water properties
water_density = 1000  # Kilograms per cubic meter
gravity = 9.81  # Meters per second squared

# Calculate the submarine's buoyancy and drag forces
buoyancy = water_density * volume * gravity  # Newtons
drag_coefficient = 0.5  # Dimensionless
frontal_area = 2  # Square meters
drag = 0.5 * water_density * speed**2 * drag_coefficient * frontal_area  # Newtons

# Define the time step for the simulation
time_step = 0.1  # Seconds

# Loop for a certain number of time steps
for i in range(100):
    # Calculate the net force acting on the submarine
    net_force = buoyancy - drag  # Newtons

    # Calculate the submarine's acceleration
    acceleration = net_force / mass  # Meters per second squared

    # Update the submarine's position and orientation
    position = (position[0] + speed * time_step * math.cos(orientation),
                position[1] + speed * time_step * math.sin(orientation))
    orientation += turn_rate * time_step
    speed += acceleration * time_step

    # Print the submarine's position, orientation, and speed
    print(f"Position: {position}, Orientation: {orientation:.2f} rad, Speed: {speed:.2f} m/s")