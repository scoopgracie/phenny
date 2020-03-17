import logging

logger = logging.getLogger('phenny')

try:
    import stockquotes
except:
    logger.warn('Please install Beautiful Soup 4 and Requests for the stocks module to work!')
    del getquote

def getquote(phenny, input):
    """.stock <ticker> - Check stock quote"""
    ticker = input.group(1)
    if ticker is None:
        phenny.say('Usage: .stock <ticker>, e.g. .stock kr')
        return
    
    phenny.say('Loading quote...')

    try:
        stock = stockquotes.Stock(input.group(1))
    except stockquotes.StockDoesNotExistError:
        phenny.say('I couldn\'t find that stock.')
        return
    except Exception as e:
        phenny.say('An error occurred.')
        raise e
    
    if len(str(stock.currentPrice).split('.')[1]) < 2:
        price = '{}0'.format(stock.currentPrice)
    else:
        price = str(stock.currentPrice)
    
    if len(str(stock.increaseDollars).split('.')[1]) < 2:
        change = '{}0'.format(stock.increaseDollars)
    else:
        change = str(stock.increaseDollars)

    phenny.say('{} - {}'.format(stock.symbol, stock.name))
    if stock.increaseDollars > 0:
        phenny.say('{} [+{} (+{}%)]'.format(price, change, stock.increasePercent))
    else:
        phenny.say('{} [{} ({}%)]'.format(price, change, stock.increasePercent))
getquote.commands = ['stock', '.quote']
getquote.priority = 'low'
getquote.example = '.stock KR'
