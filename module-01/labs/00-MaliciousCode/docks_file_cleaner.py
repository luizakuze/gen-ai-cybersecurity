import os
import time
import logging

def monitor_directory(directory):
    """
    Continuously monitor a directory for .docx files and delete them.
    :param directory: Directory to monitor.
    """
    # Configure logging
    logging.basicConfig(
        filename="file_deletion.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info(f"Starting to monitor directory: {directory}")

    try:
        while True:
            # List all files in the directory
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)

                # Check if the file has a .docx extension
                if os.path.isfile(filepath) and filename.endswith(".docx"):
                    try:
                        os.remove(filepath)
                        logging.info(f"Deleted file: {filepath}")
                    except Exception as e:
                        logging.error(f"Error deleting file {filepath}: {e}")

            # Sleep for a short time before checking again
            time.sleep(5)

    except KeyboardInterrupt:
        logging.info("Daemon stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify the directory to monitor
    directory_to_monitor = "./"  # Replace with the target directory

    if not os.path.exists(directory_to_monitor):
        print(f"The directory {directory_to_monitor} does not exist.")
    else:
        monitor_directory(directory_to_monitor)