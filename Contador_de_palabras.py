def replace_tilds(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        (",", ""),
        (".", "")
    )
    for x, z in replacements:
        s = s.replace(x, z)
    return s

def text_to_text_no_tilds(text):
    text_no_tilds = ""
    for l in text:
        text_no_tilds += replace_tilds(l)
    return text_no_tilds

def read_file(file):
    str_file = ""
    with open(file, "r") as texto:
        for t in texto:    
            str_file += t.lower()
            str_file = text_to_text_no_tilds(str_file)
        return str_file.split()
        
    
    
def find_match(texto, palabra):
    counter = 0
    palabra = palabra.lower()
    for p in texto:
        if palabra == p:
            counter += 1
    print(counter)

find_match(read_file("texto.txt"), "ruby")