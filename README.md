# SMTP_ISSOverhead

This uses the API at http://api.open-notify.org/iss-now.json to acquire the latitude and longitude of the international space station. The ISS latitude and longitude are compared to those of the user, with a margin of 5 degrees, then checks if the time of appearance overhead occurs between sunset and sunrise which are acquired from https://api.sunrise-sunset.org/json. If the ISS is overhead and it is night time an alert to the users' email is sent.
