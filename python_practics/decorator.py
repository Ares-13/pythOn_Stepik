def trace(func):
    def wrapper(*args, **kwargs):
        print(f"\nTRACE: calling {func.__name__}() with {args} and {kwargs}\n")

        original_func = func(*args, **kwargs) # func() это say()

        # !r используется для отладки — чтобы явно видеть тип данных(!s default)
        print(f"TRACE: calling {func.__name__}() returned {original_func!r}\n")

        return original_func  # без return теряется результат и будет None

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say("Jane", "Hello, World")
