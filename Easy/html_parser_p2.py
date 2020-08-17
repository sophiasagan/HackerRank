from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment ")
        else:
            print(">>> Single-line Comment ")
        print(data)

    def handle_data(self, data):
        if not data == '\n':
            print(">>> Data")
            print(data) 
html = ""   

n = (int(input()))

for i in range(n):
    html += input().rstrip()+'\n'
   
parser = MyHTMLParser()
parser.feed(html)
parser.close()


