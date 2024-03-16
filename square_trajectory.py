# #!/usr/bin/env python
# import time
# from flyt_python import api

# drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

# time.sleep(3)

# print ('taking off till height of 5m')
# drone.take_off(5.0)
# print ('Current position - Point A of square ABCD')

# print (' move in a square trajectory of side length 6.5m at a height of 5m')

# print (' 2. moving to Point B of square ABCD')
# drone.position_set(6.5, 0, 0, yaw=1.0472, relative=True)

# print (' 2. moving to Point C of square ABCD')
# drone.position_set(0, 6.5, 0, relative=True)

# print (' 2. moving back to Point D of square ABCD')
# drone.position_set(-6.5, 0, 0, relative=True)

# print (' 2. moving back to Point D of square ABCD')
# drone.position_set(0, -6.5, 0, relative=True)

# print (' 6. Landing')
# drone.land(async_land=False)
# # shutdown the instance
# drone.disconnect()
#!/usr/bin/env python
import os
import requests

# Set up environment variables
personal_access_token = os.getenv('6f58607fc92ea481c8501052c8dfc6c13ebc406e')
vehicle_id = os.getenv('hnNnWhMz')
api_base_url = "https://dev.flytbase.com/rest/ros/get_global_namespace"

# Construct authentication header
headers = {
    "Authorization": f"Token {personal_access_token}",
    "VehicleID": vehicle_id
}

# Function to make API requests
def make_api_request(endpoint, method="GET", data=None):
    try:
        url = f"{api_base_url}/{endpoint}"  # Correct URL construction
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        
        response.raise_for_status()  # Raise error for non-2xx status codes
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return None


# Function to initiate takeoff
def take_off(takeoff_alt):
    endpoint = "take_off"
    data = {"takeoff_alt": takeoff_alt}
    return make_api_request(endpoint, method="POST", data=data)

# Function to disarm the drone
def disarm():
    endpoint = "disarm"
    return make_api_request(endpoint, method="GET")

# Function to land the drone
def land():
    endpoint = "land"
    return make_api_request(endpoint, method="GET")

# Function to move the drone to a specified position
def move_to(x, y, z, yaw=0.0, is_async=False, relative=True, yaw_valid=True, body_frame=False):
    endpoint = "position_set"
    data = {
        "x": x,
        "y": y,
        "z": z,
        "yaw": yaw,
        "async": is_async,
        "relative": relative,
        "yaw_valid": yaw_valid,
        "body_frame": body_frame
    }
    return make_api_request(endpoint, method="POST", data=data)

# Main program
if __name__ == "__main__":
    try:
        # Example: Takeoff
        takeoff_altitude = 5.0
        take_off(takeoff_altitude)
        print("Takeoff initiated successfully.")

        # Example: Move to a specified position
        move_to(6.5, 0, 0, yaw=1.0472, relative=True)
        move_to(0, 6.5, 0, relative=True)
        move_to(-6.5, 0, 0, relative=True)
        move_to(0, -6.5, 0, relative=True)
        print("Move completed successfully.")

        # Example: Land
        land_response = land()
        if land_response['success']:
            print("Drone landed successfully.")
        else:
            print("Failed to land the drone:", land_response['message'])

    except Exception as e:
        print("An error occurred:", e)

