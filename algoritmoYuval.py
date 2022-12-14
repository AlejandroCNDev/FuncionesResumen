import hashlib
import numpy as np
import random
import string
import time
import zlib


class algoritmoYuval:

    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    # Here, we'll initialize some of the data.
    def __init__(self, algorithm, bits):
        # Let's add some data to the [instance of the] class.
        self.algorithmHash = algorithm
        self.bits = bits

    def generateHash(self, algorithm, bytesMessage, numBits):
        # we import hashlib (to apply SHA,MD5,...) and zlib to use crc32

        # md5 = haslib.md5(b'Hola mundo')
        # print(md5.hexdigest())

        if algorithm == "crc32":
            generatedHash = zlib.crc32(bytesMessage)
            # generatedHash = generatedHash[:int(numBits / 4)]
        elif algorithm == "md5":
            generatedHash = hashlib.md5(bytesMessage).hexdigest()
            generatedHash = generatedHash[:int(numBits / 4)]
        elif algorithm == "sha":
            generatedHash = hashlib.sha256(bytesMessage).hexdigest()
            generatedHash = generatedHash[:int(numBits / 4)]
        else:
            return -1

        return generatedHash

    #ESTO LO HE HECHO YO PA QUE FUNCIONE PERO NO SE DEBEN HACER ASI LAS MODIFICACIONES
    def generateNewPassword(self, x):
        # The characters to generate password (only ascii_lowercase)
        # characters = list(string.ascii_letters + string.digits + "@!$#&%^()*")

        characters = list(string.ascii_lowercase)
        # The length of the password.
        length_pass = x
        # Shuffling the characters.
        random.shuffle(characters)
        # Picking random characters, from the list.
        randompassword = []
        for i in range(length_pass):
            randompassword.append(random.choice(characters))
        # Shuffling the result
        random.shuffle(randompassword)
        # Converting the list to string
        newpassword = "".join(randompassword)
        # Returning the random password.
        return newpassword

    # Modificaciones menores del mensaje ilegitimo
    def modificacionMenorMi(self):

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
        mil16 = ["Goodbye. ", "Bye."]

        combinations_mi = np.array(
            np.meshgrid(mil1, mil2, mil3, mil4, mil5, mil6, mil7, mil8, mil9, mil10, mil11, mil12, mil13, mil14, mil15,
                        mil16)).T.reshape(-1, 16)

        return combinations_mi

    # Modificaciones menores del mensaje legitimo
    def modificacionMenoresMl(self):

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

        combinations_ml = np.array(
            np.meshgrid(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15,
                        ml16)).T.reshape(-1, 16)

        return combinations_ml

    def algoritmoYuval(self):

        # Para calcular el tiempo de ejecuci??n
        ini_time = time.time()
        # 1: Se generan  t = 2^(m/2) modificaciones menores de xl
        combinations_ml = self.modificacionMenoresMl()

        # 2: Computar el resumen y almacenar los pares (x???l, h(x???l))
        table_hash={}
        for i in combinations_ml:
            str_ml = "".join(i)
            bytes_ml = bytes(str_ml, encoding='utf-8')
            h = self.generateHash(self.algorithmHash, bytes_ml, self.bits)
            table_hash[h] = "".join(i)

        nocollision = True
        # 3: While no se encuentre colisi??n do {probable en t intentos}
        while nocollision:
            # 4: Generar x???i modificaci??n menor de xi y computar h(x???i)
            x = self.modificacionMenorMi()
            for i in x:
                str_mi = "".join(i)
                bytes_mi = bytes(str_mi + self.generateNewPassword(100), encoding='utf-8')
                h1 = self.generateHash(self.algorithmHash, bytes_mi, self.bits)

                # 5: Buscar si existe x???l tal que h(x???l) = h(x???i)
                if h1 in table_hash:
                    print("Existi?? una colision: \n" + "El mensaje es: " + str(bytes_mi))
                    print("Su hash es: " + str(h1))
                    nocollision = False
                    print("El mensaje legitimo con el mismo hash que el ilegitimo es: \n")
                    print(table_hash.get(h1))
                    print("Y el mensaje ilegitimo es: " + str_mi)

                    fin_time = time.time()
                    print("El t??empo de ejecuci??n del programa " + str(fin_time - ini_time))

                    return nocollision

        print("No se encontr?? colisi??n.")
        fin_time = time.time()
        print("El t??empo de ejecuci??n del programa " + str(fin_time-ini_time))
        return nocollision
