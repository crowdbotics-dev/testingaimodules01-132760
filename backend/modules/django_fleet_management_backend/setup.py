from setuptools import setup
from setuptools.command.build import build


class BuildCommand(build):
    def initialize_options(self):
        build.initialize_options(self)
        self.build_base = "/tmp"


setup(
    name="cb_django_fleet_management_backend",
    version="0.1",
    packages=["fleet_management_backend"],
    install_requires=[],
    cmdclass={"build": BuildCommand},
)
