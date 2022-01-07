def fact(n: int) -> int:
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)

def anagramme_pos(string: str, pos: int) -> list[str]:
    length = len(string)

    if pos < 0 or pos >= length:
        raise ValueError

    if length == 1:
        return [string]

    return_list = []

    # Define a new string without the cornerstone character
    new_string = ""
    if pos == 0:
        new_string = string[1:]
    else:
        new_string = string[:pos] + string[pos+1:]

    # Get anagrams for the new string and append them to the return list
    for i in range(len(new_string)):
        permuts = anagramme_pos(new_string, i)

        for permut in permuts:
            return_list.append(string[pos] + permut)

    return return_list

def remplir_tab_anagramme(string: str) -> list[str]:
    return_list = []
    done_letters = []

    for i in range(len(string)):
        try:
            done_letters.index(string[i])
        except ValueError:
            return_list.extend(anagramme_pos(string, i))
            done_letters.append(string[i])

    # Remove duplicates by temporarily converting to a dict
    return list(dict.fromkeys(return_list))

user_input = input("Entrez un mot : ")
print(f"{remplir_tab_anagramme(user_input)=}")
