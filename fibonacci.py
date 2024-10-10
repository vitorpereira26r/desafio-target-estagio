
def is_in_fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    if n in fib_seq:
        return f"O número {n} pertence a sequência fibonacci"
    else:
        return f"O número {n} não pertence a sequência fibonacci"


n = int(input("Digite um número: "))
print(is_in_fibonacci(n))