# https://zen.yandex.ru/media/id/5eda66ac221f4123b4d84830/kak-zapakovat-prilojenie-na-python-v-exe-fail-5eda7eb1e8e24e636af4df92
# *_setup.py build

from cx_Freeze import setup, Executable
# import PyQt5.Qt.plugins.platforms
executables = [Executable('Main.py',
                          targetName='login_system.exe',
                          base='Win32GUI',
                          )]

includes = ['PyQt5', 'PyQt5.sip', 'SQLAlchemy', 'sys', 'pathlib']

zip_include_packages = ['PyQt5', 'PyQt5.sip', 'SQLAlchemy', 'sys', 'pathlib']

include_files = ['./venv-login-system/Lib/site-packages/PyQt5/Qt/plugins/platforms']

options = {
    'build_exe': {
        'include_msvcr': True,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'login_system_build',
        'include_files': include_files,
    }
}

setup(name='login_system',
      version='1.0.0',
      description='App',
      executables=executables,
      options=options)
