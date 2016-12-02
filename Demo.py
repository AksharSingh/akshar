import json


def string_task(str1, str2):
    str2_count = 0
    word_count = 0
    str2_string = ''
    list_of_words = str1.split()

    for word in list_of_words:
        if str2.lower() == word.lower():
            str2_count += 1
            str2_string += ' ' + word
        word_count += 1

    sentance = ' '.join(list_of_words).replace(str2, '') + str2_string
    print sentance
    print str2_count


def json_task():
    with open('sample.json', 'r') as f:
        json_data = json.load(f)
        json_data['featureConfigs']['features'][2]['firewallRules']['firewallRules'][0]['application']['service'][0][
            'protocol'] = "udp"
        json_data['vnics']['vnics'][2] = 'EXT_VLAN_201b'
        json_data['featureConfigs']['features'][5]['ospf']['enabled'] = True
        for each in json_data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours']:
            each['holdDownTimer'] = each['holdDownTimer'] + each['keepAliveTimer']

    with open('sample.json', 'w') as f:
        f.write(json.dumps(json_data))


print(string_task('the quick brown fox jumps over the lazy the the the dog.', 'the'))
