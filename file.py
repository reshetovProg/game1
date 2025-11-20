import re

vocabular = ('ой', 'уй')

def count_word_in_file(path, word):
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()
        listik = re.split(r"[\s\n]", text)
        counter = 0
        for i in listik:
            if i == word:
                counter += 1
        return counter

def file_copy(path):
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()
    index = path.rfind(".")
    new_path = path[:index]+"(copy).txt"
    with open(new_path, 'w', encoding='utf-8') as file:
        file.write(text)

def censore(path):
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        result_list = re.split(r"[\s\n]", text)
        for i in result_list:
            if i in vocabular:
                result_list.remove(i)
        result_text = ""
        for i in result_list:
            result_text+=i + " "
    with open("src/st(copy).txt", 'w', encoding='utf-8') as file:
        file.seek(0)
        file.write(result_text)

censore("src/st.txt")
# with open("src/st.txt", 'r', encoding='utf-8') as file:
#     print(file.read())




