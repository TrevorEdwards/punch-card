import subprocess


def main():
    dates = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    times = []
    for i in range(0,24):
        times.append(' ' + str(i) + ':')
    satisfied = []
    for i in range(7):
        satisfied.append([])
    for i in range(7):
        for j in range(24):
            satisfied[i].append(False)
    log_process = subprocess.Popen(['git','log'], stdout=subprocess.PIPE)
    lines = []
    currentStr = ''

    # Gather dates into array of strings
    while True:
        outStr = log_process.stdout.readline()
        if outStr == '' and log_process.poll != None:
            break
        if 'Date' in outStr:
            lines.append(outStr)

    for i in range(7):
        date = dates[i]
        for j in range(24):
            time = times[j]
            for entry in lines:
                if date in entry and time in entry:
                    satisfied[i][j] = True

    for i in range(7):
        date = dates[i]
        for j in range(24):
            time = times[j]
            if not satisfied[i][j]:
                print(date + ' ' + time)
    
def bs_commit(day, time):
    fake_echo = 'echo filler >> filler.txt'.split(' ')
    do_add = 'git add filler.txt'.split(' ')
    do_commit = 'git commit -m "timestamp filler" --date "' + day + ' Apr 1' + time + ':00:00 2017 -0400"'.split(' ')
    subprocess.Popen(fake_echo, stdout=subprocess.PIPE)
    subprocess.Popen(do_add, stdout=subprocess.PIPE)
    subprocess.Popen(do_commit, stdout=subprocess.PIPE)

main()

