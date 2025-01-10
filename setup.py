from setuptools import setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    py_modules=[],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sora Hirano',
    maintainer_email='s23c1115wh@s.chibakoudai.jp',
    description='A ROS 2 package to publish Sotobo Line stations from Chiba to Awa-Kamogawa.',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'station_publisher = mypkg.sotobo_line_stations:main',
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/talk_listen.launch.py']),
    ],
)

