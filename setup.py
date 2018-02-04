from cx_Freeze import setup, Executable

setup(name='ZotClicker',
		version='0.1',
		description='Bust a Zot',
		executables = [Executable("ZotClicker.py")])