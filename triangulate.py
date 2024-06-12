import random
import json
import math

LIGHT_SPEED = 299792458  # m/s, corrected tuple to integer
LON_OFFSET = 0.05  # degrees, assuming this for simplicity
LAT_OFFSET = 0.00  # degrees, assuming this for simplicity

def generate_location(lat_range=(-90.0, 90.0), lon_range=(-180.0, 180.0)):
    lat = round(random.uniform(lat_range[0], lat_range[1]), 6)
    lon = round(random.uniform(lon_range[0], lon_range[1]), 6)
    return lat, lon

def haversine_dist(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def get_signal_time(lat1, lon1, lat2, lon2):
    dist = haversine_dist(lat1, lon1, lat2, lon2) * 1000  # convert km to meters
    return dist / LIGHT_SPEED

def generate_data(seed_time, lat, lon):  # V2 double input to 2 sensors SENSOR_OFFSET apart
    with open("data.txt", "w") as f:
        for i in range(39):
            time = seed_time + (i * 1000000000)
            line1 = f"TPV lat={lat} lon={lon} time={time}\n"
            line2 = f"TPV lat={lat + LAT_OFFSET} lon={lon + LON_OFFSET} time={time}\n"
            f.write(line1)
            f.write(line2)

def get_distance(ping_time):
    return ping_time * LIGHT_SPEED

def determine_target_location(data_dict):
    distances = []
    for (lat, lon), ping_time in data_dict.items():
        distances.append((lat, lon, get_distance(ping_time)))

    median_lat = median([float(lat) for lat, lon, dist in distances])
    median_lon = median([float(lon) for lat, lon, dist in distances])

    return median_lat, median_lon

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n // 2 - 1] + s[n // 2]) / 2.0 if n % 2 == 0 else s[n // 2]

def create_target_dictionary(filename, target_lat, target_lon):
    with open(filename, "r") as f:
        f.readline()  # Skip the first line if it is a header
        data_dict = {}
        for line in f:
            if line.strip():  # Make sure line is not empty
                curr = line.split()
                lat = float(curr[2].split("=")[1])
                lon = float(curr[3].split("=")[1])
                time = float(curr[4].split("=")[1])
                ping = get_signal_time(target_lat, target_lon, lat, lon)
                data_dict.update({(lat, lon): ping})
    return data_dict

# Example usage
seed_time = 1622470420000000000
target_lat, target_lon = generate_location()
generate_data(seed_time, target_lat, target_lon)
data_dict = create_target_dictionary("data.txt", target_lat, target_lon)
target_location = determine_target_location(data_dict)

print("Generated Target Location:", target_lat, target_lon)
print("Calculated Target Location:", target_location)
