"""discord command"""
import requests


class Command:
    """Command class"""
    def __init__(self, message: str, name: str, assets: list, uses_args: bool,
                 description: str):
        self.message = message
        self.name = name
        self.uses_args = uses_args
        self.assets = assets
        self.description = description

    def fetch_api(self, api):
        """Fetchs an api if the command needs it"""
        self.api = requests.get(api).json()
