import time
 

def slope_iteration_square_root(z):
    e = 1e-6
    count = 0
    x = 10
    while abs(x**2 - z) >= e:
        count = count + 1
        print(count, x)
        x = (x + z/x) / 2
start_time = time.time()
slope_iteration_square_root(200)
end_time = time.time()
print("Slope Iteration method cost time:", (end_time-start_time)*10**3, "ms")



def interval_shrink_square_root(z):
    e=1e-6
    count = 0
    x = 10
    low = 1
    high = z
    while abs(x**2 - z) >= e:
        count = count + 1
        if x**2 < z:
            low = x
        else:
            high = x
        x = (high + low)/2
        print(count, x)
start_time = time.time()
interval_shrink_square_root(200)
end_time = time.time()
print("Interval Shrink method cost time:", (end_time-start_time)*10**3, "ms")



def binomial_division_square_root(z):

    decimal = 15
    z = z * 10 ** ( (decimal+1) * 2)

    z_seg_len = len(str(z)) //2 + 1
    z_seg = [0] * z_seg_len
    index = z_seg_len - 1
    while z > 0:
        z_seg[index] = z % 100
        z = z // 100
        index = index - 1
    print(z_seg)


    s = [0] * z_seg_len
    a = [0] * z_seg_len
    r = [0] * z_seg_len
    x = 0

    s[0] = z_seg[0]
    while True:
        a[0] = a[0] + 1
        if a[0]**2 > s[0]:
            a[0] = a[0] - 1
            break
    print(a[0])
    x = a[0]
    r[0] = s[0] - a[0] ** 2
    s[1] = r[0] * 100 + z_seg[1]

    for i in range(1, len(s)-1):
        while True:
            a[i] = a[i] + 1
            if (2 * x * 10 + a[i]) * a[i] > s[i]:
                a[i] = a[i] - 1
                break
        print(a[i])
        r[i] = s[i] - (2 * x * 10 + a[i]) * a[i]
        s[i + 1] = r[i] * 100 + z_seg[i + 1]
        x = x * 10 + a[i]
        print(x)

    x = x / 10**decimal
    print(x)

start_time = time.time()
binomial_division_square_root(200)
end_time = time.time()
print("Binomial Division method cost time:", (end_time-start_time)*10**3, "ms")


