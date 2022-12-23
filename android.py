import android

# Connect to the Android device
droid = android.Android()

# Enable the phone's GPS to get the current location
try:
    droid.startLocating()
except android.AndroidError:
    print("Error starting GPS location. Make sure GPS is enabled on the device.")

# Get the current location
try:
    location = droid.readLocation()
    latitude = location['gps']['latitude']
    longitude = location['gps']['longitude']
except android.AndroidError:
    print("Error reading GPS location. Make sure GPS is enabled and has a stable connection.")

# Find the nearest cell tower
try:
    tower_info = droid.telephonyGetCellLocation()
    tower_id = tower_info['cellLocation']['cid']
except android.AndroidError:
    print("Error finding nearest cell tower. Make sure the device has a valid SIM card and is connected to a cellular network.")

# Get information about the cell tower
try:
    tower_details = droid.telephonyGetNeighboringCellInfo()
    for tower in tower_details:
        if tower['cid'] == tower_id:
            signal_strength = tower['rssi']
except android.AndroidError:
    print("Error getting information about cell tower. Make sure the device has a valid SIM card and is connected to a cellular network.")

# Print the signal strength of the nearest cell tower
try:
    print(f"The signal strength of the nearest tower (ID: {tower_id}) is {signal_strength} dBm")
except UnboundLocalError:
    print("Error getting signal strength of nearest cell tower. Make sure the device has a valid SIM card and is connected to a cellular network.")

# Stop the phone's GPS
try:
    droid.stopLocating()
except android.AndroidError:
    print("Error stopping GPS location. Make sure GPS is enabled on the device.")