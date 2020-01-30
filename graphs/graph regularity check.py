
if __name__ == "__main__":
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    vertexes_num, edges_num = map(int, lines[0].split())
    degrees = [0 for _ in range(vertexes_num)] # in and out
    for i in range(edges_num):
        v_from, v_to = map(int, lines[i+1].split())
        degrees[v_from-1] += 1
        degrees[v_to-1]   += 1

    degrees = set(degrees)

    with open(file="output.txt", mode='w') as f:
        f.write("YES" if len(degrees)==1 else "NO")