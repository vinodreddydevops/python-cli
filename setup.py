from setuptools import setup
setup(
	name="auto",
	version="1.0",
	py_modules=['myauto'],
	install_requires=[
	'click', 
	'pyyaml',
	],
	entry_points='''
	[console_scripts]
	auto=myauto:cli
	''',
	)