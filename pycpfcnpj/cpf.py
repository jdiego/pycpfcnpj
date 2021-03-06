from . import calculation as calc
from . import compatible as compat


def validate(cpf_number):
    """This function validates a CPF number.

    This function uses calculation package to calculate both digits
    and then validates the number.

    :param cpf_number: a CPF number to be validated.  Only numbers.
    :type cpf_number: string
    :return: Bool -- True for a valid number, False otherwise.

    """

    _cpf = compat.clear_punctuation(cpf_number)

    if (len(_cpf) != 11 or
       len(set(_cpf)) == 1):
        return False

    first_cpf_weighs = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    second_cpf_weighs = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    first_part = _cpf[:9]
    first_digit = _cpf[9]
    second_digit = _cpf[10]

    if (first_digit == calc.first_check_digit(first_part,
                                              first_cpf_weighs) and
       second_digit == calc.second_check_digit(_cpf[:10],
                                               second_cpf_weighs)):
        return True

    return False
