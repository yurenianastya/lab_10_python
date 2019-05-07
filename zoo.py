#!/usr/bin/env python
class Zoo:

    kowalski_time_for_analysis = 0  # static field

    def __init__(self, zoo_name='NoName',  # making a constructor
                 visitors_count_over_year=0,
                 entrance_fee=0,
                 ice_cream_carts_count=0,
                 exotic_animal='NoAnimal'):
        self._zoo_name = zoo_name
        self._visitors_count_over_year = visitors_count_over_year
        self._entrance_fee = entrance_fee
        self._ice_cream_carts_count = ice_cream_carts_count
        self._exotic_animal = exotic_animal

    def __del__(self):  # making a destructor
        print("This was deleted - ", self._zoo_name)

    def __str__(self):  # making tostring equivalent
        return self._zoo_name + ", " + str(self._entrance_fee) + ", " + self._exotic_animal + ", " + str(self._ice_cream_carts_count) + ", " + str(self._visitors_count_over_year)

    @staticmethod
    def kowalski_analyze(analysis_timing):
        Zoo.kowalski_time_for_analysis += analysis_timing
        return Zoo.kowalski_time_for_analysis


def main():
    tropicarium = Zoo("Budapest's Tropicarium", 14500, 1600, 0, "Stingray")
    africarium = Zoo("Wroclaw's Africarium", 13000, 50, 3, "Capybara")
    open_zoo = Zoo("Zoo di Napoli", 28000, 10, 10, "Siamang")
    print(str(tropicarium))
    print(str(africarium))
    print(str(open_zoo))
    print("Kowalski, analyze!")
    print(Zoo.kowalski_time_for_analysis)
    Zoo.kowalski_analyze(50)
    print("Kowalski, analyze!")
    print(Zoo.kowalski_time_for_analysis)


if __name__ == '__main__':
    main()