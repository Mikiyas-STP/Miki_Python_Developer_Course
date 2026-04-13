import logging
# Set up the logger
logging.basicConfig(level=logging.INFO)

def get_db_record(record_id: int):
    if record_id == 0:  # No parentheses needed
        raise ValueError("ID 0 is reserved")
    elif record_id == 99:
        raise ConnectionError("Database Offline")
    else:
        return "Record Data"

def run_search(record_id: int):
    try:
        # We must pass the record_id here!
        result = get_db_record(record_id)
    except ValueError as e:
        # 'e' contains the message "ID 0 is reserved"
        logging.warning(f"Invalid request: {e}")
    except ConnectionError as e:
        # 'e' contains the message "Database Offline"
        logging.error(f"System Error: {e}")
    else:
        logging.info(f"Search Successful: {result}")
    finally:
        print("Database connection closed.")
# Test it
run_search(0)   # Logs a WARNING
run_search(99)  # Logs an ERROR
run_search(1)   # Logs INFO