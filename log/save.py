

def get_average(w, l, t):
    if w + l == 0:
        return 0
    return t / (w + l)

def get_ratio(w, l):
    if w == 0:
        return 0
    return w / (w + l)

def save(mappy, mappy2, mappy3):
    file = open("save.txt", 'w')

    for key in mappy:
        w = mappy[key]
        l = mappy2[key]
        t = mappy3[key]
        average = get_average(w, l, t)
        ratio = get_ratio(w, l)
        file.write(f"{key} w: {w} l: {l} average: {average} ratio: {ratio}\n")

    file.close()
