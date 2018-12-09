nums = open('gen5.out').readlines()

for i in range(len(nums)):
    x = nums[i].rstrip()
    if "jest" in x: print(i); continue
    if x == "Koniec.": continue
    assert "dzien roku" in x

