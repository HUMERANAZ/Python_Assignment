#Q3: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
import logging
logging.basicConfig(filename='q3.log',level=logging.DEBUG, format='%(name)s -%(asctime)s - %(levelname)s - %(message)s')

class Question3:
    logging.info("creating constructor for this class")
    def __init__(self,s):
        self.s=s
        logging.info("words in comma separated order are- {}".format(self.s))

    def sort_opt(self):
        try:
            l = self.s.split(',')
            logging.info("list of words is- {}".format(l))
            l.sort()
            logging.info("sorted list of words is- {}".format(l))
            st = ",".join(l)
            logging.info("sorted string of words is- {}".format(st))
            return "alphabetically sorted string of words is-- {}".format(st)
        except Exception as e:
            logging.info(e)

s=input("Enter words in comma separated order-- ")
Q3=Question3(s)
print(Q3.sort_opt())
