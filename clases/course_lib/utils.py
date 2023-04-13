
def format_datapoints(trajectory:list, temps: list, format_as_dict: bool=True):

    formatted_datapoints = []

    for pos, temp in zip(trajectory, temps):
        x, y = pos

        if format_as_dict:
            dp = {
                'x': x,
                'y': y,
                'temp': temp,
            }

        formatted_datapoints.append(dp)

    return formatted_datapoints


