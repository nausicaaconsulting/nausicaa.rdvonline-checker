from setuptools import setup


setup(
    name='stock_listing',
    install_requires=[
        'click',

        'requests',

        # Environment variable parsing
        'environs',

        # Schedule jobs (cron-like)
        'schedule',

        'selenium',
    ],
    extras_require={
        'dev': [
            'pipdeptree',
        ]
    },
)
