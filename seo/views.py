from django.shortcuts import render
import requests
import bs4
import time

def seo(request):
    return render(request, 'seo/index.html')


def seo1(request):
    search_url_keyword='lalaland'
    if request.POST['keyword']:
        search_url_keyword=request.POST['keyword']
    # if request.method=='POST':
    #     search_url_keyword=request.POST.get('keyword')
    # else:
    #     search_url_keyword='lalaland'
    #検索順位取得処理
    if search_url_keyword and search_url_keyword.strip():
        #Google検索の実施
        search_url = 'https://www.google.co.jp/search?hl=ja&num=10&q=' + search_url_keyword
        res_google = requests.get(search_url)
        res_google.raise_for_status()
        #BeautifulSoupで掲載サイトのURLを取得
        bs4_google = bs4.BeautifulSoup(res_google.text, 'html.parser')
        link_google = bs4_google.select('div > h3.r > a')
        
        result = []
        for i in range(len(link_google)):
            time.sleep(2)
            #なんか変な文字が入るので除く
            site_url = link_google[i].get('href').split('&sa=U&')[0].replace('/url?q=', '')
            site_title=bs4_google.select('div > h3.r > a')[i].text#textで中身抽出。stringでもいいけど今回はnoneが返る
            if 'https://' in site_url or 'http://' in site_url:
                #サイトの内容を解析
                try:
                    result.append("{}位:「{}, URL「{}」\n".format(i+1,site_title,site_url))
                except:
                    continue
            # result.append('\n')

    mapped_num = map(str, result)
    result_string = ' '.join(mapped_num)
                
    return render(request, 'seo/seo.html', {'result':result_string})

