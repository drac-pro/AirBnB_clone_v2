#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers"""
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy


def deploy():
    """creates and distributes an archive to your web servers"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
