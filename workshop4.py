n = int(input("จำนวนเงินที่ต้องการเก็บ: "))
m = 0
shops = 0

while True:
    shops += 1
    m += int(input(f"ร้านที่ {shops}   จำนวนเงินที่เก็บได้: "))
    if m >= n:
        print("ครบจำนวนที่กำหนดแล้ว หยุดเก็บเงินเพิ่ม")
        break
print("จบการเก็บเงินแล้ว")