#!/usr/bin/env python
class Zoo:

    _kowalski_time_for_analysis = 0 # static field

    def __init__(self, zoo_name='NoName',  # making a constructor
                 visitors_count_over_year=0,
                 entrance_fee=0,
                 ice_cream_carts_count=0,
                 exotic_animal='NoAnimal',
                 ):
        self._zooName = zoo_name
        self._visitorsCountOverYear = visitors_count_over_year
        self._entranceFee = entrance_fee
        self._iceCreamCartsCount = ice_cream_carts_count
        self._exoticAnimal = exotic_animal

    def __del__(self):  # making a destructor
        print("This was deleted - ", self._zooName)

    def __str__(self):  # making tostring equivalent
        return self._zooName + " " + str(self._entranceFee) + " " + self._exoticAnimal + " " + str(self._iceCreamCartsCount) + " " + str(self._visitorsCountOverYear)

    @staticmethod
    def KowalskiAnalyze(analysis_timing):
        Zoo._kowalski_time_for_analysis += analysis_timing
        return Zoo._kowalski_time_for_analysis


def main():
    tropicarium = Zoo("Budapest's Tropicarium", 14500, 1600, 0, "Stingray")
    africarium = Zoo("Wroclaw's Africarium", 13000, 50, 3, "Capybara")
    openZoo = Zoo("Zoo di Napoli", 28000, 10, 10, "Siamang")
    print(str(tropicarium))
    print(str(africarium))
    print(str(openZoo))
    print("Kowalski, analyze!")
    print(Zoo._kowalski_time_for_analysis)
    Zoo.KowalskiAnalyze(50)
    print("Kowalski, analyze!")
    print(Zoo._kowalski_time_for_analysis)


if __name__ == '__main__':
    main()