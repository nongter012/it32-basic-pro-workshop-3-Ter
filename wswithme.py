# name = input("ชื่อที่ใช้กรอก: ")

# def i(name):
#     u = 0
#     for m in name:
#         u += 1
#     return u

# name_count = i(name)
# print(f"{name} มี {name_count} คำ")




# name_list = ["Ter", "Nine"]
# name_list.append("Dream")
# name_list.append(67) # เพิ่มได้ทีละ 1 ในตัวท้าย
# print(name_list)

# name_list = ["Ter", "Nine"]
# name_list.pop() # ลบแค่ตัวหลังหรือท้ายสุด ท้ายอยากลบตามตำแหน่ง ระบุลำดับใส่ใน()
# print(name_list)

# # .insert(ลำดับ, "คำ") เพิ่มตรงไหนก็ได้ตามลำดับที่อยาก

# # .remove("word") ลบตัวที่ต้องการลบ

m = []
max = 0

34
while True:
    number = (input("จำนวนเลขที่เก็บได้: "))
    if number == "stop":
        break
    else: m.append(int(number))
for c in m:
    if c > max:
        max = c
print(f"ตัวเลขที่มากที่สุดในลิสคือ {max}")
