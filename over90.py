import csv

csv_reader = csv.reader(open('CR++.csv', 'r'))

# flysight data is raw elevation and needs to be corrected.
# ground_level = int(input("please enter your DZ elevation in whole meters:\n> "))

# competition definition of exit is when Vertical speed exceeds 10m/s

for row in csv_reader:
    time = row[0]
    meters = row[3]
    v_speed = row[6]
    values = [time, meters, v_speed]
    if time.isdigit():
        time = float(time)
    elif meters.isdigit():
        meters = float(meters)
    elif v_speed.isdigit():
        v_speed = float(v_speed)

    print(values)






# # flysight record will probably never be exactly 3000 in file
# def window_top():
#     window_top() = (row[3] > 2999.99 < 3000.01) + ground_level
#
#
# # flysight record will probably never be exactly 2000 in file
# def window_bottom():
#     window_bottom() = (row[3] < 2000.01 < 1999.99) + ground_level
#
#
# def time_in_window():
#     # Need to use corresponding rows of top and bottom to determine start and finish
#     window_bottom(row[0]) - window_top(row[0])
#     if time_in_window() > 90 seconds
#     # Save files in a new directory
#     append.over90
#     directory
