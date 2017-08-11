from urllib.parse import  urlparse
import ast

queries = 0
stack_overflow = 0
github = 0
everything_else = 0
with open('url_details.txt') as f:
    for line in f:
        queries += 1
        line_array = line.split('::')

        for url in ast.literal_eval(line_array[1]):
            parsed_url = urlparse(url)
            if 'github' in parsed_url.netloc.lower() :
                github += 1
            elif 'stackoverflow' in parsed_url.netloc.lower():
                stack_overflow += 1
            else:
                everything_else += 1

print("Number of Queries : ", str(queries))
print("GitHub URLs : ", str(github))
print("StackOverflow URLs : ", str(stack_overflow))
print("Other URLs : ", str(everything_else))
