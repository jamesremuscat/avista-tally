from autobahn.twisted.component import run as run_component

from .client import component


def run():
    run_component(component)


if __name__ == '__main__':
    run()
