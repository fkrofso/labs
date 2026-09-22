def transfer_time(mb, speed):
    return mb_to_bits(mb) / (speed * 1000000)

fixed_speed = 100

for size in range(100, 1001, 150):
    print(f"{size} МБ - {transfer_time(size, fixed_speed)} сек")
