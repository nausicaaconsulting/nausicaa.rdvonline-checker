from setuptools import setup


setup(
    name='stock_listing',
    install_requires=[
        'click',

        'requests',
        'marshmallow',

        # Webscraping
        'beautifulsoup4',
        'lxml',

        # Environment variable parsing
        'environs',

        # Schedule jobs (cron-like)
        'schedule',

        'selenium',

        # Run everything together
        'supervisor',
    ],
    extras_require={
        'dev': [
            'pipdeptree',
        ]
    },
)
