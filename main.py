import datetime, json, pyperclip, random, string, tabulate
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
                self.__charPool[self.systemRandom.randint(0, poolLength)]
            )
        __generatedKey = "".join(__keyBuilder)
        return __generatedKey


class PreviouslyGeneratedDatabase:
    def __init__(self) -> None:
        pass

    def saveKey(self) -> None:
        pass

    def getKeys(self) -> json:
        pass

    def deleteKey(self, keyID: string) -> None:
        pass

    def secureWipe(self) -> None:
        pass


class KeygenUi:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        pass

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
    pass
