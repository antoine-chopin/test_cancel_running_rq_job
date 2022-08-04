The purpose of this repository is to test for what happens when we try to cancel an RQ job that is already running

Steps:
- Make a virtualenv then install rq and redis
- Run redis locally: docker run -p 6379:6379 redis
- Run the worker: rq worker defaultTASK RUNNING
- Run main.py
- See what happens!