from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent

requirements_dir = here.glob('requirements/*.py')

install_requires = []

try:
    for requirements in requirements_dir:
        with requirements.open(mode='rt', encoding='utf-8') as fp:
            lines = list(fp)
            install_requires +=(
                line.split('#')[0].strip() for line in lines
                if not line.startswith('git+') and not line.startswith('#')
            )
except IndexError:
    raise RuntimeError('requirements are broken.')

install_requires = list(filter(None, install_requires))

version = '0.1.0'

setup(
    name='findrestaurants',
    version=version,
    install_requires=install_requires,
    python_requires='>=3.6.0',
    include_package_data=True,
    package_data={
        '': ['*.jsonl'],
    },
    package=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'find_restaurants     = find.entrypoints.find:entrypoint',
        ],
    },
)
