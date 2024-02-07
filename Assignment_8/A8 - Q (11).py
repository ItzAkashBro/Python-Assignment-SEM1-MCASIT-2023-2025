# Write a Python program to get the top three items in terms of cost in a shop.
# d1={'dress':23,'pant':45,'shoe':12,'bungle':55,'book':8}
# output:
# bungle  55
# pant    45
# dress   23

d1 = {'dress': 23, 'pant': 45, 'shoe': 12, 'bungle': 55, 'book': 8}
for item, cost in sorted(d1.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"{item:<8} {cost}")