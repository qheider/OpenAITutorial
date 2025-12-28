import asyncio
import time

async def fetch_data(id: int, delay: int):
    """Simulate fetching data from an API"""
    print(f"Starting fetch {id}...")
    await asyncio.sleep(delay)
    print(f"Completed fetch {id}")
    return f"Data from source {id}"


async def main():
    """Main async function to coordinate tasks"""
    print("Starting async operations...")
    
    # Create multiple tasks
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3)
    )
    
    print(f"\nResults: {results}")


if __name__ == "__main__":
    # Using asyncio.Runner (Python 3.11+)
    with asyncio.Runner() as runner:
        runner.run(main())