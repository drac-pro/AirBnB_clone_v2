#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives"""
from fabric.api import env, run, local, cd, lcd
import os


env.user = 'ubuntu'
env.hosts = ['52.4.1.57', '52.3.244.12']


def do_clean(number=0):
    """deletes out-of-date archives
    Args:
        number(int) - number of archives to keep
    """

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]

    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
