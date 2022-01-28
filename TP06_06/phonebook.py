#!/bin/python

def saisir_numero(tel: dict) -> None:
    user_input = ''
    while not user_input.strip().lstrip("+0").isdigit():
        user_input = input("Entrez un code de pays : ")

    tel['code'] = int(user_input.strip().lstrip("+0"))

    user_input = ''
    while not user_input.strip().isdigit() or len(user_input.strip()) != 9 :
        user_input = input("Entrez un numéro de téléphone : ")

    tel['num'] = user_input.strip()


agenda = []

tel = { 'code': 0, 'num': 0}

saisir_numero(tel)
print(f"{tel=}")
