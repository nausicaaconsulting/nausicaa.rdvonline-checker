from setuptools import setup


setup(
    name='rdv_online',
    install_requires=[
        'requests',
        # Environment variable parsing
        'environs',
        'selenium',
    ],
    extras_require={
        'dev': [
            'pipdeptree',
        ]
    },
)
