import logging
import sys


def logger(
        name,
        level=logging.INFO,
        hdlr_level=logging.INFO):

    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter('%(name)s %(asctime)s %(message)s'))
    out_hdlr.setLevel(hdlr_level)
    logger = logging.getLogger(name)
    logger.addHandler(out_hdlr)
    logger.setLevel(level)
    return logger
