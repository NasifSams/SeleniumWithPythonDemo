import logging
import os
from pathlib import Path

class LogGen:
    @staticmethod
    def loggen():
        log_dir = Path("./Logs")  # Using Path object
        log_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

        # Configure logging
        logging.basicConfig(
            filename=log_dir / "automation.log",  # Using Path object to specify the file
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S'
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
