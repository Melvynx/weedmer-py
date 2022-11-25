from enigma.machine import EnigmaMachine


def cipher(rotors, reflector, ring_setting, plugboard_settings, key, message):
    machine = EnigmaMachine.from_key_sheet(
        rotors=rotors,
        reflector=reflector,
        ring_settings=ring_setting,
        plugboard_settings=plugboard_settings)
    machine.set_display(key)
    return machine.process_text(message)

