def fibonacci(lista):
    sig = lista[-1] + lista[-2]
    if sig <= 10000:
        lista.append(sig)
        fibonacci(lista)

#Principal
lista_fibo = [0, 1]
fibonacci(lista_fibo)

print(lista_fibo)