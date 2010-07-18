#! /usr/bin/python
import sys, os
from distutils.core import setup
from glob import glob

# to install type: 
# python setup.py install --root=/

locales=map(lambda i: ('share/'+i,[''+i+'/ojuba-personal-lock.mo',]),glob('locale/*/LC_MESSAGES'))
data_files=[
  ('share/ojuba-personal-lock/', glob('data/*.svg')),
  ('share/icons/hicolor/scalable/apps/', glob('data/*.svg')),
  ('share/applications/', glob('*.desktop'))
]
data_files.extend(locales)
setup (name='ojuba-personal-lock', version='0.2.2',
      description='Personal Folder Encrpytion Tool',
      author='Muayyad Saleh Alsadi',
      author_email='alsadi@ojuba.org',
      url='http://git.ojuba.org/cgit/ojuba-personal-lock/about/',
      license='Waqf',
      scripts=['ojuba-personal-lock'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
      data_files=data_files
)


