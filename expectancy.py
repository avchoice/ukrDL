coeffs = [1.28, 1.18, 1.11, 1.0, 0.71]
N = 36.0
DL = 6.0
print(f"1-5: {int(round(coeffs[0]*N*(1-DL/10), 0))}")
print(f"6-10: {int(round(coeffs[1]*N*(1-DL/10), 0))}")
print(f"11-15: {int(round(coeffs[2]*N*(1-DL/10), 0))}")
print(f"16-30: {int(round(coeffs[3]*N*(1-DL/10), 0))}")
print(f"31+ and UR: {int(round(coeffs[4]*N*(1-DL/10), 0))}")