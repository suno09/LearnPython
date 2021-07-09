def countdown(n):
    print("Counting down from", n)
    while n >= 0:
        print(True)
        newvalue = (yield n)
        print("***", newvalue)
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1
        print("*" * 20)


c = countdown(5)
print('starting...')
for x in c:
    print(x)
    if x == 5:
        c.send(3)
