import urllib.request

from tqdm import tqdm


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)


url_bn = 'http://ia802604.us.archive.org/19/items/alhelawy07/'
path_bn = 'bn/'
for i in range(1, 4):
    file_name = 'bn{:>02d}.pdf'.format(i)
    url_i = url_bn + file_name
    download_url(url_i, path_bn + file_name)
