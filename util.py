from copy import copy
from fractions import Fraction
import logging
from optparse import Option, OptionValueError

def class_logger(original_class):
    """Add _logger to a class"""
    original_class._logger = logging.getLogger(
        original_class.__module__ + '.' + original_class.__name__)
    return original_class

def check_fraction(option, opt, value):
    try:
        return Fraction(value)
    except ValueError:
        raise OptionValueError(
            "option %s: invalid fraction value: %s" % (opt, repr(value)))

class MyOption(Option):
    """Adds support for the "fraction" type"""
    TYPES = Option.TYPES + ("fraction", )
    TYPE_CHECKER = copy(Option.TYPE_CHECKER)
    TYPE_CHECKER["fraction"] = check_fraction
