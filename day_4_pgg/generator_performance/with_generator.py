import resource

def read_file(file_name):
    with open(file_name, 'r') as handle:
        while True:
            line = handle.readline()
            if not line:
                break
            yield line

# https://alx.piotr.gg/python/sales-records.csv
file_name = '../../data/sales-records.csv'
data = read_file(file_name)

for line in data:
    print(line)

print('Memory:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('User Time:', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
print('System Time:', resource.getrusage(resource.RUSAGE_SELF).ru_stime)

"""
Memory: 11206656 = 10MB
User Time: 0.799601
System Time: 0.600376
"""