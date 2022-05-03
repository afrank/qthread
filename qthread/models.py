
class QObj:
    def __init__(self, route="default", action="", **kwargs):
        self._route = route
        self._action = action
        self._args = kwargs

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, route):
        self._route = route

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, args):
        self._args = args
