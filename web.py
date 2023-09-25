# $pip install whois
# $pip install python-whois

import whois
domain=input("enter your domain : ")
doamin_info=whois.whois(domain)
for key,value in doamin_info.items():
    print(key,':',value)
    
    
# print(domain.__dict__)
# # print(domain.expiration_date)





