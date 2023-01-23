from kivymd_extensions.akivymd import *
from kivy.utils import platform

from bootstrap import Bootstrap

if __name__ == '__main__':
    if platform == 'android':
        from android.permissions import request_permissions, Permission

        request_permissions([
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.INTERNET,
        ])

    Bootstrap.initEnviroment()
    Bootstrap.run()