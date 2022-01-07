string = " je crois ce que je dis et je fais ce que je crois "
word_list = string.strip().split(" ")
string_dict = {item:word_list.count(item) for item in word_list}

print(f"{string_dict=}")