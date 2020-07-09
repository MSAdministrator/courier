from setuptools import setup, find_packages

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

version = dict()
with open("./conductor/utils/version.py") as fp:
    exec(fp.read(), version)


setup(
    name='conductor',
    version=version['__version__'],
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package to execute code remotely to multiple operating system platforms',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['conductor', 'winrm', 'ssh', 'cmd', 'powershell'],
    url='https://github.com/MSAdministrator/conductor',
    author='MSAdministrator',
    author_email='rickardja@live.com',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4'
)