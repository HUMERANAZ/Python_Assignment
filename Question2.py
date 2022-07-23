#Q2:Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
#element value in the i-th row and j-th column of the array should be i*j.


import logging
logging.basicConfig(filename='q2.log',level=logging.DEBUG, format='%(name)s -%(asctime)s - %(levelname)s - %(message)s')

class Question2:
    logging.info("creating constructor for this class")
    def __init__(self,s):
        self.s=s
        logging.info("X,Y :- {}".format(s))

    def two_d_array(self):
        try:
            st=s.split(",")
            l = []
            for i in range(int(st[0])):
                l1 = []
                for j in range(int(st[1])):
                    l1.append(i * j)
                l.append(l1)

            logging.info("2-d array:- {}".format(l))
            return "2-d array:- {}".format(l)

        except Exception as e:
            logging.info(e)

s=input("Enter X,Y - ")
Q2=Question2(s)
print(Q2.two_d_array())
