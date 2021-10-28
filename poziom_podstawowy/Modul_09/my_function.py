def wait_some_time(to_wait: int) -> None:
    from time import sleep
    print(f"We will wait {to_wait} seconds...")
    sleep(to_wait)
    print("OK, let's do rest...")
