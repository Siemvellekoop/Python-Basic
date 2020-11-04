import time
# Importeert de "time" functie zodat deze gebruikt kan worden.

import random
# Importeert de "random" functie zodat deze gebruikt kan worden.

hour = random.randrange(0, 23)
minute = random.randrange(0, 60)
second = random.randrange(0, 60)
# Door random.randrange te gebruiken, word er een random getal gegenereerd om daar vervolgens de getallen bij op te tellen.

while (hour < 24):
    second += 1
    time.sleep(1)
    # Als het onder 24 uur is word er telkens een seconde bij opgetelt

    if (second >= 59):
        second = 0
        minute += 1
    # Zodra hij de 60 seconden bereikt, word er 1 minuut bij opgetelt

    if (minute >= 59):
        minute = 0
        hour += 1
    # Zodra hij de 60 minuten bereikt, word er 1 uur bij opgetelt

print(str(hour) + ":" + str(minute) + ":" + str(second))
# Dit toont de uren op het scherm via de print functie 