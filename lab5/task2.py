s = input().strip()

if not s:
    print("Немає подій")
elif not all(c in "SFW" for c in s):
    raise ValueError("Помилка")
else:
    res = []
    curr = s[0]
    count = 1
    
    for c in s[1:]:
        if c == curr:
            count += 1
        else:
            res.append(f"{curr}{count}")
            curr = c
            count = 1
    res.append(f"{curr}{count}")
    
    print("".join(res))
