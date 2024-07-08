from application.interface.service import IServiceLogic
from application.interface.session import ISession


class ServiceLogic(IServiceLogic):

    def __init__(self, session: ISession):
        self._session = session

    def __call__(self, *args, **kwargs):
        print("START LOGIC")
        a = self._session.get_a()
        print(a)
        print("END LOGIC")
