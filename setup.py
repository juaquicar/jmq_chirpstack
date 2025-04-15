from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='mi_paquete',
    version='0.1.0',
    author='Tu Nombre',
    author_email='tu.email@example.com',
    description='Una descripción breve de tu paquete',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tu_usuario/mi_paquete',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
