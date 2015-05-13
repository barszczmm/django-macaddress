from netaddr import EUI as OrgEUI
from netaddr.strategy import int_to_words as _int_to_words
from netaddr.strategy.eui64 import word_fmt, word_sep, word_size, num_words


def int_to_words(int_val, dialect=None):
    if dialect is not None and dialect.word_size and dialect.num_words:
        return _int_to_words(int_val, dialect.word_size, dialect.num_words)
    return _int_to_words(int_val, word_size, num_words)


def int_to_str(int_val, dialect=None):
    """
    :param int_val: An unsigned integer.

    :param dialect: (optional) a Python class defining formatting options

    :return: An IEEE EUI-64 identifier that is equivalent to unsigned integer.
    """
    if dialect is not None:
        use_word_fmt = dialect.word_fmt
        use_word_sep = dialect.word_sep
    else:
        use_word_fmt = word_fmt
        use_word_sep = word_sep

    words = int_to_words(int_val, dialect)
    tokens = [use_word_fmt % i for i in words]
    addr = use_word_sep.join(tokens)
    return addr


class EUI(OrgEUI):

    def __str__(self):
        """:return: EUI in representational format"""
        return int_to_str(self._value, self._dialect)

