#Q4: Write a program that accepts a sequence of whitespace separated words as input and prints
#the words after removing all duplicate words and sorting them alphanumerically.

import logging
logging.basicConfig(filename='q4.log',level=logging.DEBUG, format='%(name)s -%(asctime)s - %(levelname)s - %(message)s')

class Question4:
    logging.info("creating constructor for this class")

    def __init__(self, s):
        self.s = s
        logging.info("Entered string is :- {}".format(self.s))

    def remove_duplicates(self):
        try:
            l = self.s.split(" ")
            logging.info("list of words is- {}".format(l))
            self.l1 = list(set(l))
            logging.info("list after removing duplicate words is- {}".format(self.l1))
            st = " ".join(self.l1)
            logging.info("string after remove duplicates:- {}".format(st))
            return "string after removing duplicate words is :- {}".format(st)
        except Exception as e:
            logging.error(e)


    def alph_sort(self):
        self.l1.sort()
        logging.info("alphanumeric sorted string :- {}".format(" ".join(self.l1)))
        return "alphanumerically sorted string is:- {}".format(" ".join(self.l1))

s=input("Enter string with whitespaces-- ")
Q=Question4(s)
print(Q.remove_duplicates())
print(Q.alph_sort())