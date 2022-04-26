def get_control_sum(value, weight_cf):
    return sum((int(val) * weight_cf[i] for i, val in enumerate(value)))


def get_remainder(control_sum: int) -> int:
    return control_sum % 11


def validator_ten_digit(inn: str, rem_div) -> str:
    if rem_div == int(inn[-1]):
        return f'The input inn: "{inn}" is valid'
    return f'The input inn: "{inn}" is not valid'


def validator_twelve_digit(inn: str, rem_div1: int, rem_div2: int) -> str:
    if rem_div1 == int(inn[-2]) and rem_div2 == int(inn[-1]):
        return f'The input inn: "{inn}" is valid'
    return f'The input inn: "{inn}" is not valid'


async def main_valid_logic(inn: str):
    weight_cf = {
        "n10": (2, 4, 10, 3, 5, 9, 4, 6, 8, 0),
        "n11": (7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0, 0),
        "n12": (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0),
    }
    if not inn:
        return f'The input inn is not valid: "{inn}" is Empty'
    if inn.isdigit():
        if len(inn) == 10:
            control_sum = get_control_sum(inn, weight_cf["n10"])
            return validator_ten_digit(inn, get_remainder(control_sum))
        elif len(inn) == 12:
            control_sum1 = get_control_sum(inn, weight_cf["n11"])
            control_sum2 = get_control_sum(inn, weight_cf["n12"])
            return validator_twelve_digit(inn, get_remainder(control_sum1), get_remainder(control_sum2))
        return f'The input inn is not valid: "{inn}" must be 10 or 12 digits'
    return f'The input inn is not valid: "{inn}" must be digit'
