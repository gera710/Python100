
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

