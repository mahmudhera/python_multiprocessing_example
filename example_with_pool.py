import multiprocessing
import time

def square(n):
    """Function to calculate the square of a number."""
    time.sleep(1)
    return n ** 2

if __name__ == '__main__':
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]*3

    start_time = time.time()
    results = [ square(i) for i in numbers ]
    end_time = time.time()
    print( f'Elapsed time: {end_time - start_time} seconds. Result: {results}' )

    start_time = time.time()
    # Create a multiprocessing pool with 4 processes
    pool = multiprocessing.Pool(processes=4)
    # Apply the square function to each number using the pool
    results = pool.map(square, numbers)
    # Close the pool and wait for the tasks to complete
    pool.close()
    pool.join()
    end_time = time.time()
    print( f'Elapsed time: {end_time - start_time} seconds. Result: {results}' )
