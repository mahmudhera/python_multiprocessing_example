import multiprocessing
import time
import requests

def get_http_response(url):
    """Function to get the HTTP response for a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response
    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))
        return None

def square(n):
    """Function to calculate the square of a number."""
    url = 'https://www.genome.jp/kegg/pathway.html'
    get_http_response(url)
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
