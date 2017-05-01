import subprocess, time, git


def main():
    dates = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    times = []
    for i in range(0,24):
        appendStr = '' + str(i)
        if i < 10:
            appendStr = '0' + str(i)
        times.append(appendStr + ':')
    satisfied = []
    for i in range(7):
        satisfied.append([])
    for i in range(7):
        for j in range(24):
            satisfied[i].append(False)
    log_process = subprocess.Popen(['git','log','--sparse','--full-history'], stdout=subprocess.PIPE)
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
                if (' ' + date) in entry and (' ' + time_clock) in entry:
                    satisfied[i][j] = True

    for i in range(7):
        date = dates[i]
        for j in range(24):
            time_clock = times[j]
            if not satisfied[i][j]:
                print(date + ' ' + time_clock)
                bs_commit(date,time_clock,i)
    
def bs_commit(day, time_clock, map_index):
    day_map = [3,4,5,6,7,8,9]
    sleep_time = 0.2
    fake_echo = ['bash','filler.sh']
    do_add = 'git add filler.txt'.split(' ')
    do_commit = ['git', 'commit', '-m' ,'timestamp filler' ,'--date', str(day) + ' Apr '+ str(day_map[map_index])  + str(time_clock) + '00:00 2017 -0400' ]
    print("doing filler")
    p=subprocess.Popen(fake_echo, stdout=subprocess.PIPE)
    p.wait()
    print("doing add")
    p=subprocess.Popen(do_add, stdout=subprocess.PIPE)
    p.wait()
    print("doing commit")
    p=subprocess.Popen(do_commit, stdout=subprocess.PIPE)
    p.wait()

main()

