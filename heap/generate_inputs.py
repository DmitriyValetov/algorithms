import random
import numpy as np


def sorting_input():
    N = 10
    unordered = [random.randint(0, 100) for _ in range(N)]
    lines = []
    lines.append(f'{N}\n')
    lines.append(" ".join(map(str, unordered)))

    with open(file='input.txt', mode='w') as f:
        f.writelines(lines)


def insert_extracting_input(n_max=100, N=100):
    commands = []
    adds = 0
    extr = 0
    for _ in range(N):
        if adds > extr:
            commands.append(np.random.choice([f'0 {random.randint(0, n_max)}', '1'], size=1, p=[0.8, 0.2])[0])
            if commands[-1][0] == '0':
                adds += 1
            else:
                extr += 1
        else:
            commands.append(f'0 {random.randint(0, n_max)}')
            adds += 1

    lines = []
    lines.append(f'{N}\n')
    lines += list(map(lambda x: str(x)+'\n', commands))
    if lines[1] == '1\n':
        lines.pop(1)
        lines.append('1')

    with open(file='input.txt', mode='w') as f:
        f.writelines(lines)


def slide_window_mins(N_min, N_max, K_min, K_max):
    N = random.randint(N_min, N_max)
    K = random.randint(K_min, K_max)
    if K > N:
        k = N
        
    numbers = [random.randint(0, 100) for _ in range(N)]

    lines = []
    lines.append(f"{N} {K}\n")
    lines.append(" ".join(map(str, numbers)))

    with open(file='input.txt', mode='w') as f:
        f.writelines(lines)


if __name__ == "__main__":
    # sorting_input()
    # insert_extracting_input()
    slide_window_mins(10, 100, 10, 15)