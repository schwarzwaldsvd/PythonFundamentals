from pprint import pprint as pp

country_to_capital = {'United Kingdom': 'London',
                        'Brazil': 'Brazilia',
                        'Morocco': 'Rabat',
                        'Sweden': 'Stockholm'}
def print_capitals():
    capital_to_country = {capital: country for country, capital in country_to_capital.items()}
    pp(capital_to_country)

words = ["hi", "hello", "foxtrot", "hotel"]
def print_first():
    return {x[0]: x for x in words}