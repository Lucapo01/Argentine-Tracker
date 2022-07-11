import re

try:
    regex_patrimonios = r"""<!-- ngIf: row\.tipo == 'data' --><td class="ng-binding ng-scope" ng-if="row\.tipo == 'data'">(.*?)<\/td><!-- end ngIf: row.tipo == 'data' -->"""
    raw_data: str = ""
    with open("raw_data.txt", "r") as f:
        raw_data =  f.read()
    
    text_data_per_string = re.findall(regex_patrimonios, raw_data)
    name_tickers = r"""<!-- ngIf: row.tipo == 'data' --><td class="ng-binding ng-scope" ng-if="row.tipo == 'data'" style="text-align:left">(.*?)</td><!-- end ngIf: row.tipo == 'data' -->"""

    text_data_tickers = re.findall(name_tickers, raw_data)
    text_data_per =  [float(i) for i in text_data_per_string]


    patrimony_string = re.search(r"""<!-- ngIf: row.tipo == 'pie' --><td class="ng-scope" ng-if="row.tipo == 'pie'"><strong class="ng-binding">(.*?)</strong></td><!-- end ngIf: row.tipo == 'pie' -->""", raw_data).group(1)

    patrimony_float=float(re.sub(",","",patrimony_string))
    for i in range(len(text_data_per)): 
        text_data_per[i]= round(text_data_per[i]*patrimony_float /100, 2)




    result = {
        "tickers":text_data_tickers,
        "qty": text_data_per,
        "patrimony": patrimony_float
    }   
    print(result)

except:
    result = {
        "tickers":[],
        "qty": [],
        "patrimony": 0
    } 
    print(result)