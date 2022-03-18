from pprint import pprint

def saisir_date() -> dict:
    print("## DATE DE NAISSANCE DU CHIARD ##")
    jour = int(input("Entrez le jour : "))
    mois = int(input("Entrez le mois : "))
    annee = int(input("Entrez l'année : "))

    return {"jour": jour, "mois": mois, "annee": annee}

def saisir_enfant() -> dict:
    print("## IDENTITÉ DU CHIARD ##")
    prenom = input("Entrez le prénom : ")
    date = saisir_date()

    return {"prenom": prenom, "anniv": date}

def saisir_employe() -> dict:
    print("## IDENTITÉ DU PARENT DU CHIARD ##")
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    nb_enfants = int(input("Entrez le nombre de chiards : "))
    tab_enf = []

    for i in range(0, nb_enfants):
        tab_enf.append(saisir_enfant())

    return {"nom": nom, "prenom": prenom, "nb_enfants": nb_enfants, "tab_enf": tab_enf}

def saisir_entreprise() -> dict:
    nb_employes = int(input("Entrez le nombre d'employés : "))
    tab_emp = []

    for i in range(0, nb_employes):
        tab_emp.append(saisir_employe())

    return {"nb_employes": nb_employes, "tab_emp": tab_emp}

def nombre_enfants_entreprise(entreprise: dict) -> int:
    return_value = 0

    for employe in entreprise["tab_emp"]:
        return_value += employe["nb_enfants"]

    return return_value

def compare_dates(d1: dict, d2:dict) -> int:
    if d1["annee"] < d2["annee"]:
        return -1
    elif d1["annee"] > d2["annee"]:
        return 1
    else:
        if d1["mois"] < d2["mois"]:
            return -1
        elif d1["mois"] > d2["mois"]:
            return 1
        else:
            if d1["jour"] < d2["jour"]:
                return -1
            elif d1["jour"] > d2["jour"]:
                return 1
            else:
                return 0

def plus_jeune_enfant(entreprise: dict) -> dict:
    return_value = {"anniv": {"annee": 0, "mois": 0, "jour": 0}}

    for employe in entreprise["tab_emp"]:
        for enfant in employe["tab_enf"]:
            if compare_dates(enfant["anniv"], return_value["anniv"]) == 1:
                return_value = enfant

    return return_value


#entreprise = saisir_entreprise()
entreprise = {
    'nb_employes': 3,
    'tab_emp': [
        {
            'nb_enfants': 1,
            'nom': 'Golo',
            'prenom': 'Henri',
            'tab_enf': [
                {
                    'anniv': {
                        'annee': 63,
                        'jour': 8,
                        'mois': 9
                    },
                    'prenom': 'blu'
                }
            ]
        },
        {
            'nb_enfants': 2,
            'nom': 'Caneur',
            'prenom': 'Henri',
            'tab_enf': [
                {
                    'anniv': {
                        'annee': 65,
                        'jour': 4,
                        'mois': 5
                    },
                    'prenom': 'plapla'
                },
                {
                    'anniv': {
                        'annee': 45,
                        'jour': 7,
                        'mois': 8
                    },
                    'prenom': 'pluplu'
                }
            ]
        },
        {
            'nb_enfants': 1,
            'nom': 'Dicule',
            'prenom': 'Henri',
            'tab_enf': [
                {
                    'anniv': {
                        'annee': 34,
                        'jour': 1,
                        'mois': 2
                    },
                    'prenom': 'ploplo'
                }
            ]
        }
    ]
}

pprint(entreprise)
print(nombre_enfants_entreprise(entreprise))
pprint(plus_jeune_enfant(entreprise))