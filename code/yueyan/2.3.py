def describe_city(city,country='China'):
    str=city+' is in '+country
    return (str)
print(describe_city('Beijing'))#默认参数
print(describe_city('Vegas','America'))
print(describe_city('Paris','France'))
