def biologiste(s):
    t_a = 0 #1 - 2 
    a_t = 1 #2 - 3
    a_t1 = 0 #1 - 2
    a_t2 = 0 #0 - 1
    while a_t * 0.2 < s:
        a_t = 2*a_t1 - a_t2
        a_t2 = a_t1
        a_t1 = a_t
        t_a += 1
    return t_a

print(biologiste(3))