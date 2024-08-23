from operations import Birthday


objet = Birthday('2005 8 4')

objet.separate_string()
objet.cast_values()
objet.separate_values()
objet.verify_values()

print(objet.age_years())