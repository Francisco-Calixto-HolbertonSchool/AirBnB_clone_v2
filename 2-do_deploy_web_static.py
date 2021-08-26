#!/usr/bin/python3
'''has function that generates tgz for web static files'''

from fabric.api import local, env, run, put
from datetime import datetime
import os


env.hosts = ['35.243.197.246', '35.196.27.66']


def do_deploy(archive_path):
    '''distributes an archive to your web servers'''


    s = archive_path.split('/')
    filename = s[-1].split('.')[0]
    uncompressed = "/data/web_static/releases/" + filename+ "/"

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p " + uncompressed)
        run("tar -xzf /tmp/" + filename + ".tgz -C " + uncompressed)
        run("rm /tmp/" + filename + ".tgz")
        run("rm /data/web_static/current")
        run("ln -sf " + uncompressed + " /data/web_static/current")
        return True
    except:
        return False
