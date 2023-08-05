from DependenciesContainer import Container
from dependency_injector import providers
from useCases.AccessManager import SimpleAccessManager

container = Container(
    accessManager = providers.Factory(SimpleAccessManager)
)
container.wire(modules=[
    "infrastructure.DataAccessI",
    "infrastructure.AccessController"
])

if __name__ == '__main__':
    from outter.TelegramAPIHandler import TelegramAPIHandler
    tg = TelegramAPIHandler()
    tg.local()