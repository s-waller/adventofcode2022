import os
import sys
import re


def main():
    locations_of_sensors_and_their_closest_beacon = parse_file("sample.txt")


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