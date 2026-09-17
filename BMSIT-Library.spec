from PyInstaller.utils.hooks import collect_submodules
hiddenimports=collect_submodules('flask')+collect_submodules('werkzeug')
a=Analysis(['launcher.py'],pathex=['.'],datas=[('frontend','frontend')],hiddenimports=hiddenimports)
pyz=PYZ(a.pure)
exe=EXE(pyz,a.scripts,a.binaries,a.datas,[],name='BMSIT-Library',console=False)
