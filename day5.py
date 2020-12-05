#PART 1

def calculate_row(boarding_pass):
    global row
    potential_rows = []
    for i in range(0,128):
        potential_rows.append(i)
    for letter in boarding_pass[0:7]:
        new_potential_rows = []
        halfway_point = (max(potential_rows) - min(potential_rows))/2
        if letter == 'F':
            for i in range(min(potential_rows), min(potential_rows)+ int(halfway_point)+1):
                new_potential_rows.append(i)
        elif letter == 'B':
            for i in range((min(potential_rows)+ 1 + int(halfway_point)), max(potential_rows) +1):
                new_potential_rows.append(i)
        else:
            print(letter, ' - is an error')
        potential_rows = new_potential_rows
        row = min(new_potential_rows)
    print('row = ', row)
    

def calculate_seat(boarding_pass):
    global seat
    potential_seats = []
    for i in range(0,8):
        potential_seats.append(i)
    for letter in boarding_pass[7:10]:
        new_potential_seats = []
        halfway_point = (max(potential_seats) - min(potential_seats))/2
        if letter == 'L':
            for i in range(min(potential_seats), min(potential_seats)+ int(halfway_point)+1):
                new_potential_seats.append(i)
        elif letter == 'R':
            for i in range((min(potential_seats)+ 1 + int(halfway_point)), max(potential_seats) +1):
                new_potential_seats.append(i)
        else:
            print(letter, ' - is an error')
        potential_seats = new_potential_seats
        seat = min(new_potential_seats)
    #print('seat = ', seat)
        

def calculate_seat_id(boarding_pass):
    calculate_row(boarding_pass)
    calculate_seat(boarding_pass)
    global seat_id
    seat_id = (row * 8) + seat
    return seat_id
    #print(seat_id)


boarding_passes = []
with open("aoc5.txt") as file :
    for line in file :
        boarding_passes.append(line)

seat_id_list = []
for bp in boarding_passes:
    id_no = calculate_seat_id(bp)
    seat_id_list.append(id_no)
    
max(seat_id_list)

# PART 2

seat_id_list = sorted(seat_id_list)

full_range_list = list(range(min(seat_id_list), max(seat_id_list)))

for i in full_range_list:
    if i in seat_id_list:
        continue
    else:
        print(i)
