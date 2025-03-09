def main():
    import sys
    import numpy as np
    
    data = sys.stdin.read().strip().split()
    if not data:
        return
    m, n = map(int, data[:2])
    H = list(map(int, data[2:2+m]))
    D = list(map(int, data[2+m:2+2*m]))
    
    total_d = sum(D)
    
    INF = 10**9
    

    dp = np.full(n+1, INF, dtype=np.int64)
    dp[0] = 0


    for hi, di in zip(H, D):

        new_dp = dp.copy()
        

        L = n - hi  # Para k < L se tiene k + hi < n
        if L > 0:

            indices = np.arange(L) + hi
            candidate = dp[:L] + di
            new_dp[indices] = np.minimum(new_dp[indices], candidate)
        
 
        if L <= n:
            candidate_n = dp[L:] + di  # Considera k de L hasta n
            candidate_n_min = candidate_n.min() if candidate_n.size > 0 else INF
            new_dp[n] = min(new_dp[n], candidate_n_min)
            
        dp = new_dp


    answer = total_d - dp[n]
    sys.stdout.write(str(answer))

if __name__ == '__main__':
    main()
