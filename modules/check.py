def checkup(phenny, input):
    """.checkup - Check if begiak is up"""
    phenny.say("Status: online")
checkup.commands = ['checkup']
checkup.priority = 'high'
checkup.example = '.checkup'
