# https://github.com/pikepdf/pikepdf
# https://pikepdf.readthedocs.io/en/latest/index.html

import pikepdf
from pathlib import Path


def unlockpikepdf(data, suff='_unlock', dirtosave=''):

    if Path(data).is_file():
        filename = str(Path(data).name)
        with pikepdf.open(filename) as pdf:
            pdf.save(dirtosave + filename.replace(str(Path(data).suffix),
                                                  suff+str(Path(data).suffix)))
    elif Path(data).is_dir():
        for i in list(Path(data).glob('**/*.pdf')):
            i = str(i)
            with pikepdf.open(i) as pdf:
                pdf.save(dirtosave + i.replace(str(Path(i).suffix),
                                               suff+str(Path(i).suffix)))
