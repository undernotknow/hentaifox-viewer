from urllib import response
import requests
from bs4 import BeautifulSoup as bs

BASE_URL='https://hentaifox.com'

def fetchHTML(url:str):
    response=  requests.get(url=url)
    if response.status_code== 200:
        return bs(response.content,'html.parser')
    else:
        raise Exception(f"Cannot fetch data from {url}")

def getFirstImagePage(html:bs):
    galleryDiv= html.find('div',{'class':'display_gallery'})
    thumbDiv= galleryDiv.find('div',{'class':'gallery_thumb'})
    link=thumbDiv.find('a')['href']
    return str(link)

def getImageLinkPattern(html:bs):
    firstImgLink=getFirstImagePage(html=html)
    page=fetchHTML(f'{BASE_URL}{firstImgLink}')
    fullImgDiv=page.find('div',{'class':'full_image'})
    img=fullImgDiv.find('img')
    # galleryDiv= html.find('div',{'class':'display_gallery'})
    # thumbDiv= galleryDiv.find('div',{'class':'gallery_thumb'})
    # pattern=str(thumbDiv.find('img')['data-src'])
    return str(img['data-src'])


def processGalleryById(id:str):
    link=f'{BASE_URL}/gallery/{id}'
    html=fetchHTML(link)
    return getImageLinkPattern(html=html)