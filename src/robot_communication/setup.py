from setuptools import find_packages, setup

package_name = 'robot_communication'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            'share/' + package_name + '/launch',
            ['launch/robot_communication.launch.py']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pranav Tarkase',
    maintainer_email='pranav@example.com',
    description='Robot publisher and subscriber communication',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'robot_publisher = robot_communication.robot_publisher:main',
            'robot_subscriber = robot_communication.robot_subscriber:main',
        ],
    },
)
