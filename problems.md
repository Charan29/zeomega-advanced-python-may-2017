#### Problem 1

There is a list of tuples each of which can have a size ranging from 1..100 
(not fixed size). 

   E.g: [(4,10,1), (8,9), (20, 10, 11, 15), (1, 8, 6, 5, 50, 9, 10), (3,),(10, 12, 14, 100, 1, 5)]

Write a program containing two functions to return an iterator containing the 
maximum and the minimum of each tuple in the list. The first function should 
use variable arguments (*args) and the second function should use generators 
(yield).

In the above case the output should be an iterator which will return the following list.

    [(10, 1), (9, 8), (20, 10), (50, 1), (3, 3), (100, 1)]

#### Problem 2

Write a function which takes two lists (sequences) of equal size as arguments, 
merges them using itertools izip and sorts them using a given key.


   E.g: l1 = [20, 1, 8, 10, 5, 15]
        l2 = [55, 8, 29, 13, 10, 11]

Your function should be written as follows.

   def zip_sort(l1, l2, key=0):
       # zip them, sort using key 0
       ...


When called like below,

   zip_sort(l1, l2),

answer would be,

   [(1, 8), (5, 10), (8, 29), (10, 13), (15, 11), (20, 55)]

And when called like,

   zip_sort(l1, l2, key=1)

answer would be

   [(8, 1), (10, 5), (11, 15), (13, 10), (29, 8), (55, 20)]

NOTE: You should try to write a generator instead of returning a list.


#### Problem 3

There is a class as follows which describes a movie show.

    class MovieShow(object):

        def __init__(self, movie_name, cinema_name):
           self.movie_name = movie_name
           self.cinema_name = cinema_name
           self.attendees = []

    
1. You and 3 of your friends decide to attend movie, "Bahubali 2" at PVR
cinemas for 830 pm show. 
2. Write a property that returns number of attendees for a given show.
3. Write a property which indicates the show times of the movie in a day. 
For example if the movie is shown at 9.00 am, 12.00 am, 2pm, 4pm it should indicate
all these times.
4. Add an attribute indicating the movie genre (action, romance, thriller etc)
and make it a property.
5. Add a class level attribute which will give the number of times the movie
was shown in a day. 
6. Write a method - when called will return the next available show time for the movie.
E.g: Called at 12.30 pm, will return 2pm as answer.

#### Problem 4

There are three lists as follows.

    l1 = [9, 10, 1, 8, 15, 23, 40, 5]
    l2 = [10, 4, 6, 34, 9, 31, 17, 8]

l1 and l2 are of same size and l3 is always of a larger size.

    l3 = [18, 57, 41, 25, 27, 39, 100, 2, 9, 36, 13]

Write a program which returns a 2-element tuple of elements in l1 and l2
which when added together will return an element in l3.

For example when the program is run in above inputs the answer would be,

    [(1, 17), (23, 34), (10, 31), (8, 17), (23, 4), (8, 31), None, None, (1, 8), (5, 31), (9, 4)]

If an element cannot be obtained using summing, that place should be filled 
with a "None".

Write the program to work under O(n) or O(n.log(n)). O(n*n) solutions are 
not acceptable.

### Submission

1. For each problem's solution -> Create a Ubuntu pastebin entry.
Make sure you choose "Python" as the Syntax when creating it.
2. Copy the URL.
3. Like that create four ubuntu paste URLs for the four problems above.
4. Go to http://bit.ly/2qtqWJB
5. Enter your Name, Email address.
6. Copy the 4 URLs into the 4 text boxes that says "URL for solution"
