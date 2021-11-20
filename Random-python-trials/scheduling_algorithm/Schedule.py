import sys
file = open(sys.argv[2])
output = open("output.txt","w")
algorithm = sys.argv[1]
tasks = [line.split() for line in file]
i = 0
while i < len(tasks):
    if not tasks[i]:
        del tasks[i]
    i += 1
for _ in range(len(tasks)):
    for i in range(3):
        tasks[_][i] = tasks[_][i][:-1]

tasks.sort(key = lambda x: x[1])
first_arrived = tasks[0]

#------------------------------------------------------------------------------------------------------------------------------

if algorithm == "fcfs":
    timer= int(tasks[0][1])
    turn_around= [0] * len(tasks)
    for i in range(len(tasks)):
        output.write("Will run Name: " + tasks[i][0] + "\n")
        output.write("Priority: "+ tasks[i][2] + "\n")
        output.write("Burst: "+ tasks[i][3] + "\n")
        output.write("Task "+tasks[i][0]+" finished" + "\n" + "\n")
        timer += int(tasks[i][3])
        turn_around[i] = timer - int(tasks[i][1])
    average_turnaround = sum(turn_around) / len(tasks)
    output.write("Average Turnaround Time: "+ str(average_turnaround) + "\n")
    waiting_time= [0] * len(tasks)
    for i in range(len(waiting_time)):
        waiting_time[i] = turn_around[i] - int(tasks[i][3])
    average_waiting = sum(waiting_time) / len(tasks)
    output.write("Average Waiting Time: "+ str(average_waiting) + "\n")

#------------------------------------------------------------------------------------------------------------------------------

if algorithm == "sjf":
    tasks.sort(key = lambda x: x[3])
    time_passed = 0
    for i in range(len(tasks)-1):
            if int(tasks[i][3]) == int(tasks[i+1][3]) and int(tasks[i][1]) > int(tasks[i+1][1]):
                temp = tasks[i]
                tasks[i] = tasks[i+1]
                tasks[i+1] = temp

    if tasks[0] != first_arrived:
        for i in range(len(tasks)):
            if (tasks[i] == first_arrived):
                del tasks[i]
                tasks.insert(0, first_arrived)

    timer = int(tasks[0][1])
    turn_around = [0] * len(tasks)
    for i in range(len(tasks)):
        output.write("Will run Name: " + tasks[i][0] + "\n")
        output.write("Priority: "+ tasks[i][2] + "\n")
        output.write("Burst: "+ tasks[i][3] + "\n")
        output.write("Task "+tasks[i][0]+" finished" + "\n" + "\n")
        timer += int(tasks[i][3])
        turn_around[i] = timer - int(tasks[i][1])
    average_turnaround = sum(turn_around) / len(tasks)
    output.write("Average Turnaround Time: " + str(average_turnaround) + "\n")
    waiting_time = [0] * len(tasks)
    for i in range(len(waiting_time)):
        waiting_time[i] = turn_around[i] - int(tasks[i][3])
    average_waiting = sum(waiting_time) / len(tasks)
    output.write("Average Waiting Time: " + str(average_waiting) + "\n")

#------------------------------------------------------------------------------------------------------------------------------

if algorithm == "pri":
    tasks.sort(key = lambda x: int(x[2]), reverse=True)
    for i in range(len(tasks)-1):
            if int(tasks[i][2]) == int(tasks[i+1][2]) and int(tasks[i][1]) > int(tasks[i+1][1]):
                temp = tasks[i]
                tasks[i] = tasks[i+1]
                tasks[i+1] = temp

    if tasks[0] != first_arrived:
        for i in range(len(tasks)):
            if (tasks[i] == first_arrived):
                del tasks[i]
                tasks.insert(0, first_arrived)

    timer = int(tasks[0][1])
    turn_around = [0] * len(tasks)
    for i in range(len(tasks)):
        output.write("Will run Name: " + tasks[i][0] + "\n")
        output.write("Priority: "+ tasks[i][2] + "\n")
        output.write("Burst: "+ tasks[i][3] + "\n")
        output.write("Task "+tasks[i][0]+" finished" + "\n" + "\n")
        timer += int(tasks[i][3])
        turn_around[i] = timer - int(tasks[i][1])
    average_turnaround = sum(turn_around) / len(tasks)
    output.write("Average Turnaround Time: " + str(average_turnaround) + "\n")
    waiting_time = [0] * len(tasks)
    for i in range(len(waiting_time)):
        waiting_time[i] = turn_around[i] - int(tasks[i][3])
    average_waiting = sum(waiting_time) / len(tasks)
    output.write("Average Waiting Time: " + str(average_waiting) + "\n")

#------------------------------------------------------------------------------------------------------------------------------

if algorithm == "rr":
    length = len(tasks)
    burst = []
    for _ in range(length):
        burst.append(tasks[_][3])
    flag = True
    i = 0
    j= 0
    timer = int(tasks[0][1])
    turn_around = [0] * len(tasks)
    while flag:
        tasks[i][-1] = int(tasks[i][-1])
        output.write("Will run Name: " + tasks[i][0] + "\n")
        output.write("Priority: " + tasks[i][2] + "\n")
        tasks[i][-1] -= 10
        timer += 10
        if tasks[i][-1] < 0:
            timer+= int(tasks[i][-1])
            tasks[i][-1] = 0
        output.write("Burst remaing: " + str(tasks[i][-1]) + "\n" + "\n")
        if tasks[i][-1] == 0:
            output.write("Task " + tasks[i][0] + " finished" + "\n" + "\n")
            turn_around[j] = timer - int(tasks[i][1])
            j += 1
            del tasks[i]
            i -=1
        i+=1
        if not tasks: flag= False
        if i >= len(tasks): i = 0
    average_turnaround = sum(turn_around) / length
    output.write("Average Turnaround Time: " + str(average_turnaround) + "\n")
    waiting_time = [0] * length
    for i in range(len(waiting_time)):
        waiting_time[i] = turn_around[i] - int(burst[i])
    average_waiting = sum(waiting_time) / length
    output.write("Average Waiting Time: " + str(average_waiting) + "\n")
#------------------------------------------------------------------------------------------------------------------------------

if algorithm == "pri-rr":
    length = len(tasks)
    burst = []
    for _ in range(length):
        burst.append(tasks[_][3])
    timer = int(tasks[0][1])
    turn_around = [0] * len(tasks)
    tasks.sort(key=lambda x: int(x[2]), reverse=True)
    flag = True
    i = 0
    z = 0
    if tasks[0] != first_arrived:
        for j in range(len(tasks)):
            if (tasks[j] == first_arrived):
                del tasks[j]
                tasks.insert(0, first_arrived)

    while flag:
        tasks[i][-1] = int(tasks[i][-1])
        if tasks[i] != tasks[-1]:
            if tasks[i][2] == tasks[i+1][2]:
                j = i
                while(tasks[j][-1] != 0 and tasks[j+1][-1] != 0):
                    tasks[j][-1] = int(tasks[j][-1])
                    output.write("Will run Name: " + tasks[j][0] + "\n")
                    output.write("Priority: " + tasks[j][2] + "\n")
                    tasks[j][-1] -= 10
                    timer += 10
                    if tasks[j][-1] < 0:
                        timer += int(tasks[i][-1])
                        tasks[j][-1] = 0
                    output.write("Burst remaing: " + str(tasks[j][-1]) + "\n" + "\n")
                    if tasks[j][-1] == 0:
                        output.write("Task " + tasks[j][0] + " finished" + "\n" + "\n")
                        turn_around[z] = timer - int(tasks[j][1])
                        z += 1
                    if j == i : j +=1
                    else: j-=1
                if tasks[j][-1] == 0: del tasks[j]
                else: del tasks[j+1]


        output.write("Will run Name: " + tasks[i][0] + "\n")
        output.write("Priority: " + tasks[i][2] + "\n")
        tasks[i][-1] -= 10
        timer += 10
        if tasks[i][-1] < 0:
            timer += int(tasks[i][-1])
            tasks[i][-1] = 0
        output.write("Burst remaing: " + str(tasks[i][-1]) + "\n" + "\n")
        if tasks[i][-1] == 0:
            turn_around[z] = timer - int(tasks[i][1])
            z += 1
            output.write("Task " + tasks[i][0] + " finished" + "\n" + "\n")
            del tasks[i]
        if not tasks: flag = False
        elif i == 0 and tasks[i][-1] != 0:
            tasks.sort(key=lambda x: int(x[2]), reverse=True)
        if i >= len(tasks): i = 0

    average_turnaround = sum(turn_around) / length
    output.write("Average Turnaround Time: " + str(average_turnaround) + "\n")
    waiting_time = [0] * length
    for i in range(len(waiting_time)):
        waiting_time[i] = turn_around[i] - int(burst[i])
    average_waiting = sum(waiting_time) / length
    output.write("Average Waiting Time: " + str(average_waiting) + "\n")


