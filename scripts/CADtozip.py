# Created by Yael Maguire yael@fb.com
# v1.0, 4/24/2011

import zipfile
from os import mkdir,rmdir
from os.path import splitext, join
import glob
import shutil

def createZip(fname,addStep=True):
    basename = splitext(fname)[0]
    ext = splitext(fname)[1]
    print basename,ext
    print ext=='.dxf'
    try:
        mkdir(basename)
    except OSError:
        pass
    file = zipfile.ZipFile(basename+'.zip',"w")
    shutil.copy('License.html',basename)
    file.write(join(basename,'License.html'),compress_type=zipfile.ZIP_DEFLATED)
    shutil.copy(fname,basename)
    file.write(join(basename,fname),compress_type=zipfile.ZIP_DEFLATED)
    if addStep is True:
        if (ext != '.dxf'):
            shutil.copy(basename+'.step',basename)
            file.write(join(basename,basename+'.step'),compress_type=zipfile.ZIP_DEFLATED)
    file.close()
    shutil.rmtree(basename)

for name in glob.glob('*.dxf'):
    createZip(name)
for name in glob.glob('*.sldasm'):
    createZip(name)
