"""discord command"""


class Command:
    """Command class"""
    def __init__(self, message: str, name: str, assets: str, uses_args: bool,
                 description: str):
        self.message = message
        self.name = name
        self.uses_args = uses_args
        self.assets = assets
        self.description = description

