from abc import ABC, abstractmethod
from render_template import render_template


class View():
    template = ''

    @abstractmethod
    def get(self, environ):
        pass
