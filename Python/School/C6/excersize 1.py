punctuation = ",.;:-?!()"
s = input("input a string : ").lower()
for i in punctuation:
    if i in s:
        s=s.replace(i, "")
print(s)