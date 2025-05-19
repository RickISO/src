from setuptools import setup

package_name = 'ros2_garra_control_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ricardo',
    maintainer_email='ricardo@example.com',
    description='Servicio para controlar la garra en ROS 2 usando Python',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'garra_service = ros2_garra_control_py.garra_service:main',
        ],
    },
)

