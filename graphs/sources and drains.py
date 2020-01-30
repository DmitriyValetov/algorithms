from functools import reduce


if __name__ == "__main__":
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    N = int(lines[0])
    degrees = [[0, 0] for _ in range(N)] # in, out
    for i in range(N):
        connections = list(map(int, lines[i+1].split()))
        for j in range(N):
            degrees[i][1] += connections[j] # add outputs
            degrees[j][0] += connections[j]

    sources = []
    drains = []
    for i in range(N):
        if degrees[i][0] == 0:
            sources.append(i)
        if degrees[i][1] == 0:
            drains.append(i)

    with open(file="output.txt", mode='w') as f:
        f.write(f"{len(sources)}\n")
        f.write("{}\n".format('\n'.join( list(map(lambda i: str(i+1), sources)))))
        f.write(f"{len(drains)}\n")
        f.write("{}".format('\n'.join( list(map(lambda i: str(i+1), drains)))))
