import os
import sys
import re

def main():
    beaconless_locations = set()
    locations_of_sensors_and_their_closest_beacon = parse_file("sample.txt")
    for sensor_beacon_pair in locations_of_sensors_and_their_closest_beacon:
        beaconless_locations.add(caculate_beaconless_locations(sensor_beacon_pair))

def caculate_beaconless_locations(sensor_and_closest_beacon_pair):
    sensor_location = sensor_and_closest_beacon_pair[0]
    beacon_location = sensor_and_closest_beacon_pair[1]
    manhattan_distance = abs(sensor_location[0] - beacon_location[0]) + abs(sensor_location[1] - beacon_location[1])

    return



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

if __name__ == "__main__":
    main()