from setuptools import setup

setup(
	name="frida-gadgetify",
	version="0.1",
	url="https://github.com/Manouchehri/frida-gadgetify",
	author="David Manouchehri",
	description=("Binary injection tool for Frida")
	keywords="binary injection frida reverse engineering",
	py_modules=["frida-gadgetify"],
	install_requires=[
		"lief"
	],
	entry_points="""
		[console_scripts]
		frida-gadgetify=frida-gadgetify:main
	"""
)
