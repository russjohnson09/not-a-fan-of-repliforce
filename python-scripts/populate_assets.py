
from yt_dlp import YoutubeDL
import os


IRIS_DEATH = "https://www.youtube.com/watch?v=3IPIPLM8ELY"


_dir = os.path.dirname(__file__)
_assets_dir = os.path.abspath(os.path.join(_dir, 'assets'))

def _get_full_path(downloaded, format = 'mp4', directory = _dir):
    id = downloaded.get('id')
    title = downloaded.get('title')

    filename = f'{title} [{id}].{format}'
    return  os.path.abspath(os.path.join(_dir, filename))

def _download_iris():
    # os.chdir(_assets_dir, 'iris')
    # https://stackoverflow.com/questions/41240726/change-the-output-name-when-download-with-youtube-dl-using-python
    ydl_opts = {'outtmpl': 'assets/iris_death.mp4'}
    with YoutubeDL(ydl_opts) as ydl:
        downloaded = ydl.extract_info(IRIS_DEATH)
        print("result")
        print(downloaded.get('id'))
        print(downloaded.get('title'))
        fullpath = _get_full_path(downloaded)
        print(fullpath)
        # os.rename(fullpath, os.path.abspath(os.path.join(_assets_dir, 'iris_death.mp4')))
        # Megaman X4： Iris's Death [3IPIPLM8ELY].mp4


def main():

    print("populate_assets")
    _download_iris()

main()