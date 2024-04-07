#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives"""
from fabric.api import env, run, local


env.user = 'ubuntu'
env.hosts = ['52.4.1.57', '52.3.244.12']


def do_clean(number=0):
    """deletes out-of-date archives
    Args:
        number(int) - number of archives to keep
    """
    number = int(number)
    if number < 0:
        return
    if number == 0:
        number = 1

    if env.host_string == env.hosts[0]:
        local(f"find ./versions/ -type f -name 'web_static_*.tgz'"
              f" | grep -E './versions/web_static_[0-9]{{14}}.tgz'"
              f" | sort | head -n -{number} | xargs -I [] rm -rf []")

    run(f"find /data/web_static/releases/ -type d -name 'web_static_*'"
        f" | grep -E '/data/web_static/releases/web_static_[0-9]{{14}}'"
        f" | sort | head -n -{number} | xargs -I [] rm -rf []")
