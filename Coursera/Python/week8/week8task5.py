from functools import reduce

print(
    reduce(
        lambda a, x: a * (x ** 5),
        map(
            int,
            input().split()
        ),
        1
    )
)

