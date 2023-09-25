import requests
import datetime as dt
import time
import smtplib

# Define the latitude and longitude of your location
# https://www.latlong.net/ to find the latitude and longitude of your location
MY_LAT = 51.344774
MY_LNG = 0.714665

# Function to check if the ISS is overhead
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    # Check if the ISS is within 5 degrees of your location
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and \
            MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True

# Function to check if it's nighttime at your location
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    # Check if it's nighttime (after sunset or before sunrise)
    if time_now >= sunset or time_now <= sunrise:
        return True

# Main loop
while True:
    time.sleep(60)  # Sleep for 60 seconds

    # Check if the ISS is overhead and it's nighttime
    if is_iss_overhead() and is_night():
        my_gmail = "Your Email Address"
        password = "Your Password Goes Here"

        # Send an email notification
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=password)
            connection.sendmail(from_addr=my_gmail,
                                to_addrs="Your Email Address",
                                msg="Subject: Look up\n\nISS is overhead"
                                )
