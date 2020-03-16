'''
covid.py - Phenny Coronavirus Module
'''

import web

@web.with_scraped_page('https://www.worldometers.info/coronavirus/')
def scrape_stats(doc):
    elements = doc.find_class('maincounter-number')
    return ( i.text_content().strip() for i in elements )

def covid(phenny, input):
    phenny.say('Loading COVID-19 statistics...')
    cases, deaths, recovered = scrape_stats()
    phenny.say('Cases\t\t{}'.format(cases))
    phenny.say('Deaths\t\t{}'.format(deaths))
    phenny.say('Recovered\t{}'.format(recovered))
covid.commands = ['covid', 'covid19', 'coronavirus', '2019ncov', 'sarscov2']
covid.example = '.covid'
covid.priority = 'medium'
