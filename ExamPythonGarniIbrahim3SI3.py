#Scripting Python
#Garni Ibrahim
#3SI3

#Importation des modules nécessaires
import os
import time
import socket
import base64
import base58
import webcolors
import enchant

#initialisation du serveur et du port
host = "148.113.42.34"
port = 17936


#Fonction pour récuperer les questions et y répondre

def Question_3(resp):
    return str(eval(resp[resp.index("Quel est le résultat de ") + len("Quel est le résultat de "): - 2 ]))
    
def Question_4(resp):
    resp = resp[resp.index("message: ")+ len("message: "):]
    for decode_function in (base64.b64decode, base64.b32decode, base64.b16decode, base64.b85decode, base58.b58decode):
        try:
            return decode_function(resp).decode('utf-8')
        except:
            pass
    return None

def Question_5(resp):
    resp = bytes.fromhex(resp[resp.index("majuscule: ")+len("majuscule: "):]).decode('utf-8')
    resp_morse_decoded = []
    for letter in resp.split() :
        resp_morse_decoded.append(morse_dict[letter])
    return ''.join(resp_morse_decoded)

def Question_6(resp):
    resp = bytes.fromhex(resp[resp.index("majuscule: ")+len("majuscule: "):]).decode('utf-8')
    resp_braille_decoded = []
    for letter in resp.split() :
        resp_braille_decoded.append(braille_dict[letter])
    return ''.join(resp_braille_decoded)

def Question_7(resp):
    return webcolors.rgb_to_name(rgb_triplet=list(map(int, resp[resp.index("RGB (")+len("RGB ("):resp.index(") ?")].split(','))), spec='css3')

def Question_8(resp):
    return int(resp[resp.index("la question ")+len("la question "):])-1

def Question_9(resp):
    indice = int(resp[resp.index("dernière lettre du ")+len("dernière lettre du "):resp.index("ème mot ")])
    liste_mot = resp[resp.index("liste: ")+len("liste: "):].split()
    return liste_mot[indice-1][-1]

def Question_10(reponse):
    resp = ""
    for i in range(len(reponse)):
        resp += reponse[i] + "_"
    return resp[:-1]

def Question_11(resp):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    en = enchant.Dict("en_US")
    best_guess = None
    resp = resp[resp.index("message: ")+len("message: "):]
    for i in range(26):
        mot_decod = ""
        for j in range(len(resp)):
            indice = alphabet.index(resp[j]) + i
            if indice >= 26 : indice -= 26
            else : pass
            mot_decod += alphabet[indice]
        if en.check(mot_decod) is True: return mot_decod
        suggestions = en.suggest(mot_decod)
        if suggestions: best_guess = suggestions[0]
        else : pass
    return best_guess if best_guess else None

def Question_12(resp):
    resp = resp[resp.index("message: ")+len("message: "):]
    for decode_function in (base64.b64decode, base64.b32decode, base64.b16decode, base64.b85decode, base58.b58decode):
        try:
            decoded_resp = decode_function(resp).decode('utf-8')
        except:
            continue
    for decalage in range(26):
        resultat = ""
        for caractere in decoded_resp:
            if 'a' <= caractere <= 'z':
                resultat += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
            elif 'A' <= caractere <= 'Z':
                resultat += chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
            else:
                resultat += caractere
        for decode_function in (base64.b64decode, base64.b32decode, base64.b16decode, base64.b85decode, base58.b58decode):
            try:
                return decode_function(resultat).decode('utf-8')
            except:
                continue

# Dictionnaire de conversion Morse et Braille

morse_dict = { '.-': 'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E',
    '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K',
    '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q',
    '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W',
    '-..-':'X', '-.--':'Y', '--..':'Z'
}

braille_dict = {
    '⠁': 'A', '⠃': 'B', '⠉': 'C', '⠙': 'D', '⠑': 'E', '⠋': 'F', 
    '⠛': 'G', '⠓': 'H', '⠊': 'I', '⠚': 'J', '⠅': 'K', '⠇': 'L', 
    '⠍': 'M', '⠝': 'N', '⠕': 'O', '⠏': 'P', '⠟': 'Q', '⠗': 'R', 
    '⠎': 'S', '⠞': 'T', '⠥': 'U', '⠧': 'V', '⠺': 'W', '⠭': 'X', 
    '⠽': 'Y', '⠵': 'Z'
}

#Fonction principale pour lancer le test
def ExamPython():
    try:
        reponse =  ["ibrahim/garni/3SI3", "16/02"]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        for i in range(12):
            resp=s.recv(1024)
            resp = resp.decode()
            print(resp)
            if i == 2:
                reponse.append(Question_3(resp))
            elif i == 3 :
                reponse.append(Question_4(resp))
            elif i == 4:
                reponse.append(Question_5(resp))
            elif i == 5:
                reponse.append(Question_6(resp))
            elif i == 6:
                reponse.append(Question_7(resp))
            elif i == 7:
                reponse.append(reponse[Question_8(resp)])
            elif i == 8:
                reponse.append(Question_9(resp))
            elif i == 9:
                reponse.append(Question_10(reponse))
            elif i == 10:
                reponse.append(Question_11(resp))
            elif i == 11:
                reponse.append(Question_12(resp))
            s.sendall(reponse[i].encode())
        resp = s.recv(1024)
        print(resp.decode())
        return True
    except Exception as e :
        print(f"Echec : {e}")
        os.system("clear")
        s.close()

#Fonction principale qui lance le test tant que l'examen n'est pas réussi
def main():
    while not ExamPython():
        time.sleep(2)

main()