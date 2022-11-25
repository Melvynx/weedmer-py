# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from encrypt import cipher
from multiprocessing import Process
import os

message = "Les troupes britanniques sont entrees a Cuxhaven a quatorze heures le six mai Desormais tout le trafic radio cessera je vous souhaite le meilleur Fermeture pour toujours tout le meilleur au revoir."

brutforce = "XHNCUZVDUASPOPSGVGGTADINYYSCXUOECYHHHSMYZJSAWPNNERYVWKYKLHYBFCSRXMGKNZYWEEVVLIVWOBDBIYEGFKVIBBBKXHPLKYCRBAONOXTWUWGNGJGDBJHKJINIPAISJAVXINECSWTTBAQS"


def get_cypher(msg):
    return cipher("I V IV", "B", [13, 15, 11], "NX EC RV GP SU DK IT FY BL AZ", "gyd", msg)


def get_cypher_brutforce(msg, rotors, indicator):
    return cipher(rotors, "B", [16, 6, 8], "GH QW TZ RO IP AL SJ DK CN YM", indicator, msg)


def exercise_1():
    # Use a breakpoint in the code line below to debug your script.

    cypher_message = get_cypher(message)

    print(cypher_message)  # Press ⌘F8 to toggle the breakpoint.

    return cypher_message


def exercise_2(data):
    # Use a breakpoint in the code line below to debug your script.

    cypher_message = get_cypher(data)

    print(cypher_message)  # Press ⌘F8 to toggle the breakpoint.


def get_rotors_combinaison():
    rotors = ["I", "II", "III", "IV", "V"]
    result = set()

    for r in rotors:
        for r2 in rotors:
            for r3 in rotors:
                if r == r2 or r == r3 or r2 == r3:
                    continue
                l = f'{r} {r2} {r3}'
                result.add(l)

    return result


def get_indicators():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    result = set()

    for r in alphabet:
        for r2 in alphabet:
            for r3 in alphabet:
                l = f'{r}{r2}{r3}'
                result.add(l)

    return result


def try_a_rotors(data, rotor, indicator):
    for r in indicator:
        p = get_cypher_brutforce(data, rotor, r)
        if p.__contains__("METEOROLOGI"):
            print(f"SOLUTION: {p} for {rotor} and {r}")
            return

    print(f"Find nothing for rotor {rotor}")


def exercice_3(data):
    rotors = list(get_rotors_combinaison())
    indicators = list(get_indicators())

    processes = []

    p = get_cypher_brutforce(data, "IV V II", "wxt")
    print(p)

    return
    for u in rotors:
        p = Process(target=try_a_rotors, args=(data, u, indicators))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # msg = exercise_1()
    # exercise_2(msg)

    exercice_3(brutforce)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
