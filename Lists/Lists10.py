"""
Write a program in python to print the file contents with line number using file.
"""

with open("test.txt", "w") as file:
    file.write("Come in through the magic door\nCome and meet Doraemon\nHe has all the future gadgets\nin his 4-D pocket\nHe saves Nobita all the time\nDay and night he works and plays\nHis favourite food are dorayakis\nand he’s afraid of rats\nWhat a very kind guy\nof red blue and white\nAh… There’s a rat!\nYeah… Yeah… Yeah….\nDoraemon and i will head to…\nA very bright future…")
with open("test.txt", "r") as file:
    i = 1
    for line in file:
        print("Line",i,": ",line)
        i+=1
        
"""
Output:
Line 1 :  Come in through the magic door

Line 2 :  Come and meet Doraemon

Line 3 :  He has all the future gadgets

Line 4 :  in his 4-D pocket

Line 5 :  He saves Nobita all the time

Line 6 :  Day and night he works and plays

Line 7 :  His favourite food are dorayakis

Line 8 :  and he’s afraid of rats

Line 9 :  What a very kind guy

Line 10 :  of red blue and white

Line 11 :  Ah… There’s a rat!

Line 12 :  Yeah… Yeah… Yeah….

Line 13 :  Doraemon and i will head to…

Line 14 :  A very bright future…
"""
