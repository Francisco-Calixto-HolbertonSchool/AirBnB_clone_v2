#!/usr/bin/python3
'''has function that generates tgz for web static files'''

from fabric.api import local
from datetime import datetime


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
