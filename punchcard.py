import subprocess, time, git


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
            time_clock = times[j]
            for entry in lines:
                if date in entry and time_clock in entry:
                    satisfied[i][j] = True

    for i in range(7):
        date = dates[i]
        for j in range(24):
            time_clock = times[j]
            if not satisfied[i][j]:
                print(date + ' ' + time_clock)
                bs_commit(date,time_clock)
    
def bs_commit(day, time_clock):
    sleep_time = 0.1
    fake_echo = ['bash','filler.sh']
    do_add = 'git add filler.txt'.split(' ')
    do_commit = ['git', 'commit', '-m' ,'timestamp filler' ,'--date', str(day) + ' Apr 1' + str(time_clock) + '00:00 2017 -0400' ]
    print(do_commit)
    print("doing filler")
    subprocess.call(fake_echo, stdout=subprocess.PIPE)
    time.sleep(sleep_time)
    print("doing add")
    subprocess.Popen(do_add, stdout=subprocess.PIPE)
    time.sleep(sleep_time)
    print("doing commit")
    subprocess.Popen(do_commit, stdout=subprocess.PIPE)
    time.sleep(sleep_time)

main()

