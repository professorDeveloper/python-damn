for i in range(1, 101):
    counter = 0
    for j in range(1, 101):
        if i % j == 0:
            counter += 1
    if counter == 2:
        print(i)
