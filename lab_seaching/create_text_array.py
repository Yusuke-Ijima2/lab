with open('text_array_vegetable_juice.txt', 'r') as f:
    kw_list = f.read().split("\n")
    # print(kw_list)
    q_list = []
    w_list = []
    e_list = []
    for a in kw_list:
        # print(a[0])
        if a[0] == "q":
            q_list.append(a.lstrip("q"))
        if a[0] == "w":
            w_list.append(a.lstrip("w"))
        if a[0] != "q" and a[0] != "w": e_list.append(a)
print(q_list)
print(w_list)
print(e_list)
