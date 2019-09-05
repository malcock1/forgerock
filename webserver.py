#!/usr/bin/env python3

import sys
import requests
from os import environ as env
from http.server import HTTPServer, BaseHTTPRequestHandler
from statistics import mean


def generate_request_handler(SYMBOL, NDAYS, APIKEY):
    class ApiRequestHandler(BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            self.url = "https://www.alphavantage.co/query?apikey={} \
                    &function=TIME_SERIES_DAILY_ADJUSTED&symbol={}".format(APIKEY, SYMBOL)

            super(ApiRequestHandler, self).__init__(*args, **kwargs)

        def get_api_data(self):
            try:
                response = requests.get(self.url).json()["Time Series (Daily)"]
                ndays_keys = list(response.keys())[:int(NDAYS)]

                closing_values = [float(response[key]['4. close']) for key in ndays_keys]

                response_string = "{0:s} data={1:s}, average={2:.2f}".format(
                                                                        SYMBOL,
                                                                        repr(closing_values),
                                                                        mean(closing_values)
                                                                    )
                return response_string

            except KeyError as e:
                print(e, file=sys.stderr)
                return "Error: response data not valid" 
        
            except TypeError as e:
                print(e, file=sys.stderr)
                return "Error: input data not valid" 

            except Exception as e:
                print(e, file=sys.stderr)
                return "Error: unhandled exception"    

        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            message = self.get_api_data()
            self.wfile.write(str.encode(message))
            return

    return ApiRequestHandler

def main():
    SYMBOL = env.get("SYMBOL")
    NDAYS  = env.get("NDAYS")
    APIKEY  = env.get("APIKEY")

    if SYMBOL is None or NDAYS is None or APIKEY is None:
        print("Please specify SYMBOL, NDAYS and APIKEY environment variables", \
            file=sys.stderr)
        exit(1)

    handler = generate_request_handler(SYMBOL, NDAYS, APIKEY)
    httpd = HTTPServer(('', 8000), handler)
    httpd.serve_forever()

    exit(0)

if __name__ == "__main__":
    main()
