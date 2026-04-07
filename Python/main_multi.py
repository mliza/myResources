import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

def do_work(task_id: int, duration: float = 0.1) -> str:
    time.sleep(duration)
    return f"Task {task_id} completed"

def run_threading(tasks: int=5, max_workers: int = 5) -> list[str]:
    results: list[str] = [ ]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_work, i, 0.1) for i in range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    return results

def do_cpu_work(task_id: int, iterations: int = 100000) -> str:
    result = 0
    for i in range(iterations):
        result += i * i

    return(f"Task {task_id} completed (result: {result})")

def run_multiprocssing(tasks: int = 5, max_workers: int = 5) -> list[str]:
    results: list[str] = [ ]

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_cpu_work, i, 1000000) for i in
                    range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    return results


def run_sync(tasks: int = 5) -> list[str]:
    results: list[str] = [ ]

    for i in range(tasks):
        result = do_work(i, duration=0.1)
        results.append(result)

    return results


if __name__== "__main__":
    start_time = time.perf_counter()
    #results = run_sync(tasks=5)
    #results = run_threading(tasks=5)
    results = run_multiprocssing(tasks=5, max_workers=5)
    elapsed_time = time.perf_counter() - start_time

    for result in results:
        print(f"    {result}")

    print(f"\nTotal time: {elapsed_time:.2f} [s]")
    #print("Note: Tasks ran one after another (synchronous execution)")
    #print("Note: Tasks ran concurrently using threads (I/O-bound tasks)")
    print("Note: Tasks ran in parallel using separate process (CPU-bound tasks)")
