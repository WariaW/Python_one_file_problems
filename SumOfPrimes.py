
# isPrime[] : isPrime[i] is true if number is prime
# prime[] : stores all prime number less than N
# SPF[] that store smallest prime factor of number
# [for ex : smallest prime factor of '8' and '16' is '2' so we put SPF[8] = 2, SPF[16] = 2 ]


def manipulated_seive(N):
    # 0 and 1 are not prime
    isprime[0] = isprime[1] = False

    for i in range(2, N):

        # If isPrime[i] == True then i is
        # prime number
        if isprime[i] == True:
            prime.append(i)

            # A prime number is its own smallest prime factor
            SPF[i] = i

        # Remove all multiples of i*prime[j]
        # Prime[i * prime[j]] = false and put SPF of i*Prime[j] as prime[j]
        # this loop run only one time for number which are not prime
        j = 0
        while (j < len(prime) and i * prime[j] < N and prime[j] <= SPF[i]):
            isprime[i * prime[j]] = False

            SPF[i * prime[j]] = prime[j]

            j += 1


if __name__ == "__main__":

    T = input()
    N = []
    for i in range(0, int(T)):
        N.append(int(input()))

    for n in N:
        isprime = [True] * n
        prime = []
        SPF = [None] * (n)
        manipulated_seive(n)
        i = 0
        while n - prime[i] not in prime:
            i += 1
        print(prime[i], (n - prime[i]))
