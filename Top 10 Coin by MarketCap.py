# Automated Looping

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
cg_list = cg.get_coins_markets(vs_currency='usd')
excluded = ['usdt', 'usdc', 'busd', 'wbtc', 'dai', 'bch', 'ust', 'shib', 'doge', 'etc']
top_ten_rank = 1


for i in cg_list:  # i is each dict in cg_list here
    if i['symbol'] in excluded: # checks If symbol is the same as a value in the excluded list
        continue # If the above true then continue skips the rest of the code and starts from the top (for loop) again
    while top_ten_rank <= 10: # If not skipped while loop starts checking if top_ten_rank is <= 10
        print('Top Ten Rank {} -- Market Cap Rank = {} -- Coin = {} -- Name = {} -- Market Cap = {}  '.format(top_ten_rank,
                                                                            i['market_cap_rank'], i['symbol'],
                                                                            i['id'], i['market_cap']))
        # ^^ prints the current value of top_ten_rank and the values in the current dict getting read
        break # Causes the while loop to stop as soon as it prints and move on
    top_ten_rank += 1 # Updates the value for the next iteration



"""
# MANUALL SCRIPT
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
cg_list = cg.get_coins_markets(vs_currency='usd') # Raw list
excluded = ['usdt', 'usdc', 'busd', 'wbtc', 'dai', 'bch', 'ust' ] # symbols I want to skip over
index = 0 # index counter


first_MC = {key: cg_list[index][key] for key in cg_list[index].keys()  # index = 0 , grabbed the dict in position index from cg_list
            & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}
index += 1  # index = 1 , add 1 to index position to move on to the next dict in list cg_list

if cg_list[index]['symbol'] in excluded or cg_list[index]['symbol'] == first_MC['symbol']: # Skip dict in position index if in excluded list or in previous dict
    index += 1

second_MC = {key: cg_list[index][key] for key in cg_list[index].keys()  # index = 1
             & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}
index += 1  # index = 2

if cg_list[index]['symbol'] in excluded or cg_list[index]['symbol'] == second_MC['symbol']:
    index += 1

third_MC = {key: cg_list[index][key] for key in cg_list[index].keys()  # index = 2
            & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}
index += 1  # index = 3

if cg_list[index]['symbol'] in excluded or cg_list[index]['symbol'] == third_MC['symbol']:
    index += 1  # index = 4

fourth_MC = {key: cg_list[index][key] for key in cg_list[index].keys()  # index = 4
             & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}
index += 1  # index = 5

if cg_list[index]['symbol'] in excluded or cg_list[index]['symbol'] == fourth_MC['symbol']:
    index += 1

fifth_MC = {key: cg_list[index][key] for key in cg_list[index].keys()
            & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}
index += 1

sixth_MC = {key: cg_list[index][key] for key in cg_list[index].keys()
            & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}
index += 1

if cg_list[index]['symbol'] in excluded or cg_list[index]['symbol'] == fourth_MC['symbol']:
    index += 1

seventh_MC = {key: cg_list[index][key] for key in cg_list[index].keys()
              & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}
index += 1

if cg_list[index]['symbol'] in excluded or cg_list[index]['symbol'] == fourth_MC['symbol']:
    index += 1

eighth_MC = {key: cg_list[index][key] for key in cg_list[index].keys()
             & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}
index += 1

if cg_list[index]['symbol'] in excluded or cg_list[index]['symbol'] == fourth_MC['symbol']:
    index += 1

ninth_MC = {key: cg_list[index][key] for key in cg_list[index].keys()
            & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}
index += 1

if cg_list[index]['symbol'] in excluded or cg_list[index]['symbol'] == fourth_MC['symbol']:
    index += 1

tenth_MC = {key: cg_list[index][key] for key in cg_list[index].keys()
            & {'id', 'symbol', 'market_cap', 'market_cap_rank'}}

print('', first_MC, '\n', second_MC, '\n', third_MC, '\n', fourth_MC, '\n', fifth_MC, '\n'
      , sixth_MC, '\n', seventh_MC, '\n', eighth_MC, '\n', ninth_MC, '\n', tenth_MC)
      
"""
