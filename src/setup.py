```python
from setuptools import setup, find_packages

setup(
    name='umi-uber-eats-integration',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'google-auth',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'google-api-python-client',
        'requests',
        'flask',
        'flask_sqlalchemy',
        'flask_migrate',
    ],
    entry_points={
        'console_scripts': [
            'umi=main:main',
        ],
    },
)
```