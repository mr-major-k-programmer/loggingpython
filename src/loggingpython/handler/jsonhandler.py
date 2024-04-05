import os
import json
from datetime import datetime

from .handler import Handler


class JSONHandler(Handler):
    """
    A class for handling log messages in JSON format.

    This class inherits from the Handler class and implements specific
    methods for formatting and outputting log messages in JSON files. It
    supports the creation of new log files based on the current date and
    allows customization of the log format string. The JSONHandler ensures
    that log messages are stored in a structured and easily accessible format,
    making it suitable for further analysis or review. It also includes
    features for hashing log messages for unique identification and updating
    the log file if the current date has changed.
    """
    def __init__(self, name: str, path: str = "logs") -> None:
        """
        Initializes the JSONHandler with the given name, log path, and log
            format string.

        Args:
            name (str): The name of the log file.
            path (str, optional): The path where the log files will be
                stored. Defaults to "logs".
            logformat_string (str, optional): The format string for the log
                messages. Defaults to "%(asctime)s: [%(loggername)s]:
                [%(loglevel)s]: %(message)s".
        """
        self._mk_logdir(path)
        self.name: str = name
        self.path: str = path
        self._current_date: str = datetime.now().strftime("%Y-%m-%d")
        self.file: str = f"{self.path}/{self.name}_{self._current_date}.json"
        self._mk_logfile(self.file)
        # Initialisieren Sie das JSON-Objekt hier
        self.log_data: dict[str, str] = {}

    def emit(self, record: dict) -> None:
        """
        Adds a log message to the JSON object and checks whether the
            date has been changed.
        Args:
            record (dict): A dictionary containing the details of the log
                entry. contains the details of the log entry.
        """
        formatted_message = self._format_message(record)
        message_hash = hash(str(formatted_message))

        self.log_data[str(message_hash)] = formatted_message
        self._update_file()
        self._write_log_data_to_file()

    def _write_log_data_to_file(self) -> None:
        """
        Writes the JSON object to the file.
        """
        with open(self.file, 'w') as file:
            file.write(json.dumps(self.log_data, indent=4))

    def _update_file(self):
        """
        Updates the log file if the current date has changed.
        """
        current_date = datetime.now().strftime("%Y-%m-%d")
        if current_date != self._current_date:
            self._current_date = current_date
            self._close_file()
            file: str = f"{self.path}/{self.name}_{self._current_date}.json"
            self.file = open(file, "a")
            self.log_data: dict[str, str] = {}

    def _close_file(self):
        """
        Closes the current log file.
        """
        if self.file:
            self.file.close()

    def _mk_logdir(self, logpath: str) -> None:
        """
        Creates the log directory if it does not exist.

        Args:
            logpath (str): The path of the log directory.
        """
        if not os.path.exists(logpath):
            os.makedirs(logpath)

    def _mk_logfile(self, file: str) -> None:
        """
        Creates the log file if it does not exist.

        Args:
            file (str): The path of the log file.
        """
        if not os.path.exists(file):
            os.open(file, os.O_CREAT)

    def _get_datestemp(self) -> str:
        """
        Returns the current date in the format "YYYY-MM-DD".

        Returns:
            str: The current date.
        """
        return datetime.now().strftime("%Y-%m-%d")

    def _format_message(self, record: dict) -> str:
        """
        Formats a log message based on the provided log data.

        Args:
            record (dict): A dictionary containing the log message details.

        Returns:
            str: The formatted log message.
        """
        values = {
            "loggername": record.get("loggername", ""),
            "iso_8601_time": record.get("iso_8601_time", ""),
            "asctime": record.get("asctime", ""),
            "loglevel": record.get("loglevel", ""),
            "message": record.get("message", ""),
        }

        return self._format_in_json(values)

    def _format_in_json(self, record: dict) -> dict:
        """
        Formats a log message based on the provided log data into a JSON
            object with hashed keys.

        Args:
            record (dict): A dictionary containing the log message details.

        Returns:
            dict: The formatted log message as a JSON object with hashed keys.
        """
        sorted_keys = sorted(record.keys())
        string_representation = str({key: record[key] for key in sorted_keys})
        message_hash = hash(string_representation)
        values = {
            message_hash: record,
        }
        return values

    def __repr__(self) -> str:
        return f"JSONHandler:{self.name}, {self.path}, {self.logformat_string}"

    def __str__(self) -> str:
        return f"JSONHandler:{self.name}, {self.path}, {self.logformat_string}"
