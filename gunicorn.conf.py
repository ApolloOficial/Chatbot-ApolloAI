"""Remove gauges de workers encerrados, preservando contadores acumulados."""
from prometheus_client import multiprocess


def child_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)
