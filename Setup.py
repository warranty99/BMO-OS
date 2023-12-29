from setuptools import setup

setup(
    name='BMOOS',
    version='0.5',
    packages=['BMOOS'],
    install_requires=[
        'elevenlabs',
        'openai',
        'numpy',
        'sounddevice',
        'pillow',
        #For now..
    ],
)
