import os
import datetime
import subprocess
from multiprocessing import Process
from oai_config import OAI_DICT, OUT_PATH

here = os.path.abspath(os.path.dirname(__file__))


def harvest(code, oai_url, md_prefix, oai_set):
    """
    harvester subprocess
    :param code: institution code used for directory structure
    :param oai_url: oai endpoint url
    :param md_prefix: metadataprefix for endpoint metadata
    :param oai_set: current set to harvest from oai_sets list
    """
    if not os.path.isdir(OUT_PATH + code):
        os.mkdir(OUT_PATH + code)
    ofile = OUT_PATH + code + '/' + oai_set + '_' + datetime.date.isoformat(datetime.date.today()) + '.xml'
    subprocess.run([os.path.join(here, 'pyoaiharvester/pyoaiharvest.py'),
                    '-l{}'.format(oai_url),
                    '-m{}'.format(md_prefix),
                    '-s{}'.format(oai_set),
                    '-o{}'.format(ofile)
                    ], stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    for provider in OAI_DICT:
        args = (OAI_DICT[provider].code, OAI_DICT[provider].oai_url, OAI_DICT[provider].mdprefix)
        for oai_set in OAI_DICT[provider].oai_sets:
            p = Process(target=harvest, args=(args[0], args[1], args[2], oai_set, ))
            p.start()
            p.join()
