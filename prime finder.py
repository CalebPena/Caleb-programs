primes=[2]
not_primes=[1]
tn=int(input('what number do you want to find primes to?\n'))
for i in range(10):
    if primes[-1]**2<tn:
        d=int(tn/primes[-1])
        for i in range(d):
            if primes[-1]*i not in not_primes:
                not_primes.append(primes[-1]*i)
    for i in range(primes[-1]**2):
        if i not in not_primes:
            primes.append(i)
print(not_primes)
print(primes)
