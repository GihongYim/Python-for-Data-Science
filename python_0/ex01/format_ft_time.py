from time import time, localtime, strftime

epoch = localtime(0)
current_time = time()
since_epoch = localtime(current_time)
print(f"Seconds since {strftime('%B %-d %Y', epoch)}: \
      {current_time} or {float(current_time):.2e} in scientific notation")
print(f"{strftime('%b %-d %-Y', since_epoch) }")


# print(epoch)
# print(current_time)
