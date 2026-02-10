import sys

TaAge = 23
AsAge = 42
my_age = str(TaAge + AsAge) + "\n"

sys.stdout.buffer.write(my_age.encode())