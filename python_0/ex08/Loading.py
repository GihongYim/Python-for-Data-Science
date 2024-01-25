import os
from time import sleep


def ft_tqdm(total):
    """_summary_
        show total's process

    Args:
        total (_type_): iterable or list etc...

    Yields:
        _type_: total's iterator result
    """

    line_length = os.get_terminal_size().columns
    cnt = 1
    for i in total:
        percent = (i + 1) * 100 // len(total)
        # print(percent)
        percent_str = f'{percent:3}%'
        remain_length = line_length - len(percent_str)
        curr_over_total = f' {i}/{len(total)}'
        remain_length = remain_length - len(curr_over_total) - 2
        bar = "█" * int((cnt / len(total)) * remain_length)
        space = " " * (remain_length - len(bar))
        process_bar = f'|{bar + space}|'
        print(f"\r{percent_str}{process_bar}{curr_over_total}", end="")
        cnt += 1
        yield i


def main():
    """main function for testing ft_tqdm
    """
    for i in ft_tqdm(range(10000)):
        sleep(0.01)


if __name__ == "__main__":
    main()
