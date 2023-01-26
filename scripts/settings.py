from environs import Env

env = Env()
env.read_env()

# When deployed in a docker container, the browser should be headless because no screen is available
WEB_CHROME_HEADLESS = env.bool('WEB_CHROME_HEADLESS', False)
# List of email address to notify when a new isin has been submitted
RDVONLINE_BASE_URL = env.str('RDVONLINE_BASE_URL', 'https://rendezvousonline.fr')
