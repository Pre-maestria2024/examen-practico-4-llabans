from queue import PriorityQueue
from queue import Queue
import sys
sys.setrecursionlimit(10**7)

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    
    n, k = map(int, input_data[:2])
    edges = input_data[2:]

    if n == 0 or k == 0:
        print(0)
        return

    adj = [[] for _ in range(n)]
    idx = 0
    for _ in range(n-1):
        u = int(edges[idx])
        v = int(edges[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    answer = [0]  # Lista para mutar en dfs

    def dfs(u, parent):
        """
        Retorna la distancia (en aristas) máxima que puede alargarse
        desde u hacia abajo sin chocar con un grupo ya formado.
        
        Si se forma un grupo en u, se retorna -1 para indicar
        que este nodo (y su cadena de k nodos) quedan usados.
        """
        bestDist = 0  # la mejor distancia de un hijo + 1
        
        for c in adj[u]:
            if c == parent:
                continue
            dist_child = dfs(c, u)
            if dist_child != -1:
                bestDist = max(bestDist, dist_child + 1)
        
        if bestDist >= k-1:
            answer[0] += 1
            return -1  # Marcamos u como "usado"
        else:
            return bestDist

    dfs(0, -1)

    print(answer[0])

if __name__ == '__main__':
    main()
