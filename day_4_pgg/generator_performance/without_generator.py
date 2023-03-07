import resource

def read_file(file_name):
    with open(file_name, 'r') as handle:
        lines = handle.readlines()

    return lines

# https://alx.piotr.gg/python/sales-records.csv
file_name = '../../data/sales-records.csv'
data = read_file(file_name)

for line in data:
    print(line)

print('Memory:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('User Time:', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
print('System Time:', resource.getrusage(resource.RUSAGE_SELF).ru_stime)

"""
Memory: 208273408 = 198 MB
User Time: 0.748394
System Time: 0.627373
"""