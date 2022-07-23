#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated-sequence.

import math
import logging
logging.basicConfig(filename="q1.log", level=logging.DEBUG, format='%(name)s -%(asctime)s - %(levelname)s - %(message)s')

class Question1:
    """Q = Square root of [(2 * C * D)/H]. this class is use to find value of Q by using formula"""
    logging.info("creating constructor of class which take one argument as comma separated string")
    def __init__(self,D):
        self.D=D
        logging.info("value of D is {}".format(self.D))

    def Comma_separated_Val(self):
        """this function split the single string into 3 different value D's"""
        try:
            D1 = self.D.split(",")
            logging.info("D after spliting is {}".format(D1))
            return D1
        except Exception as e:
            logging.error(e)


    def Sq_rt(self):
        """this function finally calculate the value of Q"""
        try:
            D1 = self.D.split(",")
            C = 50
            H = 30
            l = []
            count=0
            for i in D1:
                Q = str(round(math.sqrt(2 * C * int(i) / H)))
                count=count+1
                logging.info("value-{} of Q is- {}".format(count,Q))
                l.append(Q)
            s=",".join(l)
            logging.info("Final three results Q for three values of D are- {}".format(s))
            return "Final three results Q for three values of D are- {}".format(s)

        except Exception as e:
            logging.error(e)

D=input("Enter three values of D in comma-separated-order-- ")
Q1=Question1(D)
print(Q1.Sq_rt())

