from setuptools import setup, find_packages

setup(
    name='sequence-game',
    version='0.1.0',
    description='CLI Sequence board game with AI',
    author='Takunda Katsidzira',
    author_email='katsidzirast@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.7',
    install_requires=[
        # Add dependencies here, e.g. 'numpy',
    ],
    entry_points={
        'console_scripts': [
            'sequence=sequence.main:main',  # Updated entry point
        ],
    },
    # Optional fields:
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    # license='MIT',
)
