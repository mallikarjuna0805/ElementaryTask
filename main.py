import random

class SpaceExplorer:
    def __init__(self):
        self.planets = {
            'Mars': {'description': 'A red planet with dusty landscapes.', 'part': 'Engine', 'oxygen_cost': 10},
            'Venus': {'description': 'A planet with a toxic atmosphere.', 'part': 'Hull', 'oxygen_cost': 15},
            'Jupiter': {'description': 'A gas giant with massive storms.', 'part': 'Fuel Tank', 'oxygen_cost': 20},
            'Saturn': {'description': 'A planet with beautiful rings.', 'part': 'Control System', 'oxygen_cost': 25},
            'Earth': {'description': 'Home, but not safe anymore.', 'part': None, 'oxygen_cost': 0}
        }
        self.spaceship_parts = []
        self.current_planet = 'Earth'
        self.oxygen = 100
        self.parts_needed = ['Engine', 'Hull', 'Fuel Tank', 'Control System']
        self.game_over = False

    def show_status(self):
        print(f"\nYou are on {self.current_planet}.")
        print(self.planets[self.current_planet]['description'])
        print(f"Oxygen left: {self.oxygen}")
        print(f"Spaceship parts collected: {', '.join(self.spaceship_parts)}")
        print(f"Parts still needed: {', '.join([part for part in self.parts_needed if part not in self.spaceship_parts])}")

    def travel_to_planet(self, planet):
        if planet in self.planets:
            oxygen_cost = self.planets[planet]['oxygen_cost']
            if self.oxygen - oxygen_cost > 0:
                self.current_planet = planet
                self.oxygen -= oxygen_cost
                print(f"\nYou traveled to {planet}.")
            else:
                print("\nNot enough oxygen to travel there!")
        else:
            print("\nThat planet doesn't exist!")

    def search_for_part(self):
        if self.current_planet != 'Earth':
            part = self.planets[self.current_planet]['part']
            if part and part not in self.spaceship_parts:
                print(f"\nYou found the {part}!")
                self.spaceship_parts.append(part)
            else:
                print("\nThere's nothing useful here.")
        else:
            print("\nYou can't find parts on Earth.")

    def check_victory(self):
        if set(self.spaceship_parts) == set(self.parts_needed):
            print("\nYou have collected all the spaceship parts! You repaired the spaceship and escaped!")
            self.game_over = True

    def play(self):
        print("Welcome to 'Space Explorer: Lost in Space'!")
        print("You must collect all spaceship parts before your oxygen runs out.")

        while not self.game_over and self.oxygen > 0:
            self.show_status()
            command = input("\nWhat do you want to do? (travel/search/quit): ").strip().lower()

            if command == 'travel':
                planet = input("Enter the planet you want to travel to (Mars/Venus/Jupiter/Saturn/Earth) :").strip().capitalize()
                self.travel_to_planet(planet)

            elif command == 'search':
                self.search_for_part()
                self.check_victory()

            elif command == 'quit':
                print("\nThanks for playing!")
                break

            else:
                print("\nInvalid command.")

        if self.oxygen <= 0:
            print("\nYou ran out of oxygen! Game over.")
        elif self.game_over:
            print("\nCongratulations! You escaped the deadly space journey!")

if __name__ == "__main__":
    game = SpaceExplorer()
    game.play()
