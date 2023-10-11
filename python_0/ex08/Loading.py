from time import time
import os
def ft_tqdm(total):
    # print(os.get_terminal_size())
    start_time = time()
    line_length = os.get_terminal_size().columns - 40
    for i in total:
        percent = (i + 1) * 100 // len(total)
        percent_str = f'{percent:3}%'
        bar = "█" * ((i + 1) * (line_length ) // len(total))
        space = " " * (line_length - len(bar))
        process_bar = f'|{bar + space}|'
        curr_over_total = f'{i}/{len(total)}'
        elapsed_time = f'{time() - start_time:2.2}'
        it_per_s = f'{(i + 1) / (time() - start_time):.2f}it/s'
        print(f"\r{percent_str}{process_bar} {curr_over_total} [{elapsed_time}<{elapsed_time}, {it_per_s}]", end="")
        yield i