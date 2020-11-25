import requests
import random
from colorama import *
init()
import threading
import json
import subprocess, requests, time, os



tokenread = open("tokens.txt", "r").read()


print('')



tokensplit = tokenread.split("\n")
print(f"{Fore.CYAN}[1]{Fore.YELLOW} DM Bot" + Fore.RESET)
print(f"{Fore.CYAN}[2]{Fore.YELLOW} Sever Joiner" + Fore.RESET)
print(f"{Fore.CYAN}[3]{Fore.YELLOW} Server Message Spammer" + Fore.RESET)
print(f"{Fore.CYAN}[4]{Fore.YELLOW} Server Join Spammer" + Fore.RESET)
print(f"{Fore.CYAN}[5]{Fore.YELLOW} Group Spammer" + Fore.RESET)
print(f"{Fore.CYAN}[6]{Fore.YELLOW} Friend Request Bot" + Fore.RESET)
print(f"{Fore.CYAN}[7]{Fore.YELLOW} Status Changer" + Fore.RESET)
print(f"{Fore.CYAN}[8]{Fore.YELLOW} Friend Request Spammer" + Fore.RESET)
print(f"{Fore.CYAN}[9]{Fore.YELLOW} Server Leaver" + Fore.RESET)


choice = input('    > ')


token = random.choice(tokensplit)

if choice == ('1'):
    channel_id = input('Enter the DM Code: ')
    msg = input('Enter a MSG To Spam: ')
    number = (int(input('Enter How Many MSGs: ')))
    url_dm = 'https://discord.com/api/v8/channels/' + channel_id + '/messages'
    dm_ref = 'https://discord.com/channels/@me/' + channel_id
    data_dm = {
        'content': msg,
    }
    for _ in range(number):
        token1 = random.choice(tokensplit)
        print(token1)
        headers_dm1 = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'origin': 'https://discord.com',
            'referer': dm_ref,
            'authorization': token1
            
        }
        a = requests.post(url_dm, headers=headers_dm1, data=data_dm)
        print('MSG sent: ' + msg)





def server_joiner():
    for _ in range(number):
        token2 = random.choice(tokensplit)
        print(token2)
        headers_default2 = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'authorization': token2
        }
        b = requests.post(url_server_join, headers=headers_default2)
        print(b.text)





if choice == '2':
    invite = input('Enter an Invite Code: ')
    number = (int(input('How many tokens: ')))
    url_server_join = 'https://discord.com/api/v8/invites/' + invite
    t1 = threading.Thread(target=server_joiner)
    t2 = threading.Thread(target=server_joiner)

    t1.start()
    t2.start()





token = random.choice(tokensplit)






if choice == '4':
    server_join_spammer = input('Enter a Server ID: ')
    server_join_invite = input('Enter an Server invite: ')

    
    number = (int(input('Enter How Many tokens: ')))
    url_server_spammer = 'https://discord.com/api/v8/users/@me/guilds/' + server_join_spammer
    url_server_join = 'https://discord.com/api/v8/invites/' + server_join_invite
    for _ in range(number):
        token4 = random.choice(tokensplit)
        headers_default4 = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'authorization': token4
        }
        b = requests.post(url_server_join, headers=headers_default4)
        print('Joined Server:' + server_join_invite)
        e = requests.delete(url_server_spammer, headers=headers_default4)
        print('Left Server: ' + server_join_invite)





if choice == '5':
    print('You need to be friended with the person!')
    token5 = input('Enter a token: ')
    rec_1 = input('Enter The DM code of the First Person: ')
    rec_2 = input('Second Person To add: ')
    number = (int(input('How many groups: ')))
    url_group = 'https://discord.com/api/v8/channels/'+ rec_1 + '/recipients/' + rec_2
    headers_group = {
        'authorization': token5,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    }
    for _ in range(number):
        x = requests.put(url_group, headers=headers_group)
        print(x.status_code)
        dict_group = x.text
        y = json.loads(dict_group)
        print(y)










def server_bomber():
    for _ in range(number):
        token3 = random.choice(tokensplit)
        headers_default3 = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'authorization': token3,
            'origin': 'https: // discord.com',
            'referer': 'https: // discord.com / channels/' + server_id + '/' + server_channel_id
        }
        d = requests.post(url_server_msg, headers=headers_default3, data=server_data)
        print('MSG sent: ' + msg)


if choice == '3':
    server_id = input('Enter a server ID: ')
    if server_id == '730427438206681129':
        print('This is a blacklisted server')
        print('Shutting down in 5 seconds')
        quit()
    server_channel_id = input('Enter a server channel ID: ')
    msg = input('Enter a msg to send: ')
    number = (int(input('Enter How Many tokens: ')))
    url_server_msg = 'https://discord.com/api/v8/channels/' + server_channel_id + '/messages'
    server_data = {
        'content': msg
    }
    t1 = threading.Thread(target=server_bomber)
    t2 = threading.Thread(target=server_bomber)

    t1.start()
    t2.start()


def status_changer():
    for _ in range(number):
        token7 = random.choice(tokensplit)
        headers_status = {
            'authorization': token7,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
        status = requests.patch(url_status, headers=headers_status, json=params_status)
        print('Status Changed: ' + status_text)


if choice =='7':
    status_text = input('Status text: ')
    number = (int(input('How many Tokens: ')))
    url_status = 'https://discord.com/api/v8/users/@me/settings'

    params_status = {
        'custom_status': {'text': status_text}
    }

    t1 = threading.Thread(target=status_changer)
    t2 = threading.Thread(target=status_changer)

    t1.start()
    t2.start()



def normal_friend():
    for _ in range(number):
        token8 = random.choice(tokensplit)
        headers_friend = {
            'authorization': token8,
            'content-type': 'application/json'
        }
        friend_request = requests.post(url_friend, headers=headers_friend, json=json_friend)
        print('Friend Request Sent:' + friend_name)



if choice == '6':
    url_friend = 'https://discord.com/api/v8/users/@me/relationships'
    friend_name = input('Enter The EXACT name: ')
    friend_tag = input('Enter the tag without 0\'s: ')
    number = (int(input('How many Tokens: ')))

    json_friend = {
        'discriminator': friend_tag,
        'username': friend_name
    }

    t1 = threading.Thread(target=normal_friend)
    t2 = threading.Thread(target=normal_friend)

    t1.start()
    t2.start()


def unfriend():
    for _ in range(number):
        token9 = random.choice(tokensplit)
        headers_unfriend = {
            'authorization': token9,
            'content-type': 'application/json'
        }
        unfriend = requests.delete(url_unfriend, headers=headers_unfriend)
        friend_request = requests.post(url_friend, headers=headers_unfriend, json=json_friend)
        print('Friend Request Sent:' + friend_name)


if choice == '8':
    url_friend = 'https://discord.com/api/v8/users/@me/relationships'
    friend_name = input('Enter The EXACT name: ')
    friend_tag = input('Enter the tag without beginning 0\'s: ')

    json_friend = {
        'discriminator': friend_tag,
        'username': friend_name
    }


    unfriend_ID = input('Enter The Person\'s ID: ')
    number = (int(input('How many tokens: ')))
    url_unfriend = 'https://discord.com/api/v8/users/@me/relationships/' + unfriend_ID


    t1 = threading.Thread(target=unfriend)
    t2 = threading.Thread(target=unfriend)

    t1.start()
    t2.start()



if choice == '9':
    server_id_leave = input('Enter a server ID: ')
    url_server_leave = f'https://discord.com/api/v8/users/@me/guilds/{server_id_leave}'


    number = int(input('How many tokens: '))
    for _ in range(number):
        token10 = random.choice(tokensplit)
        headers_serverleave = {
            'authorization': token10
        }

        server_leave = requests.delete(url_server_leave, headers=headers_serverleave)
        print(f'Token Left: {token10}')


if choice == '10':
    url = 'https://discord.com/api/v8/channels/757312548461871264/messages/757340829831659550/reactions/emoji_28%3A749468433418027059/%40me'

    headers_test = {
        'authorization': 'NzY3MTY4MDI0NzMzMjg2NDAw.X4t_MQ.LfaGazuCmuPNa7Vq2EQmXW9ITec'
    }

    testing = requests.put(url, headers=headers_test)
    print(testing.text)
