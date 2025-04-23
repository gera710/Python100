
import threading
import time
import random
from typing import List, Dict, Any

# Shared list to store results from threads
# Needs protection because multiple threads will write to it
results_list: List[Dict[str, Any]] = []
# A lock to ensure only one thread modifies results_list at a time
results_lock = threading.Lock()

def simulate_fetch_data(url: str, task_id: int):
    """
    Simulates fetching data from a URL (takes variable time).
    Appends the result dictionary to the shared results_list safely.

    Args:
        url (str): The "URL" to fetch data from.
        task_id (int): An identifier for the task/thread.
    """
    print(f"[Thread-{task_id}] Starting fetch for: {url}")
    try:
        # Simulate network latency/processing time
        sleep_duration = random.uniform(0.5, 2.5) # Sleep for 0.5 to 2.5 seconds
        time.sleep(sleep_duration)

        # Simulate successful data retrieval
        data = {"url": url, "content": f"Data for {url}", "status": 200, "duration_seconds": round(sleep_duration, 2)}
        print(f"[Thread-{task_id}] Finished fetch for: {url} in {sleep_duration:.2f}s")

    except Exception as e:
        # Simulate an error during fetch
        print(f"[Thread-{task_id}] Error fetching {url}: {e}")
        data = {"url": url, "content": None, "status": 500, "error": str(e)}

    # --- Critical Section: Modifying shared data ---
    # Acquire the lock before accessing the shared results_list
    with results_lock:
        results_list.append(data)
    # The lock is automatically released when exiting the 'with' block
    # --- End Critical Section ---

# --- Main Thread Logic ---
if __name__ == "__main__":
    urls_to_fetch = [
        "http://example.com/api/users",
        "http://example.com/api/products",
        "http://example.com/api/orders",
        "http://example.com/api/settings",
        "http://invalid-url-example", # Simulate a potential error case
    ]

    threads: List[threading.Thread] = []
    start_time = time.time()

    print("Main: Creating and starting threads...")
    # Create and start a thread for each URL
    for i, url in enumerate(urls_to_fetch):
        # Create a Thread object:
        # target=simulate_fetch_data: the function the thread will execute
        # args=(url, i): tuple of arguments to pass to the target function
        thread = threading.Thread(target=simulate_fetch_data, args=(url, i))
        threads.append(thread)
        thread.start() # Start the thread's execution

    print(f"Main: All {len(threads)} threads started. Waiting for completion...")

    # Wait for all threads to finish
    # The main thread will block here until each thread completes its execution
    for i, thread in enumerate(threads):
        thread.join()
        print(f"Main: Thread-{i} has joined.")

    end_time = time.time()
    print("\nMain: All threads have completed.")
    print(f"Total execution time: {end_time - start_time:.2f} seconds.")

    print("\nCollected Results:")
    # Safely access results_list now that all threads are done (lock isn't strictly needed here,
    # but it's good practice if other threads *could* still be accessing it)
    # with results_lock: # Optional here as threads are joined
    for result in results_list:
            print(f"  - URL: {result.get('url')}, Status: {result.get('status')}, Duration: {result.get('duration_seconds', 'N/A')}s, Error: {result.get('error')}")

"""
Explanation:

1. Imports: threading for thread management, time for sleep, random for variable delays.

2. Shared Resources:
    - results_list: A standard Python list where each thread will put its result (a dictionary).
    - results_lock: A threading.Lock object. This is crucial. Before any thread modifies 
    - results_list,  it must acquire this lock. Only one thread can hold the lock at a time, 
    preventing race conditions 
    (where multiple threads try to modify the list simultaneously, potentially corrupting it).

3. simulate_fetch_data(url, task_id) Function:
    - This is the function each thread will run.
    - It prints start/finish messages, making it easy to see concurrent execution.
    - time.sleep() simulates the I/O wait time (like waiting for a network response).
    - It prepares a data dictionary containing the result.
    - Critical Section: The with results_lock: block ensures that 
    the results_list.append(data) operation is atomic 
    (happens entirely without interruption from other threads trying to do the same). 
    The lock is acquired at the start of the with block and released automatically at the end, 
    even if errors occur within the block.

4. Main Execution Block (if __name__ == "__main__":)
    - urls_to_fetch: The list of tasks to perform.
    - threads: A list to keep track of the Thread objects we create.
    Thread Creation Loop:
        - For each URL, a threading.Thread object is created.
        - target=simulate_fetch_data specifies the function the thread should execute.
        - args=(url, i) passes the specific URL and a unique ID to the function for that thread. Note: args must be a tuple, hence the comma (url, i).
        - thread.start(): Starts the thread's activity. The simulate_fetch_data function begins executing in the new thread. The main loop continues immediately to the next iteration without waiting.
    Thread Joining Loop:
        - thread.join(): This is the core management step. 
        The main thread stops and waits at this line until the specific thread it's calling join() 
        on has finished executing.
        - By looping through all threads and calling join() on each, 
        we ensure the main thread only proceeds past this loop after 
        all worker threads have completed their tasks.

Result Processing: 
    After all threads have joined, it's safe to process the results_list. 
    The total time is printed, which should be significantly less than the sum of all 
    individual sleep times if run sequentially.

This example demonstrates the fundamental pattern of creating, starting, synchronizing 
(waiting for completion with join), and safely collecting results from multiple threads.
"""