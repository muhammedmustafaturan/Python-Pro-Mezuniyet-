import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
app = Flask(__name__)


#İklim Değişikliğinin Nedenleri
url = "https://www.magdeburger.com.tr/blog/kuresel-iklim-degisikligi"

sayfa = requests.get(url)
print(sayfa)
html_sayfa = BeautifulSoup(sayfa.content,'html.parser')

my_divs = html_sayfa.find_all("div", {"class": "col-12 col-lg-8 col-xxl-9 mb-5 mb-lg-0"})

for i in my_divs:
    with open("bilgiler.txt","w+", encoding="UTF-8") as f:
        metin = i.find('ol').text
        #f.write("Bırıncı sıteden aldıgım bılgı:")
        f.write(metin + " ")
        f.write("\n")   
        
    print("dosyaya yazma ışlemı bıttı")


#İklim Değişikliğinin Sonuçları
#url_2 = "https://www.akdenizkoruma.org.tr/tr/calismalarimiz/iklim-krizi/b/deniz-suyu-sicakligi-izleme?gad_source=1&gclid=EAIaIQobChMIhP_p_4DaiQMVG2dBAh1_3AQkEAAYAiAAEgKRXPD_BwE"  

#sayfa_2 = requests.get(url_2)
#print(sayfa_2)
#html_sayfa_2 = BeautifulSoup(sayfa_2.content,'html.parser')

#my_divs_2 = html_sayfa_2.find_all("div" , {"class": 'description'})

#for i in my_divs_2:
 #    with open("bilgiler.txt", "a+" , encoding = "UTF-8") as f:
       
  #      metin_2 = i.find('p').text    
  #      f.write(metin_2)
   #     f.write("\n")
    #    print("2. dosyaya yazma işlemi bitti.")   


#İklim Değişikliğinin Türkiye'nin Üzerindeki Etkileri
url_3 = "https://www.aydemenerji.com.tr/blog/164/iklim-degisikligi-nedir-nedenleri-nelerdir-/"  

sayfa_3 = requests.get(url_3)
print(sayfa_3)
html_sayfa_3 = BeautifulSoup(sayfa_3.content,'html.parser')
    
my_divs_3 = html_sayfa_3.find_all("span" , {"style": 'font-family:Arial, sans-serif '})

for i in my_divs_3:
    with open("bilgiler.txt", "a+" , encoding = "UTF-8") as f:
        f.write("\n")
        metin_3 = i.find('p').text    
        f.write(f'{metin_3}\n')
       
    print("3. dosyaya yazma işlemi bitti.")   

@app.route("/")
def anasayfa():
    with open("bilgiler.txt", "r", encoding="utf-8") as f:
        bilgi = f.read()

    return render_template("index.html",bilgi = bilgi)

app.run(debug=True)