def assign_jobs(jobs, workers):
    assigned_jobs = [[] for _ in range(len(workers))] 

    for job, time in sorted(jobs, key=lambda x: x[1], reverse=True):
        min_worker_index = min(range(len(workers)), key=lambda i: sum(workers[i])) 
        assigned_jobs[min_worker_index].append((job, time))
        workers[min_worker_index].append(time)

    return assigned_jobs

jobs = [('작업1', 4), ('작업2', 2), ('작업3', 5), ('작업4', 3)]
workers = [[], []] 

assigned_jobs = assign_jobs(jobs, workers)

for i, worker_jobs in enumerate(assigned_jobs):
    print(f"사람 {i+1}의 작업:")
    for job, time in worker_jobs:
        print(f" - {job} ({time} 시간)")
    print()