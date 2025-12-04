from simulation import Simulation
from solarSystem import SolarSystem
from sun import Sun
from planet import Planet

def main():
    solar_sys = SolarSystem()
    solar_sys.add_sun(Sun(name="MySUN", radius=5, mass=100, temp=5000, x=0, y=0))
    solar_sys.add_planet(Planet(name="OhNo", radius=17, mass=.560, distance=2, x=100, y=0, vel_x=1000, vel_y=0))
    sim = Simulation(solar_sys, 500, 500, 100)
    solar_sys.show_planets()
    sim.run()
    solar_sys.show_planets()


if __name__ == '__main__':
    main()