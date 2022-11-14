import time
import concurrent.futures
import requests
import threading
import multiprocessing

img_urls = ['https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg']

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name + '.jpg', 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end = time.perf_counter()
    print(f"Pool ended in {round(end - start, 2)} second(s)")

    T = []
    for i in range(len(img_urls)):
        t1 = threading.Thread(target=download_image, args=[img_urls[i]])
        t1.start()
        T.append(t1)
    end = time.perf_counter()
    print(f"Thread ended in {round(end - start, 2)} second(s)")

    start = time.perf_counter()

    p1 = multiprocessing.Process(
        target=download_image('https://cdn.pixabay.com/photo/2016/07/21/15/25/minecraft-1532775_960_720.png'))
    p2 = multiprocessing.Process(
        target=download_image('https://cdn.pixabay.com/photo/2016/08/08/10/48/minecraft-1578075_960_720.png'))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()
    print(f"Process ended in {round(end - start, 2)} second(s)")
