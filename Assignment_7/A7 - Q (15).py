# Write a Python function to check whether a number falls in a given range.

def ran(number, start, end):
    return start <= number <= end
ch, rs, re = 15, 10, 20
print(f"{ch} {'falls' if ran(ch, rs, re) else 'does not fall'} within the range [{rs}, {re}]")