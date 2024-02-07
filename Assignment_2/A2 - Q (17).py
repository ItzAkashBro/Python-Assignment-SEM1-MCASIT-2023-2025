# In a company, worker efficiency is determined on the basis of the time required for a worker
# to complete a particular job. If the time taken by the worker is between 2 – 3 hours, then the
# worker is said to be highly efficient. If the time required by the worker is between 3 – 4
# hours, then the worker is ordered to improve speed. If the time taken is between 4 – 5 hours,
# the worker is given training to improve his speed, and if the time taken by the worker is
# more than 5 hours, then the worker has to leave the company. If the time taken by the
# worker is input through the keyboard, find the efficiency of the worker.

WorkTime=int(input("Enter The Time Taken By the Worker to Complete the task(minute): "))
if(WorkTime>=120 and WorkTime<180):
    print("Worker is Highly Efficient")
elif(WorkTime>=180 and WorkTime<240):
    print("worker is ordered to improve speed.")
elif(WorkTime>=240 and WorkTime<300):
    print("he worker is given training to improve his speed")
elif(WorkTime>=300):
    print("worker has to leave the company")
else:
    print("wrong value entered")
    
