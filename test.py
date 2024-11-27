import requests
from bs4 import BeautifulSoup

#İklim Değişikliğinin Nedenleri
url = "https://www.akdenizkoruma.org.tr/tr/calismalarimiz/iklim-krizi/b/deniz-suyu-sicakligi-izleme?gad_source=1&gclid=EAIaIQobChMIhP_p_4DaiQMVG2dBAh1_3AQkEAAYAiAAEgKRXPD_BwE"  

sayfa = requests.get(url)
print(sayfa)