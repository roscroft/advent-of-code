from functools import reduce
with open('input.txt', 'r+') as datafile:
    data = datafile.readlines()
print(reduce((lambda x, y: int(x) + int(y)), data))

def run_through(running_total):
    for item in data:
        running_total += int(item)
        if running_total in already_seen:
            return (running_total, True)
        else:
            already_seen.add(running_total)
    return (running_total, False)

exit_cond = False
already_seen = set()
running_total = 0
while not exit_cond:
    (running_total, exit_cond) = run_through(running_total)

print(running_total)
