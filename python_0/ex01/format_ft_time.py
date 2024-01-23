from time import time, localtime, strftime

epoch = localtime(0)
current_time = time()
since_epoch = localtime(current_time)
print(f"Seconds since {strftime('%B %-d %Y', epoch)}: {current_time} or {float(current_time):.2e} in scientific notation")
print(f"{strftime('%b %-d %-Y', since_epoch) }")


# print(epoch)
# print(current_time)

# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$