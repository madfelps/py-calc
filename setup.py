from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='pycalc',
    version='0.0.1',
    url='https://github.com/madfelps/py-calc',
    license='MIT License',
    author='Felipe Moura',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='fmoura7@live.com',
    keywords='Pacote',
    description=u'Exemplo de pacote PyPI',
    packages=['pycalc'],
    install_requires=['numpy'],)