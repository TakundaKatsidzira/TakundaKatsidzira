from setuptools import setup, find_packages

setup(
    name="sequence_game",
    version="0.1.0",
    description="Python implementation of the Sequence board game with CPU opponents",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/sequence_game",  # Optional: your repo URL
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0",    # CLI parsing library
        # Add more dependencies here as you add them
    ],
    entry_points={
        "console_scripts": [
            "sequence-game=scripts.play_sequence:main",  # CLI entry point (you'll implement main())
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
