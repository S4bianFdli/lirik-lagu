import sys
import time

lirik = [
    ("I'm looking back on things I've done", 0.2),
    ("I  never wanna play the same old part", 0.2),
    ("I,ll keep you in the dark", 0.2),
    ("Now let me show on you the shape of my heart", 0.2),
    ("Looking back on things I've done", 0.2),
    ("I wash trying to be someone", 0.2),
    ("I played my part, kept you in the dark", 0.2),
    ("Now let me show you the shape of my heart", 0.2),
]

delay = [0.3, 0.3, 0.3, 0.2, 0.4, 0.3, 0.2, 0.3, 0.4]
print("=" * 50)
print("Shape Of My Heart")
print("=" * 50)
time.sleep(2)
for i, (line, delay_karakter) in enumerate(lirik):
    for karakter in line:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay_karakter)
    print()
    time.sleep(delay_karakter)