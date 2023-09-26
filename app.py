from flask import Flask, request
import currencyapicom
API_KEY="cur_live_9SV4BxZHyszCHWGgrvRgk8Z8VNSBXtfXcJiPPiAi"

client = currencyapicom.Client(API_KEY)


def converter(c: str, cs: list):
    result = client.latest(c, currencies=cs)
    
    return result
print(converter("USD",["UZS"]))
app = Flask(__name__)

usd = 11380.7 # 1 USD = 11380.7 UZS


@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    params = request.args
    amount = params.get('amount')
    print(converter("USD",["UZS"])['data']['UZS']['value'])
    return {
                "amount": amount,
                "currency": "UZS",
                "converted": round(int(amount)/(converter("USD",["UZS"])['data']['UZS']['value']),2),
                "convertedCurrency": "USD"
            }

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    params = request.args
    amount = params.get('amount')
    return {
                "amount": amount,
                "currency": "USD",
                "converted": int(amount)*float(converter("USD",["UZS"])['data']['UZS']['value']),
                "convertedCurrency": "UZS"
            }

if __name__ == '__main__':
    app.run()    