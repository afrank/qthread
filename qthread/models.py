
class QObj:
    def __init__(self, action="", **kwargs):
        self._action = action
        self._args = kwargs

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
