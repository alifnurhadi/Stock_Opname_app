from PyInstaller.utils.hooks import collect_all, collect_submodules, collect_dynamic_libs

# Collect all submodules
hiddenimports = collect_submodules('rapidfuzz')

# Collect all data files and binaries
datas, binaries = [], []
_datas, _binaries, _hiddenimports = collect_all('rapidfuzz')
datas.extend(_datas)
binaries.extend(_binaries)

# Explicitly add C extensions
extra_binaries = collect_dynamic_libs('rapidfuzz')
binaries.extend(extra_binaries)