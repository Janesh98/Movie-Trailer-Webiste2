from bs4 import BeautifulSoup
import requests
import imdb
from threading import Thread

movie_poster_urls = {}

def handle_threading(threads):
    # function to be used by another function to handle threads
    for t in threads:
        t.start()

    for t in threads:
        t.join()


def get_mov_id():

    i = imdb.IMDb()
    top250 = i.get_top250_movies()

    return [[m.movieID, m['title']] for m in top250]


def get_img_url(l):

    title = l[1]

    start = "https://www.imdb.com/title/tt"
    movie_id = l[0]
    end = "/?ref_=fn_al_tt_1"

    url = start + movie_id + end

    html_page = requests.get(url)
    data = html_page.text

    soup = BeautifulSoup(data, features="lxml")

    link = soup.find("div", class_="poster")

    # extract image link
    link = str(link).split("<")[3].split("\"")[3]
    movie_poster_urls[title] = [link, yt_link(title)]
    return

def yt_link(title):

    # https://www.youtube.com/results?search_query=interstellar+movie+trailer

    start = "https://www.youtube.com/results?search_query="
    if len(title.split()) > 1:
        middle = "+".join([s for s in title.split()])
    else:
        middle = title
    end = "+movie+trailer"

    url = start + middle + end

    html_page = requests.get(url)
    data = html_page.text

    soup = BeautifulSoup(data, features="lxml")

    soup = str(soup).split(" ")

    yt_id = ""
    for s in soup:
        if "href=\"/watch?v=" in s:
            yt_id = s
            break

    #remove "><div" from end of youtube id
    if yt_id[len(yt_id)-1-4 : len(yt_id)] == "><div":
        yt_id = yt_id[:len(yt_id)-1-4]

    # extract youtube id
    yt_id = yt_id.split("=")[2]

    trailer = "https://www.youtube.com/watch?v=" + yt_id
    return trailer

def main():
    id_list = get_mov_id()

    threads = []

    for l in id_list:
        t = Thread(target=get_img_url, args=(l,))
        threads.append(t)

    handle_threading(threads)

    print(movie_poster_urls)

if __name__ == '__main__':
    main()
