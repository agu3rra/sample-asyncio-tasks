# A sample asyncio usage
import asyncio
import time

async def print_after(what, delay):
    """Prints what after delay in seconds
    """
    await asyncio.sleep(delay)
    print(what)
    return "Done"

if __name__ == '__main__':
    print(f"Started: {time.strftime('%X')}")
    loop = asyncio.get_event_loop()
    tasks_functions = [
        print_after("Hello", 4),
        print_after("it's me", 5),
        print_after("Executing...", 10),
    ]

    tasks = []

    for task in tasks_functions:
        tasks.append(
            loop.create_task(task)
        )

    # Trigger tasks simultaneously:
    print("Trigerring tasks...")
    try:
        for task in tasks:
            loop.run_until_complete(task)
    finally:
        loop.close()

    print("Tasks execution completed!")
    print("Results retrieved:")
    for task in tasks:
        print(task.result())
    print(f"Finished: {time.strftime('%X')}")