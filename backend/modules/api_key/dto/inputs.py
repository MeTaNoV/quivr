from dataclasses import dataclass


@dataclass
class CreateChatProperties:
    name: str

    def __init__(self, name: str):
        self.name = name
