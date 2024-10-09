
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    my_planets=[]
    for planet in planets:
        if planet['isPlanet']:
            name = planet["englishName"]
            mass = planet["mass"]["massValue"]
            orbit_period =planet['sideralOrbit']
            my_planets.append([name,mass,orbit_period])
    print(my_planets)
    return my_planets
    
def find_heaviest_planet(planets):
    heaviest_planet=''
    heaviest_weight=0
    for i in range(len(planets)):
        if planets[i][1]>heaviest_weight:
            heaviest_planet=planets[i][0]
            heaviest_weight=planets[i][1]
        
    return heaviest_planet,heaviest_weight

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name}, which weighs {mass}.")

