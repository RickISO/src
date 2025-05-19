from setuptools import setup

package_name = 'football_tracker'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'opencv-python'],
    zip_safe=True,
    maintainer='ricardo',
    maintainer_email='ricardo@example.com',
    description='Nodo para detectar un balón azul',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tracker_node = football_tracker.tracker_node:main',
        ],
    },
)
