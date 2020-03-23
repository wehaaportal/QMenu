# -*- coding: utf-8 -*-
#=============================================
#
#	QMenú 0.1
#	(c) Wehaa Portal Soft.
#
#=============================================
from __future__ import unicode_literals
import os, sys

''' PyQt5 '''
from PyQt5 import Qt, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

HOME_PATH = QDir.toNativeSeparators(QDir.homePath())
HOME_QMENU_PATH = os.path.join(HOME_PATH, "QMenu")
WORKING_FOLDER = os.path.realpath(os.path.dirname(sys.argv[0]))

DATABASE_PATH = os.path.join(HOME_QMENU_PATH, "database")