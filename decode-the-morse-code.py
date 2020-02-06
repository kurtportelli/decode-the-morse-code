def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return ' '.join(
        ''.join(MORSE_CODE[char] for char in word.split())
        for word in morse_code.strip().split('   ')
    )
