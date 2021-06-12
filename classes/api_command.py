"""Command that consumes an api"""
import requests
from .command import Command

class ApiCommand(Command):
    """Command class"""
    def __init__(self, message: str, name: str, assets: [list], uses_args: bool,
                 description: str, api_url: str):
        super().__init__(message, name, assets, uses_args, description)
        self.api_url = api_url

    def get_api(self, argument: str):
        """fetchs the api link that the command needs"""
        api_url = self.api_url + argument
        print(api_url)
        api = requests.get(api_url)
        api = api.json()
        return api
