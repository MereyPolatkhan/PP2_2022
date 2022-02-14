def solve(head, leg):
    chicken = int((leg - 4 * head) / (2 - 4))
    rabbit = head - chicken
    return {f'chicken: {chicken} and rabbit: {rabbit}'}

print(solve(35, 94))