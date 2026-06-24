class Solution:
    def countPrimes(self, n: int) -> int:
        count=0
        if n<2:
            return 0
        else:
            is_prime = [True] * (n)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n, i):
                        is_prime[j] = False

            for i in range(2, n):
                if is_prime[i]:
                    count+=1
            return count
            
