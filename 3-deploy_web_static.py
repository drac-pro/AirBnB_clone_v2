#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers"""
from datetime import datetime
from fabric.api import local, env, put, run, runs_once
import os


env.user = 'ubuntu'
env.hosts = ['52.4.1.57', '52.3.244.12']


@runs_once
def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    if not os.path.isdir('versions'):
        os.makedirs('versions')
    file = "versions/web_static_{}.tgz".\
        format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("tar -czvf {} web_static".format(file))
    if not os.path.exists(file):
        return None
    return file


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
        run('rm -rf /tmp/{}'.format(file_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(remote_path))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
