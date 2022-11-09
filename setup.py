from setuptools import setup, find_packages


setup(
    name='example_deploy_project',
    version='1.1.3',
    license='MIT',
    author="Mark",
    author_email='email@example.com',
    packages=find_packages('example_package_mark_dot'),
    package_dir={'': 'src'},
    url='https://github.com/Markelii/deploy-project',
    keywords='example project',
    install_requires=[
      ],

)