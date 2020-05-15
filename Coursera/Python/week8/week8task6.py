import itertools

print(
    *itertools.starmap(
        lambda x, y: (int(x) + int(y)) % 2,
        zip(
            input().split(),
            input().split()
        )
    )
)
