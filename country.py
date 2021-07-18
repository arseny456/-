countries = ['usa', 'russia', 'china', 'brazil', 'france']

capitals = dict()

capitals['usa'] = 'washington'
capitals['russia'] = 'moscow'
capitals['china'] = 'pekin'
capitals['brazil'] = 'brazilia'
capitals['france'] = 'paris'


for country in capitals:
    print('столица ' + str(country) + ' это ' + str(capitals[country]))