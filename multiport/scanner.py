"""
Scanner is a module that implements basic sync/async port scanning functionality.
"""
import logging
import socket
from dataclasses import dataclass
from typing import List


@dataclass
class Scanner:
    """
    Scanner implements port scanning functionality.
    """

    host: str
    open_ports: List[int]
    socket: socket.socket

    def __init__(self, host: str):
        self.host = host
        self.open_ports = []
        self.socket = socket.socket()
        logging.debug(f"Socket at host {self.host} has been created.")

    def __del__(self):
        self.socket.close()
        logging.debug(f"Socket at host {self.host} has been closed.")

    def scan(self, port: int):
        """Scans whether the given port is open."""
        try:
            logging.debug(f"Trying to connect to {self.host}:{port}.")
            self.socket.connect((self.host, port))
            self.open_ports.append(port)
            logging.debug(f"Port {self.host}:{port} is open.")
        except ConnectionRefusedError:
            logging.debug(f"Port {self.host}:{port} is closed.")
        except OSError as os_error:
            logging.debug(os_error)
        else:
            self.socket.shutdown(socket.SHUT_RDWR)
            logging.debug(f"Connection to port {self.host}:{port} has been shut down.")
