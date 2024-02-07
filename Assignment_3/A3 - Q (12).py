# Write   a   program   to   add   first   seven   terms   of   the   following   series   using   a   for   loop:
# 1/1! + 2/2! + 3/3!+...+n/n!

fact=1
answer=0
for i in range(1,8):
    fact=fact*i
    answer=i/fact+answer
print(answer)