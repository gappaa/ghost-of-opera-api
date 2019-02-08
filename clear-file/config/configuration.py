import configparser


def _get_option(config, section, option):
    return [_ for _ in config[section][option].split(';') if _ != ''] if section in config and option in config[section] else []


def get_clean(filename, logger):
    config = configparser.ConfigParser()
    try:
        config.read(filename)
    except AttributeError as e:
        logger.info(e)
        return [], []

    return _get_option(config, 'clean', 'directories'), _get_option(config, 'clean', 'files')

