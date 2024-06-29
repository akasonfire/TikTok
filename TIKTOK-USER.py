#--------এইটা হইলো tiktok user info code---------#
#--------নাম এবং logo change করে নিয়েন--------#
#--------Coded by : MD SUYAIB ISLAM--------#

import requests

def tiktok():
    logo = ("""
        _   _   _    _ __  
    / _|| | | \ \ / // \  |_ _| ) 
    \____ \| | | |\ V // _ \  | ||  _ \ 
      _) | |_| | | |/ _ \ | || |_) |
    |/ \_/  |_/_/   \_\_|/ 
    """)
    print(logo)
    
    user_input = input('Enter Tiktok Username: ')
    url = f'http://localhost:8080/tiktok-info.php?username={user_input}'
    
    try:
        req = requests.get(url).json()
        
        print(req)
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

tiktok()