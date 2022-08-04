import rq
from rq import Worker, Connection, Queue
from rq.job import Job
from redis import Redis
from threading import Thread
from time import sleep
from task import run_task

def run():
    task_id = push_task().id
    sleep(5)
    cancel_task(task_id)

def run_worker():
    with Connection(Redis(
            host='localhost',
            port=6379
    )) as connection:
        worker = Worker("default", connection=connection)
        worker.work()

def push_task():
    with Connection(Redis(
            host='localhost',
            port=6379
    )) as connection:
        queue = Queue(connection=connection)
        return queue.enqueue(f=run_task)


def cancel_task(job_id):
    with Connection(Redis(
            host='localhost',
            port=6379
    )) as connection:
        job = Job.fetch(job_id)
        print("Job status before cancel:", job.get_status())
        rq.cancel_job(job_id=job_id, connection=connection)
        print("Job status after cancel:", job.get_status())

if __name__ == "__main__":
    run()