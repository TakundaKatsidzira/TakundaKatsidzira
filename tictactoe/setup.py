from setuptools import setup, find_packages

setup(
    name="tictactoe",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A command-line TicTacToe game with AI agents and logging.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tictactoe",  # Update as needed
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        # list dependencies here, e.g.
        # "numpy>=1.21.0",
    ],
    entry_points={
        "console_scripts": [
            "play-tictactoe = scripts.play_tictactoe:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
