s = input()

if s.count("[") != 1 or s.count("]") != 1:
    raise ValueError("Помилка структури")

l, r = s.find("["), s.find("]")
if l > r:
    raise ValueError("Невірний порядок")

content = s[l + 1 : r]
print(s[: l + 1] + "***" + s[r:])
print(f"{content}; {len(content)}")
