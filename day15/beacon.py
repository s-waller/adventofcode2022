import os
import sys
import re

def main():
    beaconless_locations = set()
    locations_of_sensors_and_their_closest_beacon = parse_file("input.txt")
    for sensor_beacon_pair in locations_of_sensors_and_their_closest_beacon:
        distance = caculate_manhattan_distance(sensor_beacon_pair)
        sensor = sensor_location(sensor_beacon_pair)
        fan_out(sensor, beaconless_locations, distance)
    print(get_beaconless_locations_on_row(beaconless_locations, 20000))

def get_beaconless_locations_on_row(beaconless_locations, row_number):
    beaconless_locations_on_row = 0
    for location in beaconless_locations:
        if location[1] == row_number:
            beaconless_locations_on_row += 1
    return beaconless_locations_on_row

def sensor_location(sensor_and_closest_beacon_pair):
    sensor_location = sensor_and_closest_beacon_pair[0]
    return sensor_location

def caculate_manhattan_distance(sensor_and_closest_beacon_pair):
    sensor_location = sensor_and_closest_beacon_pair[0]
    beacon_location = sensor_and_closest_beacon_pair[1]
    manhattan_distance = abs(sensor_location[0] - beacon_location[0]) + abs(sensor_location[1] - beacon_location[1])
    return manhattan_distance

def fan_out(current_location, beaconless_locations, _max_depth=0):
    visited = {current_location}
    beaconless_locations.add(current_location)
    if _max_depth > 0:
        neighbours = scan_directions(current_location, visited)
        for next_location in neighbours:
            fan_out(next_location, beaconless_locations, _max_depth=_max_depth - 1)
        return beaconless_locations
    else:
        return beaconless_locations

def parse_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        lines = file_content.read().split('\n')
        sensors_and_closest_beacon = []
        for line in lines:
            parsed_coordinates = re.findall(r'(x|y)=(-?\d+)', line)
            sensor_coordinates = (int(parsed_coordinates[0][1]), int(parsed_coordinates[1][1]))
            closest_beacon_coordinates = (int(parsed_coordinates[2][1]), int(parsed_coordinates[3][1]))
            sensors_and_closest_beacon.append((sensor_coordinates, closest_beacon_coordinates))
        return sensors_and_closest_beacon

def west(current_location):
    location = (current_location[0] -1,current_location[1])
    return location

def east(current_location):
    location = (current_location[0] + 1,current_location[1])
    return location

def north(current_location):
    location = (current_location[0],current_location[1] + 1)
    return location

def south(current_location):
    location = (current_location[0],current_location[1] + 1)
    return location

def valid_coordinates(coordinates, visited):
    if tuple(coordinates) in visited:
        return False
    return True

def scan_directions(current_location, visited):
    possible_directions = []
    for direction in (north, south, east, west):
        direction_coordinates = direction(current_location)
        if valid_coordinates(direction_coordinates, visited):
                possible_directions.append(direction_coordinates)
    return possible_directions

if __name__ == "__main__":
    main()