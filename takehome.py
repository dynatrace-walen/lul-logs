import os
import shutil
import time
import logging

def print_inode(filepath):
    try:
        inode = os.stat(filepath).st_ino
        print(f"{filepath} inode: {inode}")
    except FileNotFoundError:
        print(f"{filepath} not found.")



def log_rotation(log_dir):
    os.makedirs(log_dir, exist_ok=True)

    # Create paths for logs.
    current_log = os.path.join(log_dir, "example-current.log")
    # log once per second
    
    rotated_log = os.path.join(log_dir, "example.log.20250714")

    logger = logging.getLogger(name="str")

    logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
                            filemode='a',
                            datefmt = '%m/%d/%Y %H:%M:%S',
                            filename=f'{"example-current.log"}'
                        )
    logger.setLevel(level="INFO")

    for x in range(20):
        logger.info(f"test log number {x+1}")
        time.sleep(1)

    logging.shutdown()

    print("\nAfter creating current log:")
    print_inode(current_log)

    time.sleep(1)

    shutil.copy(current_log, rotated_log)
    # Pointer does NOT propogate from original to copy (inode changes), so OA does not maintain tracking of the rotated file.
    # Copy current log to rotated log (example.log.20250714)

    print("\nAfter copying to rotated log:")
    print_inode(current_log)
    print_inode(rotated_log)

    # Rename current log to example-current_renamed
    renamed_log = os.path.join(log_dir, "example-current_renamed.log")
    os.rename(current_log, renamed_log)

    print("\nAfter renaming current log:")
    print_inode(renamed_log)

def main():
    log_rotation("/var/log")

if __name__ == "__main__":
    main()



# use Logger on 
