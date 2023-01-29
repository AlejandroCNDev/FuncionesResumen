# Author: Alejandro Castro Navarro

# we import hashlib (to apply SHA,MD5,...) and zlib to use crc32
import hashlib
import zlib
import itertools
import numpy as np
import random
import string
import time


class algoritmoYuval:

    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    # Here, we'll initialize some of data.
    def __init__(self, algorithm, bits):
        # Let's add some data to the [instance of the] class.
        self.algorithmHash = algorithm
        self.bits = bits

    def generateHash(self, algorithm, bytesMessage, numBits):

        formatHash = int(int(numBits) / 4)
        # md5 = haslib.md5(b'Hola mundo')
        # print(md5.hexdigest())

        if algorithm == "crc32":
            generatedHash = zlib.crc32(bytesMessage)
            # generatedHash = generatedHash[:int(numBits / 4)]
        elif algorithm == "md5":
            generatedHash = hashlib.md5(bytesMessage).hexdigest()
            generatedHash = generatedHash[:int(int(numBits) / 4)]
        elif algorithm == "sha":
            generatedHash = hashlib.sha256(bytesMessage).hexdigest()
            generatedHash = generatedHash[:int(int(numBits) / 4)]
        else:
            return -1

        return generatedHash

    # Modificaciones menores del mensaje ilegitimo
    def modificacionMenoresMi(self, num_binario):
        """
        mil1 = ["Hello ", "Hi "]
        mil2 = ["hostage,", "victim, "]
        mil3 = ["We know ", "I know "]
        mil4 = ["your exact ubication, ", "where you live, "]
        mil5 = ["if you give us ", "if you offer us  "]
        mil6 = ["100000$, ", "200.000$, "]
        mil7 = ["you can live ", "you will still be alive "]
        mil8 = ["otherwise ", "if not, "]
        mil9 = ["you will die. ", "Dead. "]
        mil10 = ["Do you accept the agreement? ", "Do you accept the deal?"]
        mil11 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
        mil12 = ["and sign the agreement ", "and sign the contract"]
        mil13 = ["and send it to me. ", "and send it to me at this same e-mail."]
        mil14 = ["You have 24 hours to think about it, ", "You have 12 hours to think about it, "]
        mil15 = ["but you know there is no choice. ", "but you know that there will be consequences. "]
        mil16 = ["Actually, ", "Really, "]
        mil17 = ["You have no choice, ", "You have no option, "]
        mil18 = ["either you do it or you do it, ", "give us the money and that's it, "]
        mil19 = ["by the way we are an APT from China. ", "by the way we are an APT from Russia. "]
        mil20 = ["Goodbye. ", "Bye."]
        """
        """mil1 = ["Hello ", "Hi "]
        mil2 = ["hostage,", "victim, "]
        mil3 = ["We know ", "I know "]
        mil4 = ["your exact ubication, ", "where you live, "]
        mil5 = ["if you give us ", "if you offer us  "]
        mil6 = ["100000$, ", "200.000$, "]
        mil7 = ["you can live ", "you will still be alive "]
        mil8 = ["otherwise ", "if not, "]
        mil9 = ["you will die. ", "Dead. "]
        mil10 = ["Do you accept the agreement? ", "Do you accept the deal?"]
        mil11 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
        mil12 = ["and sign the agreement ", "and sign the contract"]
        mil13 = ["and send it to me. ", "and send it to me at this same e-mail."]
        mil14 = ["You have 24 hours to think about it, ", "You have 12 hours to think about it, "]
        mil15 = ["but you know there is no choice. ", "but you know that there will be consequences. "]
        mil16 = ["Actually, ", "Really, "]
        mil17 = ["You have no choice, ", "You have no option, "]
        mil18 = ["either you do it or you do it, ", "give us the money and that's it, "]
        mil19 = ["by the way we are an APT from China. ", "by the way we are an APT from Russia. "]
        mil20 = ["We are proffesional  ", "We are specialized "]
        mil21 = ["cyber criminals, ", "cyber-criminals, "]
        mil22 = ["hired by the state ", "hired our the state "]
        mil23 = ["and we are dedicated ", "and we are focused "]
        mil24 = ["to do evil ", "to do harm "]
        mil25 = ["and a lot of damage ", "and a lot of pain "]
        mil26 = ["to everyone ", "to everyone and all over the world "]
        mil27 = ["except our beloved country, ", "except our beloved state, "]
        mil28 = ["and that someday will be the world power, ", "and that someday will be the world power and leader, "]
        mil29 = ["thanks to our help. ", "thanks to our efforts. "]
        mil30 = ["Goodbye. ", "Bye."]

        combinations_mi = itertools.product(mil1, mil2, mil3, mil4, mil5, mil6, mil7, mil8, mil9, mil10, mil11, mil12,
                                         mil13, mil14, mil15, mil16, mil17, mil18, mil19, mil20, mil21, mil22, mil23,
                                         mil24, mil25, mil26, mil27, mil28, mil29, mil30)

        """
        mil1 = ["Hello ", "Hi "]
        mil2 = ["hostage,", "victim, "]
        mil3 = ["We know ", "I know "]
        mil4 = ["your exact ubication, ", "where you live, "]
        mil5 = ["if you give us ", "if you offer us  "]
        mil6 = ["100000$, ", "200.000$, "]
        mil7 = ["you can live ", "you will still be alive "]
        mil8 = ["otherwise ", "if not, "]
        mil9 = ["you will die. ", "Dead. "]
        mil10 = ["Do you accept the agreement? ", "Do you accept the deal?"]
        mil11 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
        mil12 = ["and sign the agreement ", "and sign the contract"]
        mil13 = ["and send it to me. ", "and send it to me at this same e-mail."]
        mil14 = ["You have 24 hours to think about it, ", "You have 12 hours to think about it, "]
        mil15 = ["but you know there is no choice. ", "but you know that there will be consequences. "]
        mil16 = ["Actually, ", "Really, "]
        mil17 = ["You have no choice, ", "You have no option, "]
        mil18 = ["either you do it or you do it, ", "give us the money and that's it, "]
        mil19 = ["by the way we are an APT from China. ", "by the way we are an APT from Russia. "]
        mil20 = ["We are proffesional  ", "We are specialized "]
        mil21 = ["cyber criminals, ", "cyber-criminals, "]
        mil22 = ["hired by the state ", "hired our the state "]
        mil23 = ["and we are dedicated ", "and we are focused "]
        mil24 = ["to do evil ", "to do harm "]
        mil25 = ["and a lot of damage ", "and a lot of pain "]
        mil26 = ["to everyone ", "to everyone and all over the world "]
        mil27 = ["except our beloved country, ", "except our beloved state, "]
        mil28 = ["and that someday will be the world power, ", "and that someday will be the world power and leader, "]
        mil29 = ["thanks to our help. ", "thanks to our efforts. "]
        mil30 = ["Goodbye. ", "Bye."]


        modificacionMenor_mi = mil1[int(num_binario[0])] + mil2[int(num_binario[1])] + mil3[int(num_binario[2])] + \
                               mil4[int(num_binario[3])] + mil5[int(num_binario[4])] + mil6[int(num_binario[5])] + \
                               mil7[int(num_binario[6])] + mil8[int(num_binario[7])] + mil9[int(num_binario[8])] + \
                               mil10[int(num_binario[9])] + mil11[int(num_binario[10])] + mil12[int(num_binario[11])] + \
                               mil13[int(num_binario[12])] + mil14[int(num_binario[13])] + mil15[int(num_binario[14])] + \
                               mil16[int(num_binario[15])] + mil17[int(num_binario[16])] + mil18[int(num_binario[17])] + \
                               mil19[int(num_binario[18])] + mil20[int(num_binario[19])] + mil21[int(num_binario[20])]+ \
                               mil22[int(num_binario[21])] + mil23[int(num_binario[22])] + mil24[int(num_binario[23])] + \
                               mil25[int(num_binario[24])] + mil26[int(num_binario[25])] + mil27[int(num_binario[26])] + \
                               mil28[int(num_binario[27])] + mil29[int(num_binario[28])] + mil30[int(num_binario[29])]


        return modificacionMenor_mi

    # Modificaciones menores del mensaje legitimo
    def modificacionMenoresMl(self, m_2):

        if m_2 ==14:

            ml1 = ["Hello, ", "Good Morning, "]
            ml2 = ["It is my pleasure to contact you today to inform you of the opportunity we have for you. ",
                   "It is a privilege to contact you to let you know about the incredible opportunity we have for you. "]
            ml3 = ["You´ve proven to be a reliable person for us, ",
                   "You´ve reaffirmed that you are a person we can trust, "]
            ml4 = ["and I know that you will be able to help us make this innovative project a success. ",
                   "and I know that you will be able to make our future project a success. "]
            ml5 = ["I am writing to you ", "I am sending you this email  "]
            ml6 = ["because I have recently become aware of your experience and expertise. ",
                   "because I have just recently become aware of your experience, skills and knowledge. "]
            ml7 = ["If they are correct, ", "If they´re true, "]
            ml8 = ["I would like to offer you ", "I would like to propose you "]
            ml9 = ["the job in our company. ", "the possibility of a job in the company. "]
            ml10 = ["Our current salary range ", "Our actual salary range "]
            ml11 = ["for this type of position is $100,000/year. ", "for this type of role is $500,000/year. "]
            ml12 = ["Do you accept the agreement? ", "Do you accept the deal? "]
            ml13 = ["Please let me know as soon as possible, and sign the agreement",
                    "If so, please let me know as soon as possible, and sign the contract"]
            ml14 = ["and send it to me. Regards. Sir. Smith ",
                    "and send it to me at this same e-mail. Best Regards. Sir. John "]

            combinations_ml = list(
                itertools.product(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14))

        elif m_2 == 16:

            ml1 = ["Hello, ", "Good Morning, "]
            ml2 = ["It´s my pleasure to contact you today to inform you of the opportunity we have for you. ",
                   "It´s a privilege to contact you to let you know about the incredible opportunity we have for you. "]
            ml3 = ["You´ve proven to be a reliable person for us, ",
                   "You´ve reaffirmed that you are a person we can trust, "]
            ml4 = ["and I know that you will be able to help us make this innovative project a success. ",
                   "and I know that you will be able to make our future project a success. "]
            ml5 = ["I´m writing to you ", "I am sending you this email  "]
            ml6 = ["because I´ve recently become aware of your experience and expertise. ",
                   "because I´ve just recently become aware of your experience, skills and knowledge. "]
            ml7 = ["If they´re correct, ", "If they´re true,  "]
            ml8 = ["I would like to offer you ", "I would like to propose you "]
            ml9 = ["the job in our company. ", "the possibility of a job in the company. "]
            ml10 = ["Our current salary range ", "Our actual salary range "]
            ml11 = ["for this type of position is $100,000/year. ", "for this type of role is $500,000/year. "]
            ml12 = ["Do you accept the agreement? ", "Do you accept the deal?"]
            ml13 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
            ml14 = ["and sign the agreement ", "and sign the contract"]
            ml15 = ["and send it to me. ", "and send it to me at this same e-mail."]
            ml16 = ["Regards. ", "Best Regards. "]
            """
            ml1 = ["Hello, ", "Good Morning, "]
            ml2 = ["It is my pleasure to contact you today to inform you of the opportunity we have for you. ",
                   "It is a privilege to contact you to let you know about the incredible opportunity we have for you. "]
            ml3 = ["You have proven to be a reliable person for us, ",
                   "You have reaffirmed that you are a person we can trust, "]
            ml4 = ["and I know that you will be able to help us make this innovative project a success. ",
                   "and I know that you will be able to make our future project a success. "]
            ml5 = ["I am writing to you ", "I am sending you this email  "]
            ml6 = ["because I have recently become aware of your experience and expertise. ",
                   "because I have just recently become aware of your experience, skills and knowledge. "]
            ml7 = ["If they are correct, ", "If they are true,  "]
            ml8 = ["I would like to offer you ", "I would like to propose you "]
            ml9 = ["the job in our company. ", "the possibility of a job in our company. "]
            ml10 = ["Our current salary range ", "Our actual salary range "]
            ml11 = ["for this type of position is $100,000/year. ", "for this type of role is $200,000/year. "]
            ml12 = ["Do you accept the agreement? ", "Do you accept the deal?"]
            ml13 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
            ml14 = ["and sign the agreement ", "and sign the contract"]
            ml15 = ["and send it to me. ", "and send it to me at this same e-mail."]
            ml16 = ["Regards.", "Best Regards."]
            """
            combinations_ml = list(
                itertools.product(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15, ml16))

        elif m_2 == 18:
            ml1 = ["Hello, ", "Good Morning, "]
            ml2 = ["It´s my pleasure to contact you today to inform you of the opportunity we have for you. ",
                   "It´s a privilege to contact you to let you know about the incredible opportunity we have for you. "]
            ml3 = ["You´ve proven to be a reliable person for us, ",
                   "You´ve reaffirmed that you are a person we can trust, "]
            ml4 = ["and I know that you´ll be able to help us make this innovative project a success. ",
                   "and I know that you´ll be able to make our future project a success. "]
            ml5 = ["I´m writing to you ", "I am sending you this email  "]
            ml6 = ["because I´ve recently become aware of your experience and expertise. ",
                   "because I´ve just recently become aware of your experience, skills and knowledge. "]
            ml7 = ["If they´re correct, ", "If they´re true,  "]
            ml8 = ["I would like to offer you ", "I would like to propose you "]
            ml9 = ["the job in our company. ", "the possibility of a job in our company. "]
            ml10 = ["Our current salary range ", "Our actual salary range "]
            ml11 = ["for this type of position is $300,000/year. ", "for this type of role is $250,000/year. "]
            ml12 = ["Do you accept the agreement? ", "Do you accept the deal? "]
            ml13 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
            ml14 = ["and sign the agreement ", "and sign the contract"]
            ml15 = ["and send it to me. ", "and send it to me at this same e-mail."]
            ml16 = ["Actually, ", "Really, "]
            ml17 = ["You´ve the ultimate decision, ", "You´ve the final decision, "]
            ml18 = ["Kind Regards.", "Best Regards."]

            combinations_ml = list(
                itertools.product(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15, ml16,
                                  ml17, ml18))

        elif m_2 == 20:
            ml1 = ["Hello, ", "Good Morning, "]
            ml2 = ["It´s my pleasure to contact you today to inform you of the opportunity we have for you. ",
                   "It´s a privilege to contact you to let you know about the incredible opportunity we have for you. "]
            ml3 = ["You´ve proven to be a reliable person for us, ",
                   "You´ve reaffirmed that you are a person we can trust, "]
            ml4 = ["and I know that you will be able to help us make this innovative project a success. ",
                   "and I know that you will be able to make our future project a success. "]
            ml5 = ["I´m writing to you ", "I´m sending you this email  "]
            ml6 = ["because I have recently become aware of your experience and expertise. ",
                   "because I have just recently become aware of your experience, skills and knowledge. "]
            ml7 = ["If they´re correct, ", "If they´re true,  "]
            ml8 = ["I would like to offer you ", "I would like to propose you "]
            ml9 = ["the job in our company. ", "the possibility of a job in our company. "]
            ml10 = ["Our current salary range ", "Our actual salary range "]
            ml11 = ["for this type of position is $200,000/year. ", "for this type of role is $230,000/year. "]
            ml12 = ["Do you accept the agreement? ", "Do you accept the deal?"]
            ml13 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
            ml14 = ["and sign the agreement ", "and sign the contract"]
            ml15 = ["and send it to me. ", "and send it to me at this same e-mail."]
            ml16 = ["Actually, ", "Really, "]
            ml17 = ["You´ve the ultimate decision, ", "You´ve the final decision, "]
            ml18 = ["you´ll not regret it if you choose us as your company, ",
                    "you´ll not regret it if you choose us, "]
            ml19 = ["by the way we are an Valencia (Spain).", "by the way we are an Warsaw (Poland)."]
            ml20 = ["Kind Regards.", "Best Regards."]

            combinations_ml = list(
                itertools.product(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15, ml16,
                                  ml17, ml18, ml19, ml20))
        elif m_2 == 22:


            ml1 = ["Hello, ", "Good Morning, "]
            ml2 = ["I hope you are well. ", "Hope you are well. "]
            ml3 = ["My name is John ", "My name is Tom "]
            ml4 = ["and I am reaching out to you on behalf of S2Grupo.  ",
                   "and I am reaching out to you on behalf of HP. "]
            ml5 = ["We are currently looking to hire ", "We are currently looking to recruit "]
            ml6 = ["someone ", "a worker  "]
            ml7 = ["for the role of Cibersecurity Engineer ", "for the role of Blockchain Engineer "]
            ml8 = ["and after reviewing your resume and experience, ", "and after reviewing your Linkedin, "]
            ml9 = ["we believe that you would be a great fit for this position. ",
                   "we believe that you would be a great fit for this job. "]
            ml10 = ["At Company, we pride ourselves on our dynamic ",
                    "At Company, we pride ourselves on our productive "]
            ml11 = ["and collaborative work environment. ", "and cooperative work environment. "]
            ml12 = [
                "Therefore, It is my pleasure to contact you today to inform you of the opportunity we have for you. ",
                "This is why It is a privilege to contact you to let you know about the incredible opportunity we have for you. "]
            ml13 = ["You have proven to be a reliable person for us, ",
                    "You have reaffirmed that you are a person we can trust, "]
            ml14 = ["and I know that you will be able to help us make this innovative project a success. ",
                    "and I know that you will be able to make our future project a success. "]
            ml15 = ["I am writing to you ", "I am sending you this email  "]
            ml16 = ["because I have recently become aware of your experience and expertise. ",
                    "because I have just recently become aware of your experience, skills and knowledge. "]
            ml17 = ["If they are correct, ", "If they are true,  "]
            ml18 = ["I would like to offer you ", "I would like to propose you "]
            ml19 = ["the job in our company. ", "the possibility of a job in our company. "]
            ml20 = ["Our current salary range ", "Our actual salary range "]
            ml21 = ["for this type of position is $100,000/year. Do you accept the agreement? ",
                    "for this type of role is $200,000/year. Do you accept the deal? "]
            ml22 = ["Regards. Sir. Smith", "Best Regards. Sir. John"]

            combinations_ml = list(
                itertools.product(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15, ml16,
                                  ml17, ml18, ml19, ml20, ml21, ml22))
        elif m_2 == 24:

            ml1 = ["Hello, ", "Good Morning, "]
            ml2 = ["I hope you are well. ", "Hope you are well. "]
            ml3 = ["My name is John ", "My name is Tom "]
            ml4 = ["and I am reaching out to you on behalf of S2Grupo.  ",
                   "and I am reaching out to you on behalf of HP. "]
            ml5 = ["We are currently looking to hire ", "We are currently looking to recruit "]
            ml6 = ["someone ", "a worker  "]
            ml7 = ["for the role of Cibersecurity Engineer ", "for the role of Blockchain Engineer "]
            ml8 = ["and after reviewing your resume and experience, ", "and after reviewing your Linkedin, "]
            ml9 = ["we believe that you would be a great fit for this position. ",
                   "we believe that you would be a great fit for this job. "]
            ml10 = ["At Company, we pride ourselves on our dynamic ",
                    "At Company, we pride ourselves on our productive "]
            ml11 = ["and collaborative work environment. ", "and cooperative work environment. "]
            ml12 = [
                "Therefore, It is my pleasure to contact you today to inform you of the opportunity we have for you. ",
                "This is why It is a privilege to contact you to let you know about the incredible opportunity we have for you. "]
            ml13 = ["You have proven to be a reliable person for us, ",
                    "You have reaffirmed that you are a person we can trust, "]
            ml14 = ["and I know that you will be able to help us make this innovative project a success. ",
                    "and I know that you will be able to make our future project a success. "]
            ml15 = ["I am writing to you ", "I am sending you this email  "]
            ml16 = ["because I have recently become aware of your experience and expertise. ",
                    "because I have just recently become aware of your experience, skills and knowledge. "]
            ml17 = ["If they are correct, ", "If they are true,  "]
            ml18 = ["I would like to offer you ", "I would like to propose you "]
            ml19 = ["the job in our company. ", "the possibility of a job in our company. "]
            ml20 = ["Our current salary range ", "Our actual salary range "]
            ml21 = ["for this type of position is $100,000/year. ", "for this type of role is $200,000/year. "]
            ml22 = ["Do you accept the agreement? ", "Do you accept the deal?"]
            ml23 = ["Please let me know as soon as possible, and sign the agreement and send it to me.",
                    "If so, please let me know as soon as possible, and sign the contract and send it to me at this same e-mail."]
            ml24 = ["Regards.", "Best Regards."]

            combinations_ml = list(
                itertools.product(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15, ml16,
                                  ml17, ml18, ml19, ml20, ml21, ml22, ml23, ml24))

        elif m_2 == 26:

            ml1 = ["Hello, ", "Good Morning, "]
            ml2 = ["I hope you are well. ", "Hope you are well. "]
            ml3 = ["My name is John ", "My name is Tom "]
            ml4 = ["and I am reaching out to you on behalf of S2Grupo.  ",
                   "and I am reaching out to you on behalf of HP. "]
            ml5 = ["We are currently looking to hire ", "We are currently looking to recruit "]
            ml6 = ["someone ", "a worker  "]
            ml7 = ["for the role of Cibersecurity Engineer ", "for the role of Blockchain Engineer "]
            ml8 = ["and after reviewing your resume and experience, ", "and after reviewing your Linkedin, "]
            ml9 = ["we believe that you would be a great fit for this position. ",
                   "we believe that you would be a great fit for this job. "]
            ml10 = ["At Company, we pride ourselves on our dynamic ",
                    "At Company, we pride ourselves on our productive "]
            ml11 = ["and collaborative work environment. ", "and cooperative work environment. "]
            ml12 = [
                "Therefore, It is my pleasure to contact you today to inform you of the opportunity we have for you. ",
                "This is why It is a privilege to contact you to let you know about the incredible opportunity we have for you. "]
            ml13 = ["You have proven to be a reliable person for us, ",
                    "You have reaffirmed that you are a person we can trust, "]
            ml14 = ["and I know that you will be able to help us make this innovative project a success. ",
                    "and I know that you will be able to make our future project a success. "]
            ml15 = ["I am writing to you ", "I am sending you this email  "]
            ml16 = ["because I have recently become aware of your experience and expertise. ",
                    "because I have just recently become aware of your experience, skills and knowledge. "]
            ml17 = ["If they are correct, ", "If they are true,  "]
            ml18 = ["I would like to offer you ", "I would like to propose you "]
            ml19 = ["the job in our company. ", "the possibility of a job in our company. "]
            ml20 = ["Our current salary range ", "Our actual salary range "]
            ml21 = ["for this type of position is $100,000/year. ", "for this type of role is $200,000/year. "]
            ml22 = ["Do you accept the agreement? ", "Do you accept the deal?"]
            ml23 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
            ml24 = ["and sign the agreement and send it to me.",
                    "and sign the contract and send it to me at this same e-mail."]
            ml25 = [" Have a nice day. ", "Have a great day. "]
            ml26 = ["Regards.", "Best Regards."]

            combinations_ml = list(
                itertools.product(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15, ml16,
                                  ml17, ml18, ml19, ml20, ml21, ml22, ml23, ml24, ml25, ml26))

        """
                ml1 = ["Hello, ", "Good Morning, "]
                ml2 = ["I hope you are well. ", "Hope you are well. "]
                ml3 = ["My name is John ", "My name is Tom "]
                ml4 = ["and I am reaching out to you on behalf of S2Grupo.  ", "and I am reaching out to you on behalf of HP. "]
                ml5 = ["We are currently looking to hire ", "We are currently looking to recruit "]
                ml6 = ["someone ", "a worker  "]
                ml7 = ["for the role of Cibersecurity Engineer ", "for the role of Blockchain Engineer "]
                ml8 = ["and after reviewing your resume and experience, ", "and after reviewing your Linkedin, "]
                ml9 = ["we believe that you would be a great fit for this position. ", "we believe that you would be a great fit for this job. "]
                ml10 = ["At Company, we pride ourselves on our dynamic ", "At Company, we pride ourselves on our productive "]
                ml11 = ["and collaborative work environment. ", "and cooperative work environment. "]
                ml12 = ["Therefore, It is my pleasure to contact you today to inform you of the opportunity we have for you. ",
                       "This is why It is a privilege to contact you to let you know about the incredible opportunity we have for you. "]
                ml13 = ["You have proven to be a reliable person for us, ",
                       "You have reaffirmed that you are a person we can trust, "]
                ml14 = ["and I know that you will be able to help us make this innovative project a success. ",
                       "and I know that you will be able to make our future project a success. "]
                ml15 = ["I am writing to you ", "I am sending you this email  "]
                ml16 = ["because I have recently become aware of your experience and expertise. ",
                       "because I have just recently become aware of your experience, skills and knowledge. "]
                ml17 = ["If they are correct, ", "If they are true,  "]
                ml18 = ["I would like to offer you ", "I would like to propose you "]
                ml19 = ["the job in our company. ", "the possibility of a job in our company. "]
                ml20 = ["Our current salary range ", "Our actual salary range "]
                ml21 = ["for this type of position is $100,000/year. ", "for this type of role is $200,000/year. "]
                ml22 = ["Do you accept the agreement? ", "Do you accept the deal?"]
                ml23 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
                ml24 = ["and sign the agreement and send it to me.", "and sign the contract and send it to me at this same e-mail."]
                ml25 = ["Regards.", "Best Regards."]
        """

        """
        ml1 = ["Hello, ", "Good Morning, "]
        ml2 = ["I hope you are well. ", "Hope you are well. "]
        ml3 = ["My name is John ", "My name is Tom "]
        ml4 = ["and I am reaching out to you on behalf of S2Grupo.  ", "and I am reaching out to you on behalf of HP. "]
        ml5 = ["We are currently looking to hire ", "We are currently looking to recruit "]
        ml6 = ["someone ", "a worker  "]
        ml7 = ["for the role of Cibersecurity Engineer ", "for the role of Blockchain Engineer "]
        ml8 = ["and after reviewing your resume and experience, ", "and after reviewing your Linkedin, "]
        ml9 = ["we believe that you would be a great fit for this position. ", "we believe that you would be a great fit for this job. "]
        ml10 = ["At Company, we pride ourselves on our dynamic ", "At Company, we pride ourselves on our productive "]
        ml11 = ["and collaborative work environment. ", "and cooperative work environment. "]
        ml12 = ["Therefore, It is my pleasure to contact you today to inform you of the opportunity we have for you. ",
               "This is why It is a privilege to contact you to let you know about the incredible opportunity we have for you. "]
        ml13 = ["You have proven to be a reliable person for us, ",
               "You have reaffirmed that you are a person we can trust, "]
        ml14 = ["and I know that you will be able to help us make this innovative project a success. ",
               "and I know that you will be able to make our future project a success. "]
        ml15 = ["I am writing to you ", "I am sending you this email  "]
        ml16 = ["because I have recently become aware of your experience and expertise. ",
               "because I have just recently become aware of your experience, skills and knowledge. "]
        ml17 = ["If they are correct, ", "If they are true,  "]
        ml18 = ["I would like to offer you ", "I would like to propose you "]
        ml19 = ["the job in our company. ", "the possibility of a job in our company. "]
        ml20 = ["Our current salary range ", "Our actual salary range "]
        ml21 = ["for this type of position is $100,000/year. ", "for this type of role is $200,000/year. "]
        ml22 = ["Do you accept the agreement? ", "Do you accept the deal?"]
        ml23 = ["Please let me know as soon as possible, ", "If so, please let me know as soon as possible, "]
        ml24 = ["and sign the agreement ", "and sign the contract"]
        m125 = ["and send it to me. ", "and send it to me at this same e-mail."]
        ml26 = ["Actually, ", "Really, "]
        ml27 = ["You have the ultimate decision, ", "You have the final decision, "]
        ml28 = ["you will not regret it if you choose us as your company, ", "you will not regret it if you choose us, "]
        ml29 = ["by the way we are an Valencia (Spain).", "by the way we are an Warsaw (Poland)."]
        ml30 = ["Regards.", "Best Regards."]
        """

        """combinations_ml = np.array(
            np.meshgrid(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15,
                        ml16, ml17, ml18, ml19, ml20)).T.reshape(-1, 20)
        """

        """
        combinations_ml = np.array(
            np.meshgrid(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15,
                        ml16, ml17, ml18, ml19, ml20, ml21, ml22, ml23, ml24, ml25)).T.reshape(-1, 25)
        """

        """
        combinations_ml = np.array(
            np.meshgrid(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15,
                        ml16, ml17, ml18, ml19, ml20, ml21, ml22, ml23, ml24, ml25, ml26, ml27, ml28, ml29, ml30)).T.reshape(-1, 30)
        """
        return combinations_ml

    def algoritmoYuval(self):

        # 1: Se generan  t = 2^(m/2) modificaciones menores de xl
        m_2 = int(int(self.bits) / 2)  # m/2
        t = int(pow(2, m_2))

        combinations_ml = self.modificacionMenoresMl(m_2)

        # 2: Computar el resumen y almacenar los pares (x′l, h(x′l))
        table_hash = {}
        for i in combinations_ml:
            str_ml = "".join(i)
            bytes_ml = bytes(str_ml, encoding='utf-8')
            h = self.generateHash(self.algorithmHash, bytes_ml, self.bits)
            table_hash[h] = "".join(i)

        collision = False
        i = 0

        #combinations_mi = self.modificacionMenoresMi()

        # 3: While no se encuentre colisión do {probable en t intentos}
        while not collision or i<=2**30:
            try:
                # 4: Generar x′i modificación menor de xi y computar h(x′i)
                num_bin = (bin(i)[2:].zfill(30)) # Aqui no se que hacer para que se generen muchos t intentos
                i += 1
                x = self.modificacionMenoresMi(num_bin)

                #comb = next(combinations_mi)  #De esta forma es más eficiente, pero consume más memoria, para atacar funciones con mayor numero de bits
                str_mi = "".join(x)

                bytes_mi = bytes(str_mi, encoding='utf-8')
                h1 = self.generateHash(self.algorithmHash, bytes_mi, self.bits)

                # 5: Buscar si existe x′l tal que h(x′l) = h(x′i)
                if h1 in table_hash:
                    print("Existió una colision (en " + str(i) + "), el hash que coincide es: " + str(h1) + "\n")
                    collision = True
                    print("El mensaje legitimo es: ")
                    print(table_hash.get(h1))
                    print("\nY el mensaje ilegitimo es: \n" + str_mi)

                    return collision

            except StopIteration:
                print("All combinations generated")
                print("Does not exist colision")
                break

        print("No se encontró colisión.")

