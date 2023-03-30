import multiprocessing

# this function looks up the query in the shared list
# if found, it returns True
# else, it returns False
def process_data(shared_list, query, return_list, process_id):
    for item in shared_list:
        if item == query:
            return_list[process_id] = True
            return
    return_list[process_id] = False
    return


if __name__ == '__main__':
    num_processes = 10
    manager = multiprocessing.Manager()
    shared_list = manager.list()
    shared_list = shared_list + [1,2,3,4,5,6,7,8,9]
    return_list = manager.list()
    for i in range(num_processes):
        return_list.append(-2)

    process1 = multiprocessing.Process(target=process_data, args=[shared_list, 3, return_list, 0])
    process3 = multiprocessing.Process(target=process_data, args=[shared_list, 12, return_list, 4])

    print(return_list)

    process1.start()
    process3.start()
    process1.join()
    process3.join()

    print(return_list)
