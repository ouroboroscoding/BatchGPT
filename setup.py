from setuptools import setup

with open('README.md', 'r') as oF:
	long_description=oF.read()

setup(
	name='ListGPT',
	version='1.0.0',
	description='Simple tool to automate batching of prompts using a list and a template',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://ouroboroscoding.com/body/blog',
	project_urls={
		'Documentation': 'https://ouroboroscoding.com/body/blog',
		'Source': 'https://github.com/ouroboroscoding/blog',
		'Tracker': 'https://github.com/ouroboroscoding/blog/issues'
	},
	keywords=['rest','microservices'],
	author='Chris Nasr - Ouroboros Coding Inc.',
	author_email='chris@ouroboroscoding.com',
	license='Custom',
	packages=['listgpt'],
	python_requires='>=3.10',
	install_requires=[
		'bottle>=0.12.25,<0.13',
		'jsonb>=1.0.0,<1.1',
		'openai>=1.6.1,<1.7',
		'tools-oc>=1.2.2,<1.3',
		'undefined-oc>=1.0.0,<1.1'
	],
	entry_points={
		'console_scripts': ['listgpt=listgpt.__main__:cli']
	},
	zip_safe=True
)