import os
import logging
import itertools


def clear_directories(directories, files, logger):
    ok, error = [], []
    for left, right in itertools.product(directories, files):
        f = os.path.join(left, right)
        if not os.path.isfile(f):
            logger.error("file {} clear nok".format(f))
            error.append(f)
            continue
        try:
            fd = open(f, 'w')
            fd.close()
        except Exception as e:
            logger.error("file {} clear nok".format(f))
            error.append(f)
            continue
        logger.info("file {} clear ok".format(f))
        ok.append(f)
    return ok, error

