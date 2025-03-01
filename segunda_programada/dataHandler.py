import os, pickle

FIXED_RECORD_SIZE = 1024
INFO_DAT_FILENAME = "info.dat"

def initialize_info_dat(slots=750):
    if not os.path.exists(INFO_DAT_FILENAME):
        with open(INFO_DAT_FILENAME, "wb") as f:
            for _ in range(slots):
                f.write(b'\x00' * FIXED_RECORD_SIZE)

def write_record(record, position):
    with open(INFO_DAT_FILENAME, "r+b") as f:
        f.seek(position * FIXED_RECORD_SIZE)
        data = pickle.dumps(record)
        if len(data) > FIXED_RECORD_SIZE:
            raise ValueError("Excede tamaño.")
        f.write(b'\x00' * FIXED_RECORD_SIZE)
        f.seek(position * FIXED_RECORD_SIZE)
        f.write(data)

def read_record(position):
    with open(INFO_DAT_FILENAME, "rb") as f:
        f.seek(position * FIXED_RECORD_SIZE)
        data = f.read(FIXED_RECORD_SIZE)
        if all(b == 0 for b in data):
            return None
        try:
            return pickle.loads(data)
        except:
            return None

def write_collision_record(record, position):
    fname = f"{position}-col.dat"
    with open(fname, "ab") as f:
        pickle.dump(record, f)

def read_collision_records(position):
    fname = f"{position}-col.dat"
    if not os.path.exists(fname):
        return []
    records = []
    with open(fname, "rb") as f:
        while True:
            try:
                records.append(pickle.load(f))
            except EOFError:
                break
    return records
