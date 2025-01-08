from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sora Hirano',
    maintainer_email='s23c1115wh@s.chibakoudai.jp',
    description='Tokyo Station Delay Info Publisher',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tokyo_station_delay_info = mypkg.tokyo_station_delay_info:main',
        ],
    },
    install_scripts=['scripts'],
    script_dir='scripts'
)

