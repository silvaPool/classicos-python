def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

def fib2(n: int) -> int:
    if n < 2: #caso de base
        return n
    return fib2(n - 2) + fib2(n - 1) #caso recursivo

from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1} #nossos casos de base

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) #memoização
    return memo[n]

from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int: #mesma definição de fib2()
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1) #caso recursivo

def fib5(n: int) -> int:
    if n == 0: return n #caso especial
    last: int = 0 #inicialmente definido para fib(0)
    next: int = 1 #inicialmente definido para fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0 #caso especial
    if n > 0: yield 1#caso especial
    last: int = 0 #inicialmente definido para fib(0)
    next: int = 1  # inicialmente definido para fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next #passo principal da geração


for i in fib6(50):
    print(i)