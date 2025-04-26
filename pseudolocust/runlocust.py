import pandas as pd
import os
import random
while(True):
    users=int(2**((random.random()*6+3))*10)
    print(users)
    rate=random.randint(4,16)
    print(rate)

    os.system("locust -f locustfile.py --web-port 8081 --headless -u "+str(users)+" --host=http://192.168.2.11:80  -r "+str(rate)+" --run-time 180  --csv lasttest")
    input=open("lasttest_stats_history.csv")
    tasksr=open("tasks.csv")
    tasks=""
    for line in tasksr:
        tasks=line[1:-1]
        print("TASKS ARE")
        print(tasks)
    output=open("bigsums.csv", "a")
    i=0
    for line in input:
        i=i+1
        if(i>3 and i%2==1):
            towrite=line[:-1]+","+str(rate)+","+tasks+'\n'
            print(towrite)
            output.write(towrite)
    input.close()
    output.close()
    tasksr.close()
