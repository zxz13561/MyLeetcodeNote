from datetime import datetime as dt


def climb_stairs(cost):
    # Loop through every cost after the first two steps
    for i in range(2, len(cost)):
        # Update the cheapest cost to step here
        cost[i] += min(cost[i - 2], cost[i - 1])

    # Cheapest cost of the last two steps is the answer
    return min(cost[len(cost) - 2], cost[len(cost) - 1])


if __name__ == '__main__':
    input_cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(climb_stairs(input_cost))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
