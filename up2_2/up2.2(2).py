class Train:
    def info(self,title, number, time):
        self.title = title
        self.number = number
        self.time = time

    def get_train(self):
        print(self.title, self.number, self.time)

Train1 = Train()
Train1.info("пункт назначения: {теремок}", " номер поезда: {1}", "время отправления: {14:00}")
Train2 = Train()
Train2.info("пункт назначения: {река}", "номер поезда: {2}", "время отправления: {11:30}")
Train3 = Train()
Train3.info("пункт назначения: {город}", "номер поезда: {3}", "время отправления: {17:25}")

while True:
    choice = int(input("\nвведите номер поезда (1, 2, 3) "
                       "что бы узнать информацию, 0 - стоп"))

    match choice:
        case 1:
            Train1.get_train()
        case 2:
            Train2.get_train()
        case 3:
            Train3.get_train()
        case 0:
            print("программа завершила работу ;(")
            break