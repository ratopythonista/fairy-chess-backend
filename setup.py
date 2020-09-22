# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re

from setuptools import find_packages, setup

dev_requirements = [
    'pylama',
    'pytest',
]
unit_test_requirements = [
    'pytest',
]
integration_test_requirements = [
    'pytest',
]
run_requirements = [
    'loguru==0.5.1',
    'fastapi==0.60.0',
    'uvicorn==0.10.3',
    'gunicorn==19.9.0',
    'psycopg2==2.8.5',
    'python-multipart==0.0.5',
    'email-validator==1.1.1',
    'cryptography==3.1',
    'python-jose==3.2.0',
    'bcrypt==3.2.0',
    'passlib==1.7.2',
    'yagmail==0.11.224'
]

with io.open('./fairy_chess/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="fairy-chess",
    version=version,
    author="Rodrigo Guimarães Araújo",
    author_email="rodrigoara27@gmail.com.br",
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    url="https://github.com/ratopythonista/fairy-chess",
    license="COPYRIGHT",
    description="Fairy Chess",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
         'integration': integration_test_requirements,
    },
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8'
    ],
    keywords=(),
    entry_points={
        'console_scripts': [
            'fairy_chess = fairy_chess.__main__:start'
        ],
    },
)
