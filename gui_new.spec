# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gui_new.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('business_logic.py', '.'),
    ],
    hiddenimports=[
        'polars',
        'gui_new',
        'pandas',
        'fastexcel',
        'sqlite3',
        'rapidfuzz',
        'pandastable',
        'threading'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'notebook',
        'scipy',
        'statsmodels' ,
        'SQLAlchemy' ,
        'scikit-learn' ,
        'streamlit' ,
        'fastapi'
    ],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure , a.zipped_data , compression=False)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='asteros-stok opname',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[],
)

