#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers"""
from fabric.api import env, put, run
import os


env.user = 'ubuntu'
env.hosts = ['52.4.1.57', '52.3.244.12']


def do_deploy(archive_path):
    """distributes an archive to your web servers
    Args:
        archive_path(string)
    Returns:
        true otherwise false
    """
    if not os.path.exists(archive_path):
        return False

    file_ext = os.path.basename(archive_path)
    file_name = file_ext.split('.')[0]
    remote_path = '/data/web_static/releases/{}/'.format(file_name)

    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(remote_path))
        run('tar -xzf /tmp/{} -C {} --strip-components=1'.format
            (file_ext, remote_path))
        run('rm /tmp/{}'.format(file_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(remote_path))
        return True
    except Exception:
        return False
