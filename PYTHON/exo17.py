from pprint import pprint

mes_sites = {
    0: {
        "nom": "Mon super site",
        "url": "hhtps://monsupersite.com",
        "utilisateurs": [
            {
                "nom": "Germain",
                "prenom": "Philibert",
                "date_naissance": "1984-12-12",
                "nombre_abonnes": 87621,
            },
            {
                "nom": "Kaas",
                "prenom": "Patricia",
                "date_naissance": "1978-03-26",
                "nombre_abonnes": 124,
            },
            {
                "nom": "Pipoude",
                "prenom": "Serges",
                "date_naissance": "1999-01-03",
                "nombre_abonnes": 7761287,
            }
        ]
    },
    1: {
        "nom": "Mon site génial",
        "url": "hhtps://monsitegenial.com",
        "utilisateurs": [
            {
                "nom": "Sbai",
                "prenom": "Nadia",
                "date_naissance": "1978-04-01",
                "nombre_abonnes": 7627,
            },
            {
                "nom": "Koch",
                "prenom": "Christine",
                "date_naissance": "2001-12-07",
                "nombre_abonnes": 8727193,
            }
        ]
    },
}

# EXO 1 ---------------------------------------------
new_user = {"nom": "Dupont", "prenom": "Alice", "date_naissance": "1990-05-15", "nombre_abonnes": 500}
mes_sites[0]["utilisateurs"].append(new_user)
pprint(mes_sites)



# EXO 2 -----------------------------------------------
for site in mes_sites.values():
    site["utilisateurs"] = [
        user for user in site["utilisateurs"]
        if user["nom"] != "Kaas"
    ]
pprint(mes_sites)



# EXO 3 -----------------------------------------------
sum = 0
for site in mes_sites.values():
    for user in site["utilisateurs"]:
        sum += user["nombre_abonnes"]
print(sum)



# EXO 3 -----------------------------------------------
from datetime import datetime, date

sum_age = 0
sum_user = 0
today = date.today()
birth = datetime.strptime(user["date_naissance"], "%Y-%m-%d").date()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day) )
for site in mes_sites.values():
    for user in site["utilisateurs"]:
        user_birth = birth
        user_age = age
        sum_age += user_age
        sum_user +=1
avg_age = sum_age / sum_user
print(f"Moyenne d'âge: {avg_age} ans")