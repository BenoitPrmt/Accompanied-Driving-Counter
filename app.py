import json

total = open('./data.json', encoding='utf-8')

total_loaded = json.load(total)

def kilometers_checking(kilometers:int)->bool:
    """Check if the kilometers is more than 3000
    Args:
        kilometers (int): kilometers to check
    Returns:
        bool: True if less than 3000, False otherwise
    """
    if kilometers >= 3000:
        return True
    else:
        return False

def kilometers_adding(kilometers:int):
    """Add kilometers to the list"""

    total_loaded['kilometers'] += kilometers

    checked = kilometers_checking(total_loaded['kilometers'])

    if checked:
        print("Vous avez atteint les 3000 kilomètres ! Félicitations !")

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(total_loaded, f, ensure_ascii=False, indent=4)


while True:
    kil = int(input("Kilomètres à ajouter : "))
    kilometers_adding(kil)
    print(f'{kil} kilomètres ajoutés -> Total : {total_loaded["kilometers"]}\nIl reste {3000 - total_loaded["kilometers"]} kilomètres à parcourir\n')