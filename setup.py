from setuptools import setup, find_packages

setup(
    name="ollama_llama",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ollama_llama=ollama_llama.main:main_cli',
        ],
    },
)
