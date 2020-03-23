#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#=============================================
#
#	QMenú 0.1
#	(c) Wehaa Portal Soft.
#
#=============================================
''' Load '''
from cx_Freeze import setup, Executable
import sys, os

incfiles = ["icons.ico", "bkp", "imagen", "views", "docs", "controlador.py", "variables.py", "iniciar.pyw", "README.md", "LICENSE"] # include any files here that you wish
inc = ['atexit','PyQt5','sqlite3','json','os'] #'PyQt5','sqlite3','json','os'

excludes = []
packages = []

base = None
if sys.platform == "win32":
    base = "Win32GUI"

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "QMenu",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]qmenu.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

exe = Executable(
 # what to build
   script = "iniciar.pyw", # the name of your main python script goes here 
   initScript = None,
   base = base, # if creating a GUI instead of a console app, type "Win32GUI"
   targetName = "qmenu.exe", # this is the name of the executable file      
   shortcutName = "QMenu",
   shortcutDir = 'DesktopFolder',
   icon = 'icons.ico' #"bkp/icons8-inspection-100.png" # if you want to use an icon file, specify the file name here
)

setup(
 # the actual setup & the definition of other misc. info
    name = "QMenu", # program name
    version = "0.1",
    description = "Menú básico para viandas",
    long_description = ''.join(open('README.md', encoding='utf-8').readlines()),
    #long_description_content_type='text/markdown',
    author = "Pacheco, Matias W.",
    author_email = "mwpacheco@outlook.es",
    maintainer="Wehaa Portal Soft.",
    maintainer_email="mwpacheco@outlook.es",    
    keywords = "QMenú",
    license = "MIT",
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Operating System :: Microsoft :: Windows',
    ],
    options = {"build_exe": {"excludes":excludes,"packages":packages,
      "include_files":incfiles,"no_compress": True, }, "bdist_msi": bdist_msi_options}, #"zip_include_packages": "", "zip_exclude_packages": ""
    executables = [exe]
)
