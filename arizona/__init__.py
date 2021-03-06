# -*- coding: utf-8 -*-

__version__ = 'v0.0.1'

DEFAULT_PARAMETERS = {
    "abbreviation": {
        "replace_thresold": 0.5,
        "num_samples": 7,
        "lowercase": True,
        "config_file": "configs/abbreviations.json"
    },
    "keyboard": {
        "replace_thresold": 0.5,
        "num_samples": 7,
        "lowercase": True,
        "aug_char_percent": 0.2,
        "aug_word_percent": 0.1,
        "unikey_percent": 0.6,
        "config_file": "configs/unikey.json"
    },
    "remove_accent": {
        "replace_thresold": 0.4,
        "num_samples": 7,
        "lowercase": True
    }
}