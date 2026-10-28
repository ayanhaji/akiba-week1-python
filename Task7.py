destination = input("Enter destination:")
distance = float(input("Enter distance in kilometers:"))
speed = float(input("Enter average speed in km/h:"))
travel_time = distance / speed
print("TRAVEL INFORMATION")
print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average speed {speed} km/h")
print(f"Estimated Travel Time: {travel_time:2f} hours")

hours = int(travel_time)
minutes = round((travel_time-hours) *60)
print(f"Travel Time: {hours} hours and {minutes} minutes")


