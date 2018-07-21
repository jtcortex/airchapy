#!/usr/bin/python

import json
import os

# Variables
pid = ""
port = "8080"

listen_all_interfaces = 1
fldigi_xmlrpc_server_url = 'http://localhost:7362/RPC2'

macro_tx = 11

current_modem = 'PSK500R'
frequency_carrier = '1500'

must_encrypt = 0
passphrase = "password"

must_use_call_sign = 0
callsign = ""

must_news_broadcast = 0
rss_feeds = []

must_community_broadcast = 0
community_feeds = []

must_tweet_others = 0
must_tweet_broadcast = 0

twitter_hashtag2follow = "#anonymous"
searchtwterm = ""

# Twitter account info (future use)
consumer_key_default = ""
consumer_secret_default = ""
access_token_default = ""
access_token_secret_default = ""

must_use_proxy = 1

tor_proxy_host = "127.0.0.1"
tor_proxy_port = "9050"

proxy_host = "127.0.0.1"
proxy_port = 8118
proxy_user = ""
proxy_pass = ""

settings = ""

messages_sent = []
asked_resend = []
answered_resend = []
already_asked = []

new_messages = []

current_messages = ""

current_log_txt = ""

done_decoded_msgs = []

twitter_results = ""

check_news = 0
check_community = 0
check_twitter = 0

must_ask2resend = 0
must_answer_resend_req = 0

crypt_idx = "000000"

build_routes = 1

last_check = 0
last_checkr_send = 0

folder = "/bin"

keys = {}
rtable = {}

os.umask(077)

def save_settings():
    data = {}
    data['fldigi_xmlrpc_server_url'] = fldigi_xmlrpc_server_url
    data['port'] = port
    data['listen_all_interfaces'] = listen_all_interfaces
    data['current_modem'] = current_modem
    data['frequency_carrier'] = frequency_carrier
    data['must_encrypt'] = must_encrypt
    data['passphrase'] = passphrase
    data['must_use_call_sign'] = must_use_call_sign
    data['callsign'] = callsign
    data['must_news_broadcast'] = must_news_broadcast
    data['rss_feeds'] = rss_feeds
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port
    data['port'] = port

    json_data = json.dumps(data)
    print json_data

save_settings()

def load_settings():
    print "/bin" #print $FindBin::Bin;

    if (os.path.exists(".airchapysettings")
            config_file = "/.airchappysettings"
            with open(config_file, "r+") as f:
                
