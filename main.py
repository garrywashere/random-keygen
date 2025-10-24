import datetime, os, pickle, pyperclip, random, secrets, string, sys, tabulate, traceback, xxhash
from InquirerPy.separator import Separator as sep
from InquirerPy import inquirer as inq

RECENTLY_GENERATED_PATH = "./data/recentlyGenerated.bin"
TAG = "v1.1"

clear = lambda: os.system("clear") if os.name != "nt" else os.system("cls")


class Generator:
    def __init__(self) -> None:
        self.systemRandom = random.SystemRandom()

    def generateKey(self, length: int, special: bool = True) -> str:
        if special:
            __charPool = string.ascii_letters + string.digits + string.punctuation
        else:
            __charPool = string.ascii_letters + string.digits

        poolLength = len(__charPool)
        __keyBuilder = []
        for i in range(length):
            __keyBuilder.append(
                __charPool[self.systemRandom.randint(0, poolLength - 1)]
            )
        __generatedKey = "".join(__keyBuilder)
        return __generatedKey


class Key:
    def __init__(self, key: str) -> None:
        self.__key = key

        self.timestamp = datetime.datetime.now().strftime("%Y/%m/%d @ %H:%M:%S")

    def generateKeyId(self) -> None:
        hasher = xxhash.xxh64()
        salt = secrets.token_hex(8)
        hasher.update((salt + self.__key).encode())

        self.keyId = hasher.hexdigest()

    def getListWithKey(self) -> list:
        return [self.keyId, self.__key, self.timestamp]

    def getList(self) -> list:
        return [self.keyId, self.timestamp]


class Main:
    def __init__(self) -> None:
        self.running = True

        if not os.path.exists(RECENTLY_GENERATED_PATH):
            try:
                os.mkdir("./data")
            except FileExistsError:
                pass

            with open(RECENTLY_GENERATED_PATH, "wb") as file:
                pickle.dump([], file)

    def run(self) -> None:
        while self.running:
            self.mainMenu()

    def printHeader(self, title: string = "Random Keygen"):
        clear()

        HEAD_CHAR = "="
        TITLE_CHAR = " "
        FOOT_CHAR = "="

        # total length must add up to 45
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

    def sendToDisk(self, key: str) -> None:
        keyObject = Key(key)
        keyObject.generateKeyId()

        # get pickle
        __recentlyGeneratedList = None
        with open(RECENTLY_GENERATED_PATH, "rb") as file:
            __recentlyGeneratedList = pickle.load(file)

        __recentlyGeneratedList.append(keyObject.getListWithKey())

        # set pickle
        with open(RECENTLY_GENERATED_PATH, "wb") as file:
            pickle.dump(__recentlyGeneratedList, file)

    def generateMenu(self) -> None:
        self.printHeader("Generate Key")

        print("NOTE: Some Services Are NOT Compatible With Special Characters.\n")
        specialCharsToggle = inq.confirm(
            message="Would You Like to Use Special Characters?",
            default=True,
            qmark="[*]",
            amark="[+]",
        ).execute()

        desiredLength = inq.number(
            message="Input Desired Key Length:",
            default=32,
            max_allowed=128,
            min_allowed=1,
            qmark="[*]",
            amark="[+]",
        ).execute()

        desiredLength = int(desiredLength)

        generatorObject = Generator()
        __key = generatorObject.generateKey(desiredLength, specialCharsToggle)

        print("\n" + "-" * desiredLength + "\n")
        print(__key)
        print("\n" + "-" * desiredLength + "\n")

        self.sendToDisk(__key)

        pyperclip.copy(__key)
        print("[+] Copied to Clipboard.\n")

        print("NOTE: Clipboard Contents Will Be Erased When Continuing\n")
        input("Press Return to Continue.")
        pyperclip.copy("")

    def recallMenu(self) -> None:
        self.printHeader("Recall")

        with open(RECENTLY_GENERATED_PATH, "rb") as file:
            for keyRecord in pickle.load(file):
                print(keyRecord)

        print("")

        input("Press Return to Continue.")

    def confirmWipe(self) -> None:
        self.printHeader("Wipe History")

        print("WARNING: This Operation Is Non-Reversible, ALL DATA WILL BE LOST.\n")
        confirmation = inq.confirm(
            message="Are You Sure?", default=False, qmark="[*]", amark="[+]"
        ).execute()

        # TESTING ONLY! NOT SECURE!
        # implement secure erase later
        if confirmation:
            os.remove(RECENTLY_GENERATED_PATH)
            print("\n[+] Wipe Complete.")

            self.running = False

        input("\nPress Return to Continue.")


if __name__ == "__main__":
    try:
        app = Main()
        app.run()
        sys.exit(0)
    except KeyboardInterrupt:
        print("Stopping...")
        sys.exit(0)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
