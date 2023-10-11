from time import time, strftime

print("Seconds since January 1, 1970: ", end ="")
print(f"{time():,}", end ="")
print(" or ", end="")
print("%.2e"%time(), end="")
print(" in scientifice notation")
## todo second line
print(strftime("%b %d %Y"))

# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $>``