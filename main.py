import datetime, json, os, pyperclip, random, string, tabulate
from InquirerPy.separator import Separator as sep
from InquirerPy import inquirer as inq

TAG = "v1.0"

clear = lambda: os.system("clear") if os.name != "nt" else os.system("cls")


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


class Main:
    def __init__(self) -> None:
        self.running = True

    def run(self) -> None:
        while self.running:
            self.mainMenu()

    def printHeader(self, title: string = "Random Keygen"):
        clear()

        HEAD_CHAR = "="
        TITLE_CHAR = " "
        FOOT_CHAR = "="

        # Total length must add up to 45
        titleCharCount = 43 // 2 - len(title) // 2
        formattedTitle = " ".join(
            [TITLE_CHAR * titleCharCount, title, TITLE_CHAR * titleCharCount]
        )

        if len(formattedTitle) < 45:
            formattedTitle = formattedTitle + " "

        print(HEAD_CHAR * 14, "© 2025 garrynet", HEAD_CHAR * 14)
        print(formattedTitle)
        print(FOOT_CHAR * 19, TAG, FOOT_CHAR * 20)
        print("")

    def mainMenu(self) -> None:
        self.printHeader()

        choicePool = [
            "Generate Key",  # 0
            sep(),
            "Recall",  # 2
            "Wipe History",  # 3
            sep(),
            "Exit",  # 5
        ]

        selection = inq.select(
            message="Select Operation:",
            choices=choicePool,
            qmark="[*]",
            amark="[+]",
            pointer=">",
        ).execute()

        # I'm aware I could've matched to strings, but I wanted to make it easier to rename options down the line
        match selection:
            case x if x == choicePool[0]:  # Generate Key
                self.generateMenu()
            case x if x == choicePool[2]:  # Recall
                self.recallMenu()
            case x if x == choicePool[3]:  # Wipe History
                self.confirmWipe()
            case x if x == choicePool[5]:  # Exit
                self.running = False
                clear()

    def generateMenu(self) -> None:
        self.printHeader("Generate Key")
        input()

    def recallMenu(self) -> None:
        self.printHeader("Recall")
        input()

    def confirmWipe(self) -> None:
        self.printHeader("Wipe History")
        input()


if __name__ == "__main__":
    try:
        app = Main()
        app.run()
    except KeyboardInterrupt:
        print("Stopping...")
        exit(0)
    except Exception as e:
        print(e)
        exit(1)
