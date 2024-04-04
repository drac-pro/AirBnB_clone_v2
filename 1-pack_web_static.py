#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    if not os.path.isdir('versions'):
        os.makedirs('versions')
    file = "versions/web_static_{}.tgz".\
        format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("tar -czvf {} web_static".format(file))
    if not os.path.exists(file):
        return None
