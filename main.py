meme_dict = {
            "CRINGE": "coś dziwnego lub wstydliwego",
            "LOL": "odpowiedź na coś zabawnego",
            "ROFL": "odpowiedź na żart",
            "SHEESH": "lekka dezaprobata",
            "CREEPY": "straszny, złowieszczy",
            "AGGRO": "stać się agresywnym/zły",
            }
word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

def checking():
    global word, run
    if word in meme_dict.keys():
        print(word,":", meme_dict[word])
        run = False
    else:
        print("there is no word like that in ")
        

checking()
