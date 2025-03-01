# dataHandler.py

import os
import pickle

FIXED_RECORD_SIZE = 1024
INFO_DAT_FILENAME = "info.dat"
COLLISIONS_DIR = "collisions"  # Subcarpeta para colisiones

def initialize_info_dat(slots=750):
    if not os.path.exists(INFO_DAT_FILENAME):
        with open(INFO_DAT_FILENAME, "wb") as f:
            for _ in range(slots):
                f.write(b'\x00' * FIXED_RECORD_SIZE)

def write_record(record, position):
    with open(INFO_DAT_FILENAME, "r+b") as f:
        offset = position * FIXED_RECORD_SIZE
        f.seek(offset)
        data = pickle.dumps(record)
        if len(data) > FIXED_RECORD_SIZE:
            raise ValueError("El objeto excede el tamaño fijo asignado.")
        f.write(b'\x00' * FIXED_RECORD_SIZE)
        f.seek(offset)
        f.write(data)

def read_record(position):
    with open(INFO_DAT_FILENAME, "rb") as f:
        offset = position * FIXED_RECORD_SIZE
        f.seek(offset)
        data = f.read(FIXED_RECORD_SIZE)
        if all(b == 0 for b in data):
            return None
        try:
            return pickle.loads(data)
        except:
            return None

def write_collision_record(record, position):
    if not os.path.exists(COLLISIONS_DIR):
        os.makedirs(COLLISIONS_DIR)
    collision_filename = f"{position}-col.dat"
    collision_path = os.path.join(COLLISIONS_DIR, collision_filename)
    with open(collision_path, "ab") as f:
        pickle.dump(record, f)

def read_collision_records(position):
    if not os.path.exists(COLLISIONS_DIR):
        return []
    collision_filename = f"{position}-col.dat"
    collision_path = os.path.join(COLLISIONS_DIR, collision_filename)
    if not os.path.exists(collision_path):
        return []
    records = []
    with open(collision_path, "rb") as f:
        while True:
            try:
                records.append(pickle.load(f))
            except EOFError:
                break
    return records


