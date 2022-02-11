#!/bin/python

from pprint import pprint

def saisir_numero(tel: dict) -> None:
    user_input = ''
    while not user_input.strip().lstrip("+0").isdigit():
        user_input = input("Entrez un code de pays : ")

    tel['code'] = int(user_input.strip().lstrip("+0"))

    user_input = ''
    while not user_input.strip().isdigit() or len(user_input.strip()) != 9 :
        user_input = input("Entrez un numéro de téléphone : ")

    tel['num'] = int(user_input.strip())

def saisir_liste_telephone() -> dict:
    tels = []

    for i in range(0,3):
        print("NUMERO {}".format(i+1))

        tel = {}
        saisir_numero(tel)
        tels.append(tel)

    return tels

def saisir_personne() -> dict:
    person = {'nom': '', 'tels': [], 'nation': ''}

    user_input = ''

    while not user_input.isalpha():
        user_input = input("Entrez un nom : ")
    person['nom'] = user_input

    tels = saisir_liste_telephone()
    person['tels'] = tels

    user_input = input("Entrez une nationalité : ")
    person['nation'] = user_input

    return person

def saisir_agenda() -> list:
    agenda = []

    user_input = 'o'
    while user_input == 'o':
        agenda.append(saisir_personne())

        user_input = ''

        while user_input != 'o' and user_input != 'n':
            user_input = input("Ajouter une personne ? (o/n) : ")

    return agenda

def afficher_nationalite(agenda: list) -> None:
    user_input = input("Saisir nationalité : ")

    results = list(filter(lambda person: person['nation'] == user_input, agenda))

    if len(results) <= 0:
        print("Personne avec cette nationalité n'a été trouvé.")
    else:
        pprint(results)

def chercher_numero(agenda: list) -> None:
    input_tel = {}
    saisir_numero(input_tel)
    results = []

    for person in agenda:
        for tel in person['tels']:
            if tel == input_tel:
                results.append(person)
                break

    if len(results) <= 0:
        print("Personne avec ce numéro n'a été trouvé.")
    else:
        pprint(results)

#agenda = saisir_agenda()
#afficher_nationalite(agenda)

agenda = [
    {
        'nom': "Mick Tanner",
        "tels": [
            {"code":33, "num":987654321},
            {"code":33, "num":321654987},
            {"code":33, "num":682531129}
        ]
    },
    {
        'nom': "Dick Rivers",
        "tels": [
            {"code":33, "num":123456789},
            {"code":33, "num":789456123},
            {"code":33, "num":681137121}
        ]
    },
    {
        'nom': "Hugh Jass",
        "tels": [
            {"code":34, "num":741852963},
            {"code":34, "num":963852741},
            {"code":34, "num":678621109}
        ]
    }
]

chercher_numero(agenda)