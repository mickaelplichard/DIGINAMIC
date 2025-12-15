from datetime import date

prenom = "bobby"
age = 30
date_naissance = date(1992, 5, 26)

print(f"Bonjour, je m'appelle {prenom}, j'ai {age:04d} ans, je suis né le {date_naissance.strftime('%b %d %Y')}.")