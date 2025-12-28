import time

def fetch_data(id: int, delay: int):
    """Simulate fetching data from an API"""
    print(f"Starting fetch {id}...")
    time.sleep(delay)
    print(f"Completed fetch {id}")
    return f"Data from source {id}"


def main():
    """Main function to coordinate tasks"""
    print("Starting synchronous operations...")
    print("=" * 50)
    
    start_time = time.time()
    
    # Execute tasks sequentially (one after another)
    results = []
    results.append(fetch_data(1, 2))
    results.append(fetch_data(2, 1))
    results.append(fetch_data(3, 3))
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    print("\n" + "=" * 50)
    print(f"Results: {results}")
    print(f"Total time: {elapsed:.2f} seconds")
    print("\nNote: Tasks ran sequentially (2+1+3 = ~6 seconds)")


if __name__ == "__main__":
    main()