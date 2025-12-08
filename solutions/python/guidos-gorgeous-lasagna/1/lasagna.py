EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).

    This function takes the amount of time the lasagna has already spent baking
    and returns how many minutes of baking time are still needed based on the
    EXPECTED_BAKE_TIME constant.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - preparation time (in minutes).

    This function takes the number of layers in the lasagna and returns how many
    minutes of preparation time are required based on the PREPARATION_TIME constant.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed baking time.
    :return: int - total time elapsed (in minutes).

    This function adds the preparation time and the time already spent baking
    to calculate how many total minutes have elapsed cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
