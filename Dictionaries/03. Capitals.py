def data():
    counties = input().split(", ")
    capitals = input().split(", ")
    result = dict(zip(counties, capitals))

    for key, value in result.items():
        print(f"{key} -> {value}")


data()


