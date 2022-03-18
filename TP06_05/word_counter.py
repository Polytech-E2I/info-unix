from pprint import pprint

string = " je crois ce que je dis et je fais ce que je crois "
word_list = string.strip().split(" ")
string_dict = {item:word_list.count(item) for item in word_list}

string_dict_tab = []

for item in string_dict:
    string_dict_tab.append({item: string_dict[item]})

pprint(string_dict_tab)