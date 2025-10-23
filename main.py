import datetime, json, os, pyperclip, random, string, tabulate
from InquirerPy.separator import Separator as sep
from InquirerPy import inquirer as inq


class Generator:
    def __init__(self) -> None:
        self.__charPool = string.ascii_letters + string.digits + string.punctuation
        self.systemRandom = random.SystemRandom()

    def generateKey(self, length: int) -> str:
        poolLength = len(self.__charPool)
        __keyBuilder = []
        for i in range(length):
            __keyBuilder.append(
                self.__charPool[self.systemRandom.randint(0, poolLength - 1)]
            )
        __generatedKey = "".join(__keyBuilder)
        return __generatedKey


class PreviouslyGeneratedDatabase:
    def __init__(self) -> None:
        if not os.path.exists("./data"):
            os.mkdir("./data")

        try:
            self.__file = open("./data/generatedKeys.json", "at")
        except Exception as e:
            print(e.__traceback__)
            exit(1)

    def __del__(self):
        self.__file.close()

    # def saveKey(self, key: string) -> None:
    #     try:
    #         __keyDatabase = json.loads(self.__file.read())
    #     except Exception as e:
    #         print(e.__traceback__)
    #         exit(1)

    #     keyID = "lmao"
    #     timestamp = "01/04/2006"

    #     __keyDict = {"keyID": keyID, "key": key, "timestamp": timestamp}
    #     self.__file.write(json.dumps(__keyDict, indent=4))

    def getKeys(self) -> json:
        pass

    def deleteKey(self, keyID: string) -> None:
        pass

    def secureWipe(self) -> None:
        pass


class KeygenUi:
    def __init__(self) -> None:
        self.running = True

    def start(self) -> None:
        while self.running:
            self.main()

    def main(self) -> None:
        print("=" * 15, "Random Keygen", "=" * 15)
        print("=" * 14, "© 2025 garrynet", "=" * 14)
        print("")
        selection = inq.select(
            message="Operations:",
            choices=["Generate", sep(), "View Previous", "Exit"],
            qmark="[*]",
            amark="[+]",
        ).execute()

        match selection:
            case "Generate":
                generator = Generator()
                print("")
                __newKey = generator.generateKey(8)
                pyperclip.copy(__newKey)
                print(__newKey)
                print("")
            case "View Previous":
                pass
            case "Exit":
                pass
            case _:
                raise NotImplementedError

        self.running = False

    def genKey(self) -> None:
        pass

    def sendToClipboard(self, key) -> None:
        pass

    def showKeys(self) -> None:
        pass

    def markKeysForDeletion(self) -> None:
        pass

    def confirmSecureWipe(self) -> None:
        pass


if __name__ == "__main__":
    try:
        ui = KeygenUi()
        ui.start()
    except KeyboardInterrupt:
        print("Stopping...")
    except Exception as e:
        print(e)
