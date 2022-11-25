# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from encrypt import cipher

message = "Les troupes britanniques sont entrees a Cuxhaven a quatorze heures le six mai Desormais tout le trafic radio cessera je vous souhaite le meilleur Fermeture pour toujours tout le meilleur au revoir."


def get_cypher(msg):
    return cipher("I V IV", "B", [13, 15, 11], "NX EC RV GP SU DK IT FY BL AZ", "gyd", msg)


def exercise_1():
    # Use a breakpoint in the code line below to debug your script.

    cypher_message = get_cypher(message)

    print(cypher_message)  # Press ⌘F8 to toggle the breakpoint.

    return cypher_message


def exercise_2(data):
    # Use a breakpoint in the code line below to debug your script.

    cypher_message = get_cypher(data)

    print(cypher_message)  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    msg = exercise_1()
    exercise_2(msg)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
