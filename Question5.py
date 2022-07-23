import logging
logging.basicConfig(filename='q5.log',level=logging.DEBUG, format='%(name)s -%(asctime)s - %(levelname)s - %(message)s')

class Question5:
    logging.info("creating constructor for this class")
    def __init__(self,s):
        self.s=s
        logging.info("entered string is:- {}".format(self.s))

    def count_alph_digi(self):
        try:
            l = 0
            d = 0
            for i in self.s:
                if i.isalpha():
                    l = l + 1
                elif i.isdigit():
                    d = d + 1
                else:
                    continue
            logging.info("LETTERS-{} \n DIGITS-{}".format(l,d))
            return "LETTERS-{} \n DIGITS-{}".format(l,d)

        except Exception as e:
            logging.info(e)

s=input("Enter string - ")
Q5=Question5(s)
print(Q5.count_alph_digi())

