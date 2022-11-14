import time
import concurrent.futures
import requests
import threading

img_urls = ['https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg',
            'https://cdn.pixabay.com/photo/2022/11/04/08/29/water-7569331_960_720.jpg']

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name + '.jpg', 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    T = []
    for i in range(len(img_urls)):
        t1 = threading.Thread(target=download_image, args=[img_urls[i]])
        t1.start()
        T.append(t1)
    end = time.perf_counter()


