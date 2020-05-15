import sys

num_steps = sys.argv[1]
num_int = int(num_steps)

for i in range(1, num_int + 1):
    print(" " * (num_int - i) + "#" * i)
