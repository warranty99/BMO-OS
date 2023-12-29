from setuptools import setup

setup(
    name='BMOOS',
    version='0.2',
    packages=['BMOOS'],
    install_requires=[
        'elevenlabs',
        'openai',
        'numpy',
        'sounddevice',
        #For now..
    ],
)
