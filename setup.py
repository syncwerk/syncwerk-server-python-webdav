from setuptools import setup, find_packages
setup(
    name='syncwerk-server-python-webdav',
    version='20181227',
    author='Syncwerk GmbH',
    author_email='support@syncwerk.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://www.syncwerk.com',
    license='MIT',
    description='WsgiDAV WebDAV Server',
    long_description='WsgiDAV is a generic WebDAV server written in Python and based on WSGI',
    platforms=['any'],
    include_package_data=True,
)
