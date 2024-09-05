numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for current_num in range(2, len(numbers)+1):
    is_prime = True
    for _delitel in range(2, current_num):
        if current_num % _delitel == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(current_num)
    if is_prime == False:
        not_primes.append(current_num)
print('Primes:', primes)
print('Not Primes:', not_primes)
