"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
59
* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import urllib.request


def count_dots_on_i(url: str):
    temp = 0
    try:
        temp2 = urllib.request.urlopen(url)
        the_page = str(temp2.read())
        print(the_page)
        for i in the_page:
            if i == 'i':
                temp += 1
        return temp
    except urllib.error.URLError:
        raise ValueError(f"Unreachable {url}")
