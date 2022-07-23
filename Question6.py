import logging
logging.basicConfig(filename='q6.log',level=logging.DEBUG, format='%(name)s -%(asctime)s - %(levelname)s - %(message)s')

class Question6:
    logging.info("creating constructor for this class")
    def __init__(self,s):
        self.s=s
        self.sc="$#@"
        logging.info("entered passwords are {}".format(self.s))

    def password_check(self):
        try:
            pw = self.s.split(',')
            logging.info("list of entered passwords is- {}".format(pw))
            for p in pw:
                logging.info("checking lenghth of - {}".format(p))
                if len(p) >= 6 and len(p) <= 12:
                    logging.info("checking validation for - {}".format(p))
                    uc, lc, sc, d = 0, 0, 0, 0
                    for i in p:
                        if i.isupper():
                            uc = uc + 1
                        elif i.islower():
                            lc = lc + 1
                        elif i in self.sc:
                            sc = sc + 1
                        elif i.isdigit():
                            d = d + 1

                        else:
                            break
                    if uc >= 1 and lc >= 1 and sc >= 1 and d >= 1:
                        logging.info("uppercase-{} , lowercase-{}, specialcharacter-{}, digits-{}".format(uc,lc,sc,d))
                        logging.info("{} is valid password".format(p))
                        return "{} is valid password".format(p)
                else:
                    logging.info("{} is invalid password".format(p))
        except Exception as e:
            logging.info(e)

s=input("Enter passwords- ")
Q6=Question6(s)
print(Q6.password_check())

