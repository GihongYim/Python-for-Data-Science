def ft_tqdm(total):
    """ ft_tqdm(generator) -> generator result"""
    line_length = 109
    for i in total:
        percent = (i + 1) * 100 // len(total)
        percent_str = f'{percent:3}%'
        bar = "█" * ((i + 1) * (line_length) // len(total))
        space = " " * (line_length - len(bar))
        process_bar = f'|{bar + space}|'
        curr_over_total = f'{i}/{len(total)}'
        print(f"\r{percent_str}{process_bar} {curr_over_total}", end="")
        yield i


def main():
    pass


if __name__ == "__main__":
    main()
