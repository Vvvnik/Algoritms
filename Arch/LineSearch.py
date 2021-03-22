names = ["Володя", "Валера", "Вася", "Саша", "Антон", "Яков"]
search_for = "Антон" # что ищем

def linear_search(where, what):
    for v in enumerate(where):
        if v[1]==what:
            return v[0] #Возвращаем индекс

    return None # Возвращаем none
print( "Искомый элемент", search_for, "найдет под индексом"
, linear_search(names,search_for ))
