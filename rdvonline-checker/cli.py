import logging
import rdvonline_web

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    postal_code = '33380'
    distance = 50
    nb_persons = 1

    rdvonline_web.check_available_date(postal_code, distance, nb_persons)
