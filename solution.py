# Input is the encrypted ransom note
# Expected return value is a string
# Skriv din egen docstring till funktionen: vilket cipher är det, och hur fungerar det?

# Ciphret som används verkar vara en modifierd version av ett atbash-cipher som även inkluderar siffror.
# Ciphret fungerar att det ersätter bokstäver med samma värde i ett spegelvänt alfabet. Ciphret vi har att göra med i applicerar bara för gemener och siffrorna 0-9.

import string

krypterad_anteckning = 'Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv. Sprxpz 24 yrgxlrm uöiv nåmwzt po 90:99, zmmzih häoqvi er pfmwfkktrugvimz kå mägvg!'


def solution(note):
    # Första halvan av funktionen skapar upp listor och bygger ett cipher-bibliotek med nyckel:värde par beståendes av hela nycklarna består av alfabetet och siffrorna 0-9, värdena består av alfabetet omvänt och siffrorna omvänt.
    # Andra halvan loopar över paremetern note som är en sträng. I loppen jämför vi varje tecken i strängen och ser om det finns i vårt cipher bibliotek eller inte.
    # Finns värdet i biblioteket läggs motsvarande tecken ifrån nyckel:värde paret in i en lista, finns tecknet inte så läggs bara tecknet så som det är in i samma lista i följd.
    # När hela strängen har loopats över omvandlas den tillfälliga listan till en sträng som skrivs ut och returneras.

    # Första halvan
    alfabet = []
    omvant_alfabet = []
    for bokstav in string.ascii_lowercase:
        alfabet.append(bokstav)
        omvant_alfabet.insert(0, bokstav)

    nummer = []
    omvant_nummer = []
    for siffra in string.digits:
        nummer.append(siffra)
        omvant_nummer.insert(0, siffra)

    dictionary = {}
    for i in range(len(alfabet)):
        dictionary[alfabet[i]] = omvant_alfabet[i]
    for i in range(len(nummer)):
        dictionary[nummer[i]] = omvant_nummer[i]

    # Andra halvan
    
    avkrypterad_anteckning_lista = []
    for tecken in note:
        if tecken in dictionary:
            avkrypterad_anteckning_lista.append(dictionary[tecken])
        else:
            avkrypterad_anteckning_lista.append(tecken)
    avkrypterad_anteckning = "".join(avkrypterad_anteckning_lista)
    return avkrypterad_anteckning

if __name__ == "__main__":
    avkrypterad_anteckning = solution(krypterad_anteckning)
    print(f"Krypterad anteckning: {krypterad_anteckning}")
    print(f"Avkrypterat: {avkrypterad_anteckning}")

def test_solution_1():
    assert solution('abba') == 'zyyz'

def test_solution_2():
    assert solution('Aoo blfi yzhv ziv yvolmt gl fh!') == 'All your base are belong to us!'

def test_solution_3():
    assert solution('Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv. Sprxpz 24 yrgxlrm uöiv nåmwzt po 90:99, zmmzih häoqvi er pfmwfkktrugvimz kå mägvg!') == 'Era servrar är låsta och backuperna är raderade. Skicka 75 bitcoin före måndag kl 09:00, annars säljer vi kunduppgifterna på nätet!'

def test_solution_4():
    in_data = ':-?"åÄö'
    ut_data = solution(in_data)
    assert in_data == ut_data                  # eget test 1, bara specialtecken och annat om inte ska finnas i ett atbash cipher, samma sträng vi skickar in bör vara den vi får tillbaka.

def test_solution_5():
    assert solution('1-2==3') == '8-7==6'      # eget test 2, faller den av mattematiska operatorer

def test_solution_6():
    assert solution('   ') == '   '            # eget test 3, vad händer med bara mellanslag?
