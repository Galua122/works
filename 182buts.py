p = int(input(f"p="))
np = int(input(f"N{p}="))
k = int(1)
N10 = int(0)
while not np == 0:
    N10 = N10 + (np % 10) * k
    k = k * p
    np = np // 10
print(f"N10 = {N10}")
