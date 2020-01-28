from functools import reduce


if __name__ == "__main__":
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    N = int(lines[0])
    results = [[0, 0] for _ in range(N)] # in, out
    for i in range(N):
        connections = list(map(int, lines[i+1].split()))
        for j in range(N):
            results[i][1] += connections[j] # add outputs
            results[j][0] += connections[j]


    with open(file="output.txt", mode='w') as f:
        f.write('\n'.join( map(str, reduce(lambda a, b : a + b, results, []) )))
