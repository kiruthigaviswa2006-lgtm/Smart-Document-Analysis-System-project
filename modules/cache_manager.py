import os
import hashlib

CACHE_FOLDER = "cache"

os.makedirs(CACHE_FOLDER, exist_ok=True)


def get_cache_path(file_path):

    file_hash = hashlib.md5(file_path.encode()).hexdigest()

    return os.path.join(CACHE_FOLDER, file_hash + ".txt")


def save_cache(file_path, text):

    cache_file = get_cache_path(file_path)

    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(text)


def load_cache(file_path):

    cache_file = get_cache_path(file_path)

    if os.path.exists(cache_file):

        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()

    return None