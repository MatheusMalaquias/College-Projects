#I added a delay to appear the questions and the results
import time
def water_column_height(tower_height, tank_height):
    water_column_height = tower_height + (3 * tank_height / 4)
    return water_column_height

def pressure_gain_from_water_height(height):
    density = 998.2
    gravity = 9.80665
    pressure_gain_from_water_height = (density * gravity * height) / 1000
    return pressure_gain_from_water_height 

def pressure_loss_from_pipe(friction_factor, pipe_length, fluid_velocity, pipe_diameter):
    density = 998.2
    pressure_loss_from_pipe = -friction_factor * pipe_length * density * fluid_velocity ** 2 / (2000 * pipe_diameter)
    return pressure_loss_from_pipe

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density = 998.2
    pressure_loss_from_fittings = (-0.04 * density * (fluid_velocity ** 2) * quantity_fittings) / 2000
    return pressure_loss_from_fittings

def reynolds_number(hydraulic_diameter, fluid_velocity):
    density = 998.2
    dynamic_viscosity_of_water = 0.0010016
    reynolds_number = density * hydraulic_diameter * fluid_velocity / dynamic_viscosity_of_water
    return reynolds_number

def pressure_loss_from_pipe_reduction(reynolds_number, larger_diameter, smaller_diameter, fluid_velocity):
    density = 998.2
    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) -1)
    pressure_loss_from_pipe_reduction = -k * density * fluid_velocity ** 2 / 2000
    return pressure_loss_from_pipe_reduction

def kpa_to_psi(kpa):
    return kpa * 0.145038

PVC_SCHED80_INNER_DIAMETER = 0.28687
PVC_SCHED80_FRICTION_FACTOR = 0.013
SUPPLY_VELOCITY = 1.65
HDPE_SDR11_INNER_DIAMETER = 0.048692
HDPE_SDR11_FRICTION_FACTOR = 0.018
HOUSEHOLD_VELOCITY = 1.75

def main():
    time.sleep(2)
    tower_height = float(input("Height of water tower (meters): "))
    time.sleep(2)
    tank_height = float(input("Height of water tank walls (meters): "))
    time.sleep(2)
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    time.sleep(2)
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    time.sleep(2)
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)

    loss = pressure_loss_from_pipe(friction, length1, velocity, diameter)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(reynolds, diameter, HDPE_SDR11_INNER_DIAMETER, velocity)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY

    loss = pressure_loss_from_pipe(friction, length2, velocity, diameter)
    pressure += loss

    pressure_psi = kpa_to_psi(pressure)
    time.sleep(2)
    print(f'Pressure at house: {pressure:.1f} kilopascals, {pressure_psi:.1f} psi')

if __name__ == "__main__":
    main()