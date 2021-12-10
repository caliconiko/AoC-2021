import queue

q = queue.SimpleQueue()

q.put(1)
q.put(2)
q.put(3)

s = 3

def do(s):
    for _ in range(s):
        a = q.get()
        print(a)
        q.put(a)
        if a==1:
            q.put(1)
            s+=1
    return s

for i in range(3):
    s = do(s)
    print("---")

