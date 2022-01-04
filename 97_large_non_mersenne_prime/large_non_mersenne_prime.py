value = 1
for power in range(1, 7830458, 1):
    value = value * 2
    if len(str(value)) > 10:
        value = int(str(value)[-10:])

value = (value * 28433) + 1
print(str(value)[-10:])
