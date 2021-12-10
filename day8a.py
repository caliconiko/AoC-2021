with open("day8.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def str_intersect(strs):
    return set(strs[0]).intersection(*[set(s) for s in strs[1:]])

def part2():
    tot=0

    for l in lines:
        dig = l.split(" | ")[0].split()
        fou = l.split(" | ")[1].split()

        known = {}

        seg6 = []
        seg5 = []
        
        for d in dig:
            match len(d):
                case 2:
                    known[1] = d
                case 4:
                    known[4] = d
                case 3:
                    known[7] = d
                case 7:
                    known[8] = d
                case 6:
                    seg6.append(d)
                case 5:
                    seg5.append(d)

        
        bot_r = str_intersect([known[1]]+seg6)
        top_r = set(known[1])-bot_r
        right = bot_r.union(top_r)

        top = set(known[7])-set(known[1])
        rows = str_intersect(seg5)
        mid = rows.intersection(known[4])
        bot = rows-mid-top

        left = set(known[8])-rows-set(known[1])
        top_l = left.intersection(set(known[4]))
        bot_l = left-top_l

        for s in seg6:
            if not (set(s) - top - bot - left - right):
                known[0]=s
            elif not (set(s) - rows - left - bot_r):
                known[6]=s
            elif not (set(s) - rows - right - top_l):
                known[9]=s

        for s in seg5:
            if not (set(s) - rows - top_r - bot_l):
                known[2]=s
            elif not (set(s) - rows - right):
                known[3]=s
            elif not (set(s) - rows - top_l - bot_r):
                known[5]=s


        # print(f"{top=} {bot=} {bot_r=} {bot_l=} {top_r=} {top_l=} {mid=}")
        # print(known)

        digits = ""
        for f in fou:
            for n, segs in known.items():
                # print(set(f)==set(segs))
                if set(f)==set(segs):
                    digits+=str(n)
                    break
        tot+=int(digits)
    print(tot)