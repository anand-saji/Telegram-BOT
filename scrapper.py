import requests
from bs4 import BeautifulSoup


def scrap(new=0):
#Making a GET request
  r = requests.get('https://ktu.edu.in/eu/core/announcements.htm')
  lt = 0
  
  #reads stored notification title
  if r.status_code == 200 :
    print("Scrapping website...")
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    s = soup.find('div', class_='c-details')
  
    content = s.find_all('li')
    
    links = s.find_all('a')

    if(new==0):
      fpr=open("notif.txt","r")
      notific=fpr.read()
      print(notific)
      fpr.close()
      l=[]
      lt=0
      print(content[lt].b.text)
      print(notific)
      print(content[lt].b.text!=notific)

      while (content[lt].b.text!=notific):
        # print(lt)
        sss = links[lt].get('href').split(" ")
        description = content[lt].text
        # if description[len(content[0].b.text)+1:] == "Notification" :
        #   description=""
        
        link ='https://ktu.edu.in' + sss[0].strip("\r\n") +sss[len(sss) - 1].strip("\t")
        title = content[lt].b.text
        des = description[len(content[lt].b.text)+1:].replace("Notification","").strip("\n")
      
        # message = f'*{title}*\n\n{des}\n\n{link}'
        dy = {}
        dy["title"] = title
        dy["description"] = des
        dy["link"] = link
        # filt(title)
        #print(dy)
        l.append(dy)
        # print("in loop")
        # print("Successfully parsed!")
        lt=lt+1
      
      print(lt)
      fpr=open("notif.txt","w")
      fpr.write(content[0].b.text)
      fpr.close()

    #print(l)
      return l
    # return message 
    else:
      sss = links[lt].get('href').split(" ")
      description = content[lt].text
        # if description[len(content[0].b.text)+1:] == "Notification" :
        #   description=""
        
      link ='https://ktu.edu.in' + sss[0].strip("\r\n") +sss[len(sss) - 1].strip("\t")
      title = content[lt].b.text
      des = description[len(content[lt].b.text)+1:].replace("Notification","").strip("\n")

      dy = {}
      dy["title"] = title
      dy["description"] = des
      dy["link"] = link

      return dy


  