import logging

def class_logger(original_class):
    """Add _logger to a class"""
    original_class._logger = logging.getLogger(
        original_class.__module__ + '.' + original_class.__name__)
    return original_class
