import requests
import json



def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet["englishName"]
            mass = planet["mass"]["massValue"]
            orbit_period =planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()
"""
Expected Outcome:

Planet: Uranus, Mass: 8.68127, Orbit Period: 30685.4 days
Planet: Neptune, Mass: 1.02413, Orbit Period: 60189.0 days
Planet: Jupiter, Mass: 1.89819, Orbit Period: 4332.589 days
Planet: Mars, Mass: 6.41712, Orbit Period: 686.98 days
Planet: Mercury, Mass: 3.30114, Orbit Period: 87.969 days
Planet: Saturn, Mass: 5.68336, Orbit Period: 10759.22 days
Planet: Earth, Mass: 5.97237, Orbit Period: 365.256 days
Planet: Venus, Mass: 4.86747, Orbit Period: 224.701 days

"""