"""
Naı̈ve Estimator (CZ4041 assignment)

- author: Ngo Jun Hao Jason (matriculation number: U1721978B)
- Python version: 3.7.6
"""


def window_function(u):
    """
    params:
    - u: an iterable

    return:
    - 1 if u_i < 1/2 for all i ∈ {1,2, ... , d}, and 0 otherwise
    """
    for u_i in u:
        if abs(u_i) >= 0.5:
            return 0

    return 1

def read_data(file_path='data.txt', verbose=False):
    """
    params:
    - file_path: path to file that contains data (default: 'data.txt')
    - verbose: whether to print information (default: False)

    return: a tuple that consists of the following:
    - n: number of data instances
    - m: number of features of each data instance
    - data: a list of tuple, where each tuple is a data instance
    """
    n, m, data = 0, 0, []

    with open(file_path, 'r') as input_file:
        line = input_file.readline().strip('\n')
        n, m = map(int, line.split(','))

        if verbose:
            print(f'number of data instances: {n}')
            print(f'number of features of each data instance: {m}')
        
        for _ in range(n):
            line = input_file.readline().strip('\n')
            data_instance = tuple(map(float, line.split(' ')))
            data.append(data_instance)

        if verbose:
            print('data:', data)

    return n, m, data


def estimate_probability(test_instance, data, h, n, V):
    """
    Naı̈ve Estimator
    
    params:
    - test_instance: a tuple
    - data: a list of tuple, where each tuple is a data instance
    - h: length of each edge of a hypercube (multi-variate version of delta)
    - n: number of data instances
    - V: volume of the hypercube

    return: relative likelihood that a RV from the data equals the test instance
    """
    sum = 0

    for data_point in data:
        x_minus_x_i = tuple(map(lambda x, x_i: x - x_i, test_instance, data_point))
        x_minus_x_i_over_h = tuple(map(lambda x: x / h, x_minus_x_i))

        sum += window_function(x_minus_x_i_over_h)

    return (sum / n) / V


def estimate_density(data, h, n, V):
    """
    params:
    - data: a list of tuple, where each tuple is a data instance
    - h: length of each edge of a hypercube (multi-variate version of delta)
    - n: number of data instances
    - V: volume of the hypercube

    return: a list of probability for each data instance in data
    """
    probabilities = []

    for data_point in data:
        # use each data point as a test instance in this assignment
        p_hat = estimate_probability(data_point, data, h, n, V)
        probabilities.append(p_hat)

    return probabilities


def write_output(probabilities, file_path='output.txt'):
    """
    params:
    - probabilities: a list of probability for each data instance in data
    - file_path: path to file for writing output to (default: 'output.txt')
    """
    with open(file_path, 'w') as output_file:
        for probability in probabilities:
            output_file.write(str(probability) + '\n')


if __name__ == '__main__':
    import os


    # change directory to this script's directory
    # since data.txt should be in the same directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    h = 2  # length of each edge of a hypercube

    n, m, data = read_data()

    V = h**m  # volume of the hypercube

    probabilities = estimate_density(data, h, n, V)

    write_output(probabilities)
