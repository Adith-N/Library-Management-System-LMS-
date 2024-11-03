# importing requests package
import requests	 
import time as t
def NewsFromBBC():
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "4dbc17e007ab436fb66416009dfb59a8"
	}
	main_url = " https://newsapi.org/v1/articles"
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()
	article = open_bbc_page["articles"]
	results = []
	for ar in article:
		results.append(ar["title"])
		
	for i in range(len(results)):
            print(i + 1, results[i])
            t.sleep(1)

#RUN CODE
if __name__ == '__main__':
	NewsFromBBC() 
