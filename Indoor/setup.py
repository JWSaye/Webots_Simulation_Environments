from setuptools import find_packages, setup

package_name = 'Indoor'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/indoor_sim_env_launch.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/Rodgers Floor 2.wbt', 
]))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/resource', [
    'resource/turtlebot_webots.urdf',
    'resource/ros2control.yml',
]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='Jared Saye',
    maintainer_email='jwsaye@crimson.ua.edu',
    description='2nd Floor of Rodgers Library Webot Environment',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],    
        'console_scripts': ['Indoor = Indoor.Indoor:main']
    },

)
