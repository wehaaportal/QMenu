[![GitHub License](https://img.shields.io/github/license/wehaaportal/QMenu)](https://github.com/wehaaportal/QMenu/blob/master/LICENSE) 
[![GitHub Release](https://img.shields.io/github/v/release/wehaaportal/QMenu?include_prereleases)](https://github.com/wehaaportal/QMenu/releases)
![GitHub Size](https://img.shields.io/github/repo-size/wehaaportal/QMenu)


![QMenú Captura](https://github.com/wehaaportal/QMenu/blob/master/docs/captura.png "QMenú")

# QMenú 0.1
===============================================================================

QMenú es un generador de menú básico para viandas 

Esta aplicación fue creada con la intensión de modernizar el trabajo de las
Comidas Rápidas, permitiéndoles digitalizar viandas diarias.
Estos datos tendrán un soporte digital (Base de datos), y un respaldo
en formato PDF para luego llevarlo al papel.

# Wehaa Portal Soft.
===============================================================================
  - Pacheco, Matias W.
  - <mwpacheco@outlook.es>
  - MIT License

# Tecnologias:
===============================================================================
  - Python3 3.8
  - PyQt5 5.10
  
# Setup:
===============================================================================
Puede descargar Python desde el [Sitio Oficial](https://www.python.org/downloads/). Para este software, se recomienda la versión 3.8. También necesitaremos instalar [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5).

> Si está instalando Python en Windows, solo recuerde marcar la casilla "Agregar Python a la RUTA" durante la instalación.

## Instalación de PyQt5:

Para instalar `PyQt5` usaremos `pip`. Después de instalar Python, abra una terminal e ingrese lo siguiente:
```
$ pip install PyQt5
```

## Ejecutable e Instalador para Windows

Para crear el Ejecutable:
```
$ python.exe setup.py build
```

Para crear un Instalador:
```
$ python.exe setup.py bdist_msi
```
