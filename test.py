from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OmYyM2YwZGZlOWNiZTNlOTY5OGZiMTJhMzM4NWQxODYy'

security_api = intrinio_sdk.SecurityApi()

active = True # bool | When True, return securities that are active. When False, return securities that are not active. A security is considered active if it has traded or has had a corporate action in the past 30 days, and has not been merged into another security (such as due to ticker changes or corporate restructurings). (optional)
delisted = False # bool | When True, return securities that have been delisted from their exchange. Note that there may be a newer security for the same company that has been relisted on a differente exchange. When False, return securities that have not been delisted. (optional)
code = '' # str | Return securities classified with the given code reference [see - https://docs.intrinio.com/documentation/security_codes]. (optional)
currency = '' # str | Return securities traded in the given 3-digit ISO 4217 currency code reference [see - https://en.wikipedia.org/wiki/ISO_4217]. (optional)
ticker = '' # str | Return securities traded with the given ticker. Note that securities across the world (and through time) may trade with the same ticker but represent different companies. Use this in conjuction with other parameters for more specificity. (optional)
name = '' # str | Return securities with the given text in their name (not case sensitive). (optional)
composite_mic = '' # str | Return securities classified under the composite exchange with the given Market Identification Code (MIC). A composite exchange may or may not be a real exchange.  For example, the USCOMP exchange (our only composite exchange to date) is a combination of exchanges with the following MICs: ARCX, XASE, XPOR, FINR, XCIS, XNAS, XNYS, BATS.  This composite grouping is done for user convenience.  At this time, all US securities are classified under the composite exchange with MIC USCOMP.  To query for specific US exchanges, use the exchange_mic parameter below.  (optional)
exchange_mic = '' # str | The MIC code of the exchange where the security is actually traded. (optional)
stock_prices_after = '' # date | Return securities with end-of-day stock prices on or after this date. (optional)
stock_prices_before = '' # date | Return securities with end-of-day stock prices on or before this date. (optional)
cik = '' # str | Return securities belonging to the company with the given Central Index Key (CIK). (optional)
figi = '' # str | Return securities with the given Exchange Level FIGI reference [see - https://www.openfigi.com/about]. (optional)
composite_figi = '' # str | Return securities with the given Country Composite FIGI reference [see - https://www.openfigi.com/about]. (optional)
share_class_figi = '' # str | Return securities with the given Global Share Class FIGI reference [see - https://www.openfigi.com/about]. (optional)
figi_unique_id = '' # str | Return securities with the given FIGI Unique ID reference [see - https://www.openfigi.com/about]. (optional)
include_non_figi = False # bool | When True, include securities that do not have a FIGI. By default, this is False. If this parameter is not specified, only securities with a FIGI are returned. (optional) (default to False)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = security_api.get_all_securities(active=active, delisted=delisted, code=code, currency=currency, ticker=ticker, name=name, composite_mic=composite_mic, exchange_mic=exchange_mic, stock_prices_after=stock_prices_after, stock_prices_before=stock_prices_before, cik=cik, figi=figi, composite_figi=composite_figi, share_class_figi=share_class_figi, figi_unique_id=figi_unique_id, include_non_figi=include_non_figi, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_all_securities: %s\r\n" % e)
    
