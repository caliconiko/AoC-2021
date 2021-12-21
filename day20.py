import numpy as np

with open("day20.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def pad(a:np.array, val=0):
    wat = 0 if val==0 else 1
    w = np.where(a==wat)

    i_min = np.min(w[0])
    i_max = np.max(w[0])

    j_min = np.min(w[1])
    j_max = np.max(w[1])

    a = a[i_min:i_max+1, j_min:j_max+1]
    return np.pad(a, 3, mode="constant", constant_values=val)

def print_image(img:np.array):
    p = ""

    for l in img:
        for n in l:
            p+="#" if n==1 else "."
        p+="\n"

    print(p)

def part1():
    ...
    sections = raw.split("\n\n")

    algorithm = tuple(int(n) for n in sections[0].replace("\n", "").replace("#", "1").replace(".", "0"))

    image = np.array([[int(n) for n in l]for l in sections[1].replace("#", "1").replace(".", "0").splitlines()])

    the_fucking_void = 0

    for _ in range(2):
        image=pad(image, val=the_fucking_void)
        count=0
        next_image=np.full(image.shape,the_fucking_void, image.dtype)
        for i in range(image.shape[0]-2):
            for j in range(image.shape[1]-2):
                # print_image(image[i:i+3, j:j+3])
                # print("___")
                count+=1
                rows = np.ravel(image[i:i+3, j:j+3])

                b_str = "".join([str(n) for n in rows])
                b_num = int(b_str, 2)

                next_image[i+1, j+1] = algorithm[b_num]

        if the_fucking_void == 0:
            the_fucking_void = algorithm[0]
        else:
            the_fucking_void = algorithm[-1]
        # print(count)
        image=next_image
        image=image[1:-1,1:-1]
        # print(the_fucking_void)

    print_image(image)
    print(np.sum(image))

def part2():
    ...
    sections = raw.split("\n\n")

    algorithm = tuple(int(n) for n in sections[0].replace("\n", "").replace("#", "1").replace(".", "0"))

    image = np.array([[int(n) for n in l]for l in sections[1].replace("#", "1").replace(".", "0").splitlines()])

    the_fucking_void = 0

    for _ in range(50):
        image=pad(image, val=the_fucking_void)
        count=0
        next_image=np.full(image.shape,the_fucking_void, image.dtype)
        for i in range(image.shape[0]-2):
            for j in range(image.shape[1]-2):
                # print_image(image[i:i+3, j:j+3])
                # print("___")
                count+=1
                rows = np.ravel(image[i:i+3, j:j+3])

                b_str = "".join([str(n) for n in rows])
                b_num = int(b_str, 2)

                next_image[i+1, j+1] = algorithm[b_num]

        if the_fucking_void == 0:
            the_fucking_void = algorithm[0]
        else:
            the_fucking_void = algorithm[-1]
        # print(count)
        image=next_image
        image=image[1:-1,1:-1]
        # print(the_fucking_void)

    print_image(image)
    print(np.sum(image))
part2()