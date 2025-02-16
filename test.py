import base64
import base58
import enchant

cle = "cjc1PkBNRFJfXg== SFVTWlY2RVlIQ1BaRDQzTQ== 5Bx4WuUb6dLRnHs8zZ Qc*TjcW!P$b2n! G5DUQVLFOZMGS2SNKF4HQ3A= NmZGT2dscHE3dTdPT0M= S2hkdGt5UkpZZDNQYzVO OforVZ%R36aB4k0 Q%pupNkv*vRa8S)Jv}= dNe(FSW{0@c|m$U MzRoZHBpVTJLT1E3T3lXdWI= 3wnXJDyZQhvgCs Uko1ZzhYeTJnQ25SanZW RY)OaSX6CSQa= Rat2(GF4h6L_t$MI70 5BoV5drfg1zv7Gbpye L1j-fa5YagbZl4 KBLWE3LVJZNGMUCYMJUQ==== NLEWxG&D0>NK8*rG*mT JN4HO23OGJ3WQSSINFSUUSKDO4====== 3DdZSUZnPKBeP9CuEXc3w PES%;S~g8mP*XujL_Iw{ FMEmeyT7Zs5kdTHgbo4mpG V3FXZnlXdENaYWI= GIDT9b4g)#V>CELF;O^gGy 2cNt38QgCBg9FZqhC HBK>9QE_T*SYZ 2XsTobA7zMnAYAPNk TkdZSERBTU9PR1NSPT09PQ== PDpeCUiGmDpv 2Wn1ZNUst3cUk4cRSSa5zbd|69&eK2Dqb68> JJDVKVBUK5EUUSSTK5KUIPJ5HU====== KBKFKWSLGJDEIUKMKZNFKPJ5HU====== MRXDS53FJBLXUZSSHU6Q==== VT5KYT9WLUo5flNNeTQk clVUM05WWGRwVnk9 MVYFSMLGOFMXMQSUHU6Q==== SzhSMVBDM3NOVmpmNTdv aTQ+SEpGayhqP2d5 M29HYVhPUmw4bWdVV3BrSXFLODZN 3JgACUx9CYG7Z9v8TPksz GJLWUT2PI5NESMZSKVAU6=== GJCWGYK2GZIGSVJWO5GGK=== SUFN>VM0YoRZ%v2Z8mB WnN1c3xkJk4k dDhtZTlzU3s+QE92 NBBUEYKFINVGERRTIJZA==== INBEYS2RGRJEQQ2GJRFTITSXHU====== Qm85YUFZMXJkb0gwQllTPQ== NmMdXQ&TfmNK{W!PgF)t 7W5CAuuMMt3gbcri4HWZGHfak814HvBYg N?0jJRZJ>tK2dEZG9yE6dj WnQ0YzlacXM0JFpn NEZVKMDKORBW6RRSINRWWRKUHU====== NBEXO4JWNASXO52L JIZDS2TNPBMWUSSIMV3Q==== M>uSEZZtVKXjnr|T39& csXuLNOxB|a(#GKNHs< 5CDRUCe72sanGg6hLm 2XsUvjhR16rxujBJr S1ZUU1U1SFFKQlRTND09PQ== bvZ$HNK<)CLQ4"
list_cle = cle.split()

""""
def Question_12(list_cle):
    en = enchant.Dict("en_US")
    for cle in list_cle:
        try:
            for decode_function in (base64.b64decode, base64.b32decode, base64.b16decode, base64.b85decode, base58.b58decode):
                try:
                    decoded_cle = decode_function(cle).decode('utf-8')
                except:
                    continue
            for decalage in range(26):
                resultat = ""
                for caractere in decoded_cle:
                    if 'a' <= caractere <= 'z':
                        resultat += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
                    elif 'A' <= caractere <= 'Z':
                        resultat += chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
                    else:
                        resultat += caractere
                for decode_function in (base64.b64decode, base64.b32decode, base64.b16decode, base64.b85decode, base58.b58decode):
                    try:
                        resultat = decode_function(cle).decode('utf-8')
                        print(resultat)
                    except:
                        continue
                if en.check(resultat)  is True: print(resultat)
        except:
            continue


def Question_4(cle):
    for decode_function in (base64.b64decode, base64.b32decode, base64.b16decode, base64.b85decode, base58.b58decode):
        try:
            return decode_function(cle).decode('utf-8')
        except:
            pass
    return None
"""

def main(list_cle):
    for cle in list_cle:
        try:
            for decode_function in (base64.b64decode, base64.b32decode, base64.b16decode, base64.b85decode):
                try:
                    decoded_cle = decode_function(cle).decode('utf-8')
                except:
                    continue
            print(cle)
            print(decoded_cle)
            for decalage in range(26):
                resultat = ""
                for caractere in decoded_cle:
                    if 'a' <= caractere <= 'z':
                        resultat += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
                    elif 'A' <= caractere <= 'Z':
                        resultat += chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
                    else:
                        resultat += caractere
                for decode_function in (base64.b64decode, base64.b32decode, base64.b16decode, base64.b85decode):
                    try:
                        return decode_function(resultat).decode('utf-8')
                    except:
                        continue
        except:
            continue

main(list_cle)