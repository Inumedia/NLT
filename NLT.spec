# -*- mode: python -*-

block_cipher = None


a = Analysis(['NLT.py'],
             pathex=['C:\\Users\\ghardin\\PycharmProjects\\EnvChanger'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='NLT',
          debug=False,
          strip=False,
          upx=True,
          console=False , uac_admin=True, icon='logo.ico')
coll = COLLECT(exe,
               strip=False,
               upx=True,
               name='NLT'
)