```python
from setuptools import setup, find_packages

setup(
    name='umi-uber-eats-integration',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'google-auth',
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'google-api-python-client',
        'oauthlib',
        'httplib2',
    ],
    entry_points='''
        [console_scripts]
        umi=src.main:main
    ''',
)
```