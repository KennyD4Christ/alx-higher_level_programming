def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    return total_weighted_sum / total_weight


if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
