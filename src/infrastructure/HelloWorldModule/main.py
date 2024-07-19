from src.core.ports.helloworldport import HelloWorldInterface


class HelloWorld(HelloWorldInterface):
    def __init__(self) -> None:
        self.text = 'Hello world!'

    async def hello_world(self) -> None:
        print(self.text)
