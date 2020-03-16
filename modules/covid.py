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
    current = format(int(cases.replace(',', '')) - ( int(deaths.replace(',', '')) + int(recovered.replace(',', '')) ), ',d')
    phenny.say('Cases\t\t{}'.format(cases))
    phenny.say('Current\t{}'.format(current))
    phenny.say('Deaths\t\t{}'.format(deaths))
    phenny.say('Recovered\t{}'.format(recovered))
    phenny.say('Recovery rate\t\t{}%'.format(round(int(recovered.replace(',', ''))/int(cases.replace(',', '')) * 10000) / 100))
    phenny.say('Death rate\t\t\t{}%'.format(round(int(deaths.replace(',', ''))/int(cases.replace(',', '')) * 10000) / 100))
    phenny.say('Recoveries/Deaths\t{}'.format(round(int(recovered.replace(',', ''))/int(deaths.replace(',', '')) * 100 ) / 100 ))
    phenny.say('This is not medical advice.')

    
covid.commands = ['covid', 'covid19', 'coronavirus', '2019ncov', 'sarscov2']
covid.example = '.covid'
covid.priority = 'medium'
