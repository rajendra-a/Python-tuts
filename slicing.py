#   We can access characters from string individually
#   we can use the square brackets after string\
#   Location called an index, index starts from 0 and last index can be represent with -1

message = 'Hello World'
print(message[0])
print(message[5])
print(message[0:5]) # not including 9th index means 10th character l
print(message[:5]) # we will get the same output as above statement because
# the starting point starts with 0 if not mentioned anything
print(message[6:])
# as like above statement if we didn't mention end index it will assumes like that is last index as -1
# means last letter from string

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
print(my_list[5])
print(my_list[2:8:1])
print(my_list[-9])
print(my_list[:])
print(my_list[2:-1])
print(my_list[2:-1:2])
print(my_list[2:-1:1])
print(my_list[-2:2:-
1])


sample_url = 'http://coreyms.com'
print(sample_url)
# reverse the sample url
print(sample_url[::-1])
# Get the top level domain here .com
print(sample_url[-4:])
# print the url  without http
print(sample_url[7:])
# print the url without top level domain or http
print(sample_url[7:-4])