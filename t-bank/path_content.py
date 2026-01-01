def routes_func():
    # Чтение количества маршрутов
    N = int(input().strip())
    routes = []

    for _ in range(N):
        line = input().strip().split()
        path = line[0]
        content = " ".join(line[1:])
        routes.append((path, content))

    # Чтение количества переходов
    M = int(input().strip())
    transitions = [input().strip() for _ in range(M)]

    for t in transitions:
        matched = False
        for route, content in routes:
            route_parts = route.split("/")
            t_parts = content.split("/")

    if not matched:
        print("404 Not Found")


routes_func()
