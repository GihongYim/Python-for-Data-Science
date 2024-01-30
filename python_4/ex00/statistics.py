def ft_statistics(*args: any, **kwargs: any) -> None:
    """
        ft_statistics function args: numbers,\
            kwargs {key:value} key: name value:statistical function
    """
    functions = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
        }
    for function in kwargs.values():
        if len(args) == 0:
            print("ERROR")
            continue
        if function in functions:
            functions[function](*args)
    return None


def mean(*args: any):
    args_mean = sum(args) / len(args)
    print(f'mean: {args_mean}')


def median(*args: any):
    sorted_args = sorted(args)
    median_value = sorted_args[len(args) // 2]
    print(f'median: {median_value}')


def quartile(*args: any):
    sorted_args = sorted(args)
    quartile_values = [
        sorted_args[len(args) // 4], sorted_args[len(args) * 3 // 4]]
    quartile_values = list(map(float, quartile_values))
    print(f'quartile: {quartile_values}')


def std(*args: any):
    args_mean = sum(args) / len(args)
    deviation = list(map(lambda x: x - args_mean, args))
    variance = sum(list(map(lambda x: x ** 2, deviation))) / len(deviation)
    print(f'std: {variance ** (0.5)}')


def var(*args: any):
    args_mean = sum(args) / len(args)
    deviation = list(map(lambda x: x - args_mean, args))
    variance = sum(list(map(lambda x: x ** 2, deviation))) / len(deviation)
    print(f'var: {variance}')


def main():
    pass


if __name__ == "__main__":
    main()
