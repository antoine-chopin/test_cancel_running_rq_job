from time import sleep

def run_task():
    for _ in range(4):
        print("TASK RUNNING")
        sleep(5)
    print("TASK FINISHED")