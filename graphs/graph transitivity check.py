from functools import reduce


def no_transirivity(u, v, connectivity_matrix):
    for w in range(len(connectivity_matrix)):
        if connectivity_matrix[v][w]>0 and not connectivity_matrix[u][w]:
            return True

if __name__ == "__main__":
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    N = int(lines[0])
    results = [[0, 0] for _ in range(N)] # in, out
    connectivity_matrix = [list(map(int, line.split())) for line in lines[1:] ]
    answer = "YES"
    for i in range(N):
        for j in range(N):
            if connectivity_matrix[i][j]:
                if no_transirivity(i,j,connectivity_matrix):
                    answer = "NO"
                    break
        
        if answer == "NO":
            break


    with open(file="output.txt", mode='w') as f:
        f.write(answer)
