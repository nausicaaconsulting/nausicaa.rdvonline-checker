from setuptools import setup


setup(
    name='rdv_online',
    install_requires=[
        'requests',
        # Environment variable parsing
        'environs',
        'selenium',
        'kivy',
    ],
    extras_require={
        'dev': [
            'pipdeptree',
        ]
    },
)
