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
    uncompressed = "/data/web_static/releases/" + filename + "/"

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p " + uncompressed)
        run("tar -xzf /tmp/" + filename + ".tgz -C " + uncompressed)
        run("rm /tmp/" + filename + ".tgz")
        run("mv " + uncompressed + "web_static/* " + uncompressed)
        run("rm -rf " + uncompressed + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + uncompressed + " /data/web_static/current")
        print("New version deployed!")
        return True
    except:
        return False


def do_pack():
    '''packs up all files from web_static to tgz'''
    try:
        local("mkdir -p versions")
        now = datetime.now()
        form = now.strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_" + form + ".tgz"
        form = "tar -cvzf " + filename + " web_static"
        local(form)
        return filename
    except:
        return None


def deploy():
    '''automate prevoius functions'''
    archive_path = do_pack()
    if not archive_path:
        return False
    d_d = do_deploy(archive_path)
    return d_d
