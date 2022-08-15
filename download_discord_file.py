from urllib import request
import urllib
import os

hdr = ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', )

opener = urllib.request.build_opener()
opener.addheaders = [hdr]
urllib.request.install_opener(opener)
cwd = os.getcwd()


def download_discord_file(url, folder, seed):
    if not os.path.isdir('images'):
        os.mkdir('images')
    folder = folder.strip()
    folder_path = os.path.join('images', folder)
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

    name = os.path.join(cwd, 'images', folder, '{}.png'.format(seed))

    return request.urlretrieve(url, name)
