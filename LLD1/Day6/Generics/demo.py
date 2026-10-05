from typing import TypeVar

T = TypeVar('T')


def add(a: T, b: T) -> T:
    return a


print(add(2, 3))
print(add("Hi", "Hello"))
print(add(1, "Hi"))



def first(items: list[T]) -> T:
    return items[0]


numbers = first([1, 2, 3])

names = first(["Vinod", "Hello", "Amit",])

name: str = names[0];
