import sys

A = {'4D Adventure': 120, 'Aqua Bike': 55, 'BlackHole Coaster': 140, 'Giant House': 89, 'Grandcar': 70,
     'Heart wheel': 85, 'Horror Tower': 110, 'Hurricane': 160, 'Kart Rider': 100,
     'Pegasus': 80, 'Spaceship': 60, 'Raptor': 115, 'Sky Cab': 90, 'Sky Coaster': 180,
     'Snow Town': 200, 'Super Splash': 130, 'Tornado': 170, 'Vikings': 150,
     'Water Fun': 125}


class Node:
    def __init__(self, data=None): # ฟังก์ชันสำหรับประกาศตัวแปรที่เรียกใช้ภายใน class
        self.data = data
        # ส่วน linked list
        self.next = None
        # ส่วน Bst
        self.left = None
        self.right = None


class InforList:
    def __init__(self): # ฟังก์ชันสำหรับประกาศตัวแปรที่เรียกใช้ภายใน class
        self.first = Node("Infor")
        self.name = None

    def append(self, data): # ฟังก์ชันสำหรับเพิ่มข้อมูลโดยเรียกใช้ฟังก์ชันนี้ก่อนจะส่งต่อไปยังฟังก์ชัน appendList
        self.appendList(data, self.first)

    def appendList(self, data, slist): # ฟังก์ชันสำหรับรับข้อมูลจากฟังก์ชัน append มาเพิ่มเก็บไว้ในโนด
        data = str(data)
        if slist.next is None: # ถ้าโนดว่างก็ให้เพิ่มข้อมูลลงในโนดได้เลย
            slist.next = Node(data)
        else: # ถ้าโนดไม่ว่างให้เพิ่มข้อมูลลงโนดถัดไป
            self.appendList(data, slist.next)

    def searchage(self, data, slist): # ฟังก์ชันสำหรับค้นหาข้อมูลประเภทอายุในโนด
        if slist is None: # ถ้าไม่มีข้อมูลที่ค้นหาให้แสดงทางหน้าจอว่า Not Found
            return "Not Found "+str(data)
        elif slist.data == data: # ถ้าเจอข้อมูลตรงกับที่ค้นหาแล้วให้ return ข้อมูลเป็น int ออกไปเพื่อนำไปใช้คิดค่าเข้าสวนสนุก
            return int(slist.next.data)
        else: # ถ้ายังไม่เจอให้ลองค้นหาโนดต่อๆไป
            return self.searchage(data, slist.next)

    def searchcard(self, data, slist): # ฟังก์ชันสำหรับค้นหาข้อมูลประเภทของการ์ดในโนด
        if slist is None: # ถ้าไม่มีข้อมูลที่ค้นหาให้แสดงทางหน้าจอว่า Not Found
            return "Not Found "+str(data)
        elif slist.data == data: # ถ้าเจอข้อมูลตรงกับที่ค้นหาแล้วให้ return ข้อมูลออกไปเพื่อนำไปใช้คิดในส่วนของการเสียค่าเครื่องเล่น
            return slist.next.next.data
        else: # ถ้ายังไม่เจอให้ลองค้นหาโนดต่อๆไป
            return self.searchcard(data, slist.next)

    def inforname(self):  # เพิ่มชื่อลูกค้า
        self.name = input("Name:")
        if self.name.isalpha(): # ถ้าข้อมูลที่ input เข้ามาเป็น string ทั้งหมดให้เพิ่มข้อมูลลงไปและเรียกใช้ฟังก์ชันเพิ่มข้อมูลประเภทอายุต่อ
            self.append(self.name)
            self.inforage()
        else: # ถ้าข้อมูลที่ input เข้ามาไม่ได้เป็น string จะเรียกใช้ฟังก์ชันเพิ่มชื่อเพื่อให้ใส่ข้อมูลอีกครั้ง
            print("Please enter letters only")
            self.inforname()

    def inforage(self):  # เพิ่มอายุลูกค้า
        age = input("Age:")
        try: # ถ้าข้อมูลที่ใส่มาเป็น int ก็สามารถเพิ่มข้อมูลลงไปในโนดได้เลย
            age = int(age)
            self.append(age)
        except: # ถ้าข้อมูลที่ใส่มาไม่เป็น int จะเรียกใช้ฟังก์ชันเพิ่มอายุเพื่อให้ใส่ข้อมูลอีกครั้ง
            print("Please enter a number")
            self.inforage()

    def inforcard(self):  # รับชนิดบัตร
        card = input("Type card: ")
        if card == "N" or card == "B" or card == "S" or card == "G" or card == "P": # ถ้าใส่ข้อมูลตามที่กำหนดก็สามารถเพิ่มข้อมูลลงไปในโนด
            self.append(card)
        else: # ถ้าใส่ข้อมูลไม่ตรงตามที่กำหนดจะต้องกรอกข้อมูลอีกครั้ง
            print('%s is not a valid choice' % card)
            self.inforcard()


class Binarytree:
    def __init__(self, rootdata): # ฟังก์ชันสำหรับประกาศตัวแปรที่เรียกใช้ภายใน class
        self.root = Node(rootdata)
        self.heart = Heartland()

    def insert(self, data): # ฟังก์ชันเพิ่มข้อมูล
        if not self.search(self.root, data): # ถ้าเรียกใช้ฟังก์ชัน search แล้วไม่เจอ
            try:
                data = int(data) # กำหนดข้อมูลที่ได้มาให้เป็น int
                self.root = self.insert_Btree(self.root, data) # เพิ่มข้อมูลไปใน Btree
            except ValueError:
                print("Not integer")

    def insert_Btree(self, ptr, data): # ฟังก์ชันค้นหาภายใน Btree เพื่อทำการเพิ่มข้อมูล
        if ptr is None: # ถ้าเจอตำแหน่งที่โนดว่างให้เพิ่มข้อมูล
            ptr = Node(data)
        elif data < ptr.data: # ถ้าไม่เจอและ data < ptr.data ให้ค้นหาต่อไปทางซ้าย
            ptr.left = self.insert_Btree(ptr.left, data)
        elif data > ptr.data: # ถ้าไม่เจอและ data > ptr.data ให้ค้นหาต่อไปทางขวา
            ptr.right = self.insert_Btree(ptr.right, data)
        return ptr # return ค่าตำแหน่งออกมา

    def search(self, ptr, data): # ฟังก์ชันค้นหา
        if ptr is None: # ถ้าเจอตำแหน่งที่โนดว่างให้ return False
            return False
        elif ptr.data == data: # ถ้าเจอข้อมูลที่ตรงกันให้ return True
            return True
        elif data < ptr.data: # ถ้า data < ptr.data ให้ค้นหาต่อไปทางซ้าย
            return self.search(ptr.left, data)
        elif data > ptr.data: # data > ptr.data ให้ค้นหาต่อไปทางขวา
            return self.search(ptr.right, data)
        return False

    def getLevelUtil(self, node, data, level): #ฟังก์ชันการนับระดับโนดของ Btree
        if node is None: # ถ้าโนดว่างให้ return ค่า 0
            return 0
        if node.data == data: # ถ้าโนดของข้อมูลตรงกันให้ return ค่าเลเวล
            return level
        downlevel = self.getLevelUtil(node.left, data, level + 1) # หากไม่เข้าเงื่อนไขด้านบนก็ทำการเรียกใช้ฟังก์ชันซ้ำเพื่อดูโนดถัดไปด้านซ้าย
        if downlevel != 0: # ถ้าค่า downlevel ไม่เท่ากับ 0 ก็ return ค่าออกไปได้เลย
            return downlevel
        downlevel = self.getLevelUtil(node.right, data, level + 1) # หากไม่เข้าเงื่อนไขด้านบนก็ทำการเรียกใช้ฟังก์ชันซ้ำเพื่อดูโนดถัดไปด้านขวา
        return downlevel

    def getLevel(self, node, data): # ฟังก์ชันสำหรับรับข้อมูลเพื่อเรียกใช้ฟังก์ชันการนับระดับโนดต่อ
        return self.getLevelUtil(node, data, 1)


class Heartland:
    def __init__(self):  # ฟังก์ชันสำหรับประกาศตัวแปรที่เรียกใช้ภายใน class
        self.income = 0
        self.rootdata = None
        self.btree = None

    def arrayA(self):  # ฟังก์ชันสร้าง array เพื่อเก็บเฉพาะราคาของเครื่องเล่น
        costT = []
        for x in A:
            if A[x] != 0: # ถ้า x ไม่เท่ากับ 0 ให้เพิ่มข้อมูลลงในอะเรย์
                costT.append(A[x])
        return costT

    def insert(self, name, cost):  # ฟังก์ชันเพิ่มเครื่องเล่น/ปรับราคา
        A[name] = cost  # แก้ไขในลิสต์ A
        self.arrayA() # สร้างอะเรย์ใหม่
        self.bst() # สร้าง Btree ใหม่
        return A  # return อะเรย์ A ค่าใหม่

    def delete(self, name):  # ฟังก์ชันลบเครื่องเล่น
        if name in A: # ถ้าชื่อมีอยู่ในอะเรย์
            A[name] = 0  # แก้ไขราคาเครื่องเล่นที่ต้องการลบในลิสต์ A ให้เป็น 0
        else:
            print('"%s" not found' %name)  # กรณีไม่พบชื่อที่ต้องการลบ
        self.arrayA() # สร้างอะเรย์ใหม่
        self.bst() # สร้าง Btree ใหม่
        return A  # return อะเรย์ A ค่าใหม่

    def bst(self): # ฟังก์ชันสำหรับเพิ่มข้อมูลแบบ Btree
        AC = self.arrayA() # กำหนดชื่อตัวแปร AC เพื่อเข้าถึงข้อมูลในอะเรย์
        self.rootdata = AC[0]
        self.btree = Binarytree(self.rootdata)
        for n in AC:
            if n != self.rootdata: # ถ้าข้อมูลไม่อยู่ใน Btree ให้ทำการเพิ่มข้อมูลลงไป
                self.btree.insert(n)
        return self.btree

    def cardLevelB(self): # ฟังก์ชันสำหรับเก็บราคาเครื่องเล่นไม่เกินเลเวล 2
        cardB = []
        self.bst()
        for x in range(1, 1000):
            level = self.btree.getLevel(self.btree.root, x) # ตรวจเลเวลของราคาเครื่องเล่นที่อยู่ใน Btree
            if level:
                if int(self.btree.getLevel(self.btree.root, x)) <= 2: # ถ้าเลเวลไม่เกิน 2 ให้เพิ่มข้อมูลในอะเรย์
                    cardB.append(x)
        return cardB

    def cardLevelBcost(self): # ฟังก์ชันรวมราคาของเครื่องเล่นแบบเหมา
        B = self.cardLevelB() # กำหนดชื่อตัวแปร B เพื่อเข้าถึงราคาเครื่องเล่น
        costCardB = 0
        for n in B: # วนใน B เพื่อนำค่าเครื่องเล่นมาบวกกัน
            costCardB = costCardB + n # คำนวณราคาเหมาทั้งหมดของเครื่องเล่น
        return costCardB  # แสดงราคาบัตร B

    def cardLevelBname(self): # ฟังก์ชันเก็บชื่อเครื่อเล่นในบัตรเลเวลB
        B = self.cardLevelB() # กำหนดชื่อตัวแปร B เพื่อเข้าถึงราคาเครื่องเล่นในส่วนของเลเวล
        cardBname = {} # สร้างเซตว่างเพื่อรอเก็บชื่อเครื่องเล่นในบัตร B
        for n in B: # วนใน B เพื่อนำข้อมูลไปคิดในเงื่อนไขถัดไป
            for j in A: # วนใน A เพื่อนำข้อมูลไปคิดในเงื่อนไขถัดไป
                if A[j] == n: # ถ้าราคาใน A เท่ากับใน B เพิ่มชื่อและราคาลงในเซต cardBname
                    cardBname[j] = n
        return cardBname  # แสดงเครื่องเล่นสำหรับบัตร B

    def cardLevelS(self): # ฟังก์ชันสำหรับเก็บราคาเครื่องเล่นเลเวลเท่ากับ 3
        cardS = []
        self.bst()
        for x in range(1, 1000):
            level = self.btree.getLevel(self.btree.root, x) # ตรวจเลเวลของราคาเครื่องเล่นที่อยู่ใน Btree
            if level:
                if int(level) == 3: # ถ้าเลเวลเท่ากับ 3 ให้เพิ่มข้อมูลในอะเรย์
                    cardS.append(x)
        return cardS

    def cardLevelScost(self): # ฟังก์ชันรวมราคาของเครื่องเล่นแบบเหมา
        S = self.cardLevelS() # กำหนดชื่อตัวแปร S เพื่อเข้าถึงราคาเครื่องเล่น
        costCardS = self.cardLevelBcost()
        for n in S: # วนใน S เพื่อนำค่าเครื่องเล่นมาบวกกัน
            costCardS = costCardS + n # คำนวณราคาเหมาทั้งหมดของเครื่องเล่น
        return costCardS  # แสดงราคาบัตร S

    def cardLevelSname(self): # ฟังก์ชันเก็บชื่อเครื่อเล่นในบัตรเลเวลS
        S = self.cardLevelS() # กำหนดชื่อตัวแปร S เพื่อเข้าถึงราคาเครื่องเล่นในส่วนของเลเวล
        cardSname = {} # สร้างเซตว่างเพื่อรอเก็บชื่อเครื่องเล่นในบัตร S
        for n in S: # วนใน S เพื่อนำข้อมูลไปคิดในเงื่อนไขถัดไป
            for j in A: # วนใน A เพื่อนำข้อมูลไปคิดในเงื่อนไขถัดไป
                if A[j] == n: #ถ้าราคาใน A เท่ากับใน S เพิ่มชื่อและราคาลงในเซต cardSname
                    cardSname[j] = n
        return cardSname  # แสดงเครื่องเล่นสำหรับบัตร S
##################################################################

    def cardLevelG(self): # ฟังก์ชันสำหรับเก็บราคาเครื่องเล่นเลเวล 4
        cardG = []
        self.bst()
        for x in range(1, 1000):
            level = self.btree.getLevel(self.btree.root, x) #ตรวจเลเวลของราคาเครื่องเล่นใน BST
            if level:
                if 3 < int(level) <= 4: # ถ้าเลเวลเท่ากับ4 ให้เพิ่มข้อมูลในอะเรย์
                    cardG.append(x)
        return cardG #แสดงบัตรG

    def cardLevelGcost(self): # ฟังก์ชันรวมราคาของเครื่องเล่นแบบเหมาเลเวล 4
        G = self.cardLevelG() # กำหนดชื่อตัวแปร G เพื่อเข้าถึงราคาเครื่องเล่น
        costCardG = self.cardLevelScost()
        for n in G:  # วนใน B เพื่อนำค่าเครื่องเล่นมาบวกกันและคำนวณราคาเหมาทั้งหมดของเครื่องเล่น
            costCardG = costCardG + n
        return costCardG  # แสดงราคาบัตร G

    def cardLevelGname(self):# ฟังก์ชันเก็บชื่อเครื่อเล่นในบัตรเลเวล G
        G = self.cardLevelG()  # กำหนดชื่อตัวแปร G เพื่อเข้าถึงราคาเครื่องเล่นในส่วนของเลเวล
        cardGname = {}  # สร้างเซตว่างเพื่อรอเก็บชื่อเครื่องเล่นในบัตร G
        for n in G: # วนใน G เพื่อนำข้อมูลไปคิดในเงื่อนไขถัดไป
            for j in A: # วนใน A เพื่อนำข้อมูลไปคิดในเงื่อนไขถัดไป
                if A[j] == n: #ถ้าราคาใน A เท่ากับใน G เพิ่มชื่อและราคาลงในเซต cardGname
                    cardGname[j] = n
        return cardGname  # แสดงเครื่องเล่นสำหรับบัตร G

    def cardLevelP(self): # ฟังก์ชันสำหรับเก็บราคาเครื่องเล่นแบบเหมาเครื่องเล่นทั้งหมด
        cardP = []
        self.bst()
        for x in range(1, 1000):
            level = self.btree.getLevel(self.btree.root, x) #ตรวจเลเวลของราคาเครื่องเล่นใน BST
            if level:
                if int(level) > 4: # ถ้าเลเวล มากกว่า4 ให้เพิ่มข้อมูลในอะเรย์
                    cardP.append(x)
        return cardP   #แสดงบัตร P

    def cardLevelPcost(self): # ฟังก์ชันรวมราคาของเครื่องเล่นแบบเหมาเครื่องเล่นทั้งหมด
        P = self.cardLevelP() # กำหนดชื่อตัวแปร P เพื่อเข้าถึงราคาเครื่องเล่น
        costCardP = self.cardLevelGcost()
        for n in P:  # วนใน P เพื่อนำค่าเครื่องเล่นมาบวกกัน และคำนวณราคาเหมาทั้งหมดของเครื่องเล่น
            costCardP = costCardP + n
        return costCardP  # แสดงราคาบัตร P

    def cardLevelPname(self): # ฟังก์ชันเก็บชื่อเครื่อเล่นในบัตรเลเวล P
        P = self.cardLevelP()  # กำหนดชื่อตัวแปร P เพื่อเข้าถึงราคาเครื่องเล่น
        cardPname = {}  # สร้างเซตว่างเพื่อรอเก็บชื่อเครื่องเล่นในบัตร P
        for n in P:  # วนใน P เพื่อนำข้อมูลไปคิดในเงื่อนไขถัดไป
            for j in A:  # วนใน A เพื่อนำข้อมูลไปคิดในเงื่อนไขถัดไป
                if A[j] == n: #ถ้าราคาใน A เท่ากับใน P เพิ่มชื่อและราคาลงในเซต cardPname
                    cardPname[j] = n
        return cardPname  # แสดงเครื่องเล่นสำหรับบัตร P

    def checkCard(self, nameC, Slist):  # แสดงราคาบัตรที่ต้องจ่ายและเครื่องเล่นที่เล่นฟรี
        costCardB = self.cardLevelBcost()  #ราคาบัตรB
        cardBname = str(self.cardLevelBname()) #แสดงเครื่องเล่นบัตรB
        costCardS = self.cardLevelScost()  #ราคาบัตรS
        cardSname = cardBname+str(self.cardLevelSname())   #แสดงเครื่องเล่นบัตรS
        costCardG = self.cardLevelGcost()  #ราคาบัตรG
        cardGname = cardSname+str(self.cardLevelGname())  #แสดงเครื่องเล่นบัตรG
        costCardP = self.cardLevelPcost()  #ราคาบัตรP
        card = Slist.searchcard(nameC, Slist.first)
        if card == "N": #เงื่อนไขถ้าในการกรอกข้อมูลเลือกบัตรเป็น N
            age = Slist.searchage(nameC, Slist.first)
            if age <= 15: #ถ้าอายุไม่เกิน15 ราคาบัตรเท่ากับ 99 บาท
                self.income = self.income+99
                print("Ticket price 99 baht")
            else: #แต่ถ้าอายุมากกว่า15 เป็นต้นไป ราคราบัตรจะเท่ากับ 149 บาท
                self.income = self.income + 149
                print("Ticket price 149 baht")
        elif card == "B": #เงื่อนไขถ้าในการกรอกข้อมูลเลือกบัตรเป็น B จะแสดงราคาและเครื่องเล่นที่เล่นได้
            self.income = self.income + costCardB
            print("Ticket price %d baht" % costCardB)
            print("Free!! ", cardBname)
        elif card == "S": #เงื่อนไขถ้าในการกรอกข้อมูลเลือกบัตรเป็น S จะแสดงราคาและเครื่องเล่นที่เล่นได้
            self.income = self.income + costCardS
            print("Ticket price %d baht" % costCardS)
            print("Free!! ", cardSname)
        elif card == "G":  #เงื่อนไขถ้าในการกรอกข้อมูลเลือกบัตรเป็น G จะแสดงราคาและเครื่องเล่นที่เล่นได้
            self.income = self.income + costCardG
            print("Ticket price %d baht" % costCardG)
            print("Free!! ", cardGname)
        elif card == "P": #เงื่อนไขถ้าในการกรอกข้อมูลเลือกบัตรเป็น P จะแสดงราคาและเครื่องเล่นที่เล่นได้
            self.income = self.income + costCardP
            print("Ticket price %d baht" % costCardP)
            print("All Free!!")

    def addcost(self, nameC, nameA, Slist):  # แสดงราคาที่ต้องจ่ายเพิ่ม
        card = Slist.searchcard(nameC, Slist.first)
        try:
            cost = A[nameA]
            if card == "B": #กรณีบัตร B
                if cost in self.cardLevelB(): #ถ้าเครื่องเล่นอยู่ใน card B อยู่แล้ว จะไม่มีค่าใช้จ่ายเพิ่มเติม
                    print("No extra charge")
                elif int(cost) == 0: #ถ้าราคาเครื่องเล่น =0 เครื่องเล่นอยู่ระหว่างการปรับปรุง
                    print("under rennovation")
                else:
                    self.income = self.income+cost  #ถ้าเครื่องเล่นไม่ได้อยู่ใน card B จะบวกราคาเครื่องเล่นใหม่เข้าไปแล้วแสดงราคาที่ต้องจ่ายเพิ่ม
                    print("have to pay %d baht" % cost)
            elif card == "S": #กรณีบัตร S
                if cost in self.cardLevelB()+self.cardLevelS(): #ถ้าเครื่องเล่นอยู่ใน card S อยู่แล้ว จะไม่มีค่าใช้จ่ายเพิ่มเติม
                    print("No extra charge")
                elif int(cost) == 0: #ถ้าราคาเครื่องเล่น =0 เครื่องเล่นอยู่ระหว่างการปรับปรุง
                    print("under rennovation")
                else:
                    self.income = self.income + cost  #ถ้าเครื่องเล่นไม่ได้อยู่ใน card S จะบวกราคาเครื่องเล่นใหม่เข้าไปแล้วแสดงราคาที่ต้องจ่ายเพิ่ม
                    print("have to pay %d baht" % cost)
            elif card == "G": #กรณีบัตร G
                if cost in self.cardLevelB()+self.cardLevelS()+self.cardLevelG():  #ถ้าเครื่องเล่นอยู่ใน card G อยู่แล้ว จะไม่มีค่าใช้จ่ายเพิ่มเติม
                    print("No extra charge")
                elif int(cost) == 0:  #ถ้าราคาเครื่องเล่น =0 เครื่องเล่นอยู่ระหว่างการปรับปรุง
                    print("under rennovation")
                else:
                    self.income = self.income + cost #ถ้าเครื่องเล่นไม่ได้อยู่ใน card G จะบวกราคาเครื่องเล่นใหม่เข้าไปแล้วแสดงราคาที่ต้องจ่ายเพิ่ม
                    print("have to pay %d baht" % cost)
            elif card == "P":  #กรณีบัตร P
                if int(cost) == 0:  #ถ้าราคาเครื่องเล่น =0 เครื่องเล่นอยู่ระหว่างการปรับปรุง
                    print("under rennovation")
                else:  #เครื่องเล่นอยู่ใน card P จะไม่มีค่าใช้จ่ายเพิ่มเติม
                    print("No extra charge")
            elif card == "N": #กรณีบัตร N
                if int(cost) == 0:  #ถ้าราคาเครื่องเล่น =0 เครื่องเล่นอยู่ระหว่างการปรับปรุง
                    print("under rennovation")
                else:
                    self.income = self.income + cost #แสดงราคาบัตรค่าเข้าที่ต้องจ่าย
                    print("have to pay %d baht" % cost)

        except:
            print("Not found %s" % nameA) #ไม่พบข้อมูล


class Menu:
    def __init__(self): # ฟังก์ชันสำหรับประกาศตัวแปรที่เรียกใช้ภายใน class
        self.inforlist = InforList()
        self.heartland = Heartland()
        self.choices = {
            '1': self.adddata_cus,
            '2': self.add_Rides,
            '3': self.delete_Rides,
            '4': self.select_Rides,
            '5': self.quit,
        }

    def display_menu(self): #ฟังก์ชันที่ใช้แสดงหน้าหลัก
        print(
            '''
Welcome to Heart Land
1. Add customer information
2. Add Rides
3. Delete Rides
4. Select Rides for customer
5. Quit
'''
        )

    def run(self): #ฟังก์ชันรับข้อมูลแล้วตรวจสอบว่ามีในช้อยหรือไม่
        while True:
            self.display_menu()
            choice = input('Enter an option : ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def adddata_cus(self): #กรอกข้อมูลลูกค้า
        self.inforlist.inforname()
        self.addCard()

    def addCard(self): #เลือกเลเวลบัตร แสดงชื่อ,ราคาบัตร,เครื่องเล่นในแต่ละบัตร
        costB = self.heartland.cardLevelBcost()
        nameB = str(self.heartland.cardLevelBname())
        costS = self.heartland.cardLevelScost()
        nameS = nameB+str(self.heartland.cardLevelSname())
        costG = self.heartland.cardLevelGcost()
        nameG = nameS+str(self.heartland.cardLevelGname())
        costP = self.heartland.cardLevelPcost()
        print('''
N : Ticket for chlid price 99 baht (age not over 15)
    Ticket for adult price 149 baht\n
B : Bronze price %d baht\n%s\n
S : Silver price %d baht\n%s\n
G : Gold price %d baht\n%s\n
P : Platinum price %d baht\n All Free!!\n
''' % (costB, nameB, costS, nameS, costG, nameG, costP))
        self.inforlist.inforcard()
        self.heartland.checkCard(self.inforlist.name, self.inforlist)


    def add_Rides(self): #เพิ่มเครื่องเล่นและราคาเครื่องเล่น
        addtoy = input('Name Ride : ') #ใส่ชื่อเครื่องเล่น
        costtoy = input('Cost Ride : ') #ใส่ราคาเครื่องเล่น
        self.heartland.insert(addtoy, int(costtoy))

    def delete_Rides(self): #ลบเครื่องเล่น
        print(str(self.heartland.cardLevelBname())+str(self.heartland.cardLevelSname())+"\n"
                +str(self.heartland.cardLevelGname())+str(self.heartland.cardLevelPname()))
        deltoy = input('Name Ride : ') #ใส่ชื่อเครื่องเล่น
        self.heartland.delete(deltoy)

    def select_Rides(self): #เลือกเครื่องเล่นเพิ่มเติม
        name = input("Customer's name: ") #ใส่ชื่อลูกค้า
        print(str(self.heartland.cardLevelBname())+str(self.heartland.cardLevelSname())+"\n"
                +str(self.heartland.cardLevelGname())+str(self.heartland.cardLevelPname()))
        ride = input("Ride: ") #ใส่เครื่องเล่น
        self.heartland.addcost(name, ride, self.inforlist)

    def quit(self): #จบการทำงาน
        total = self.heartland.income
        print("Today's income is %d bath" % total) #แสดงรายรับทั้งหมด
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
