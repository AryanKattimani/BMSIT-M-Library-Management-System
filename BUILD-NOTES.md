# Build notes

A Windows EXE is intentionally built on Windows using PyInstaller. The current execution environment is not a Windows/PyInstaller build host, so this source package includes the complete PyInstaller specifications and `build.bat` rather than pretending that a Windows binary was produced here.

`BMSIT-Library.spec` builds personal/local mode.

`BMSIT-Library-Server.spec` builds LAN server mode. `launcher.py` automatically detects the `-Server` executable name and enables server mode.
