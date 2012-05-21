# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), '/home/tanmay/Code/EclipseWorkspace/Comic Downloader/TComicDown.py'],
             pathex=['/home/tanmay/Code/Downloads/pyinstaller-1.5.1'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'TComicDown'),
          debug=False,
          strip=False,
          upx=True,
          console=1 )
