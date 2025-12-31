
'''
CREATED BY Navtej-Singh-1053
© 2025 Navtej Singh Saggar
Educational use only

12/31/2025

Version - 0.0.1

'''



import os
import time
import webbrowser


RED = "\033[1;31m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"
B_Red = "\033[1;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
ORANGE = "\033[38;5;214m"
YELLOW = "\033[0;33m"
N_Green = "\033[92m"

os.system("clear")

print(N_Green+r'''

 _   _             _       _   _____ _             _
| \ | |           | |     (_) /  ___(_)           | |
|  \| | __ ___   _| |_ ___ _  \ `--. _ _ __   __ _| |__
| . ` |/ _` \ \ / / __/ _ \ |  `--. \ | '_ \ / _` | '_ \
| |\  | (_| |\ V /| ||  __/ | /\__/ / | | | | (_| | | | |
\_| \_/\__,_| \_/  \__\___| | \____/|_|_| |_|\__, |_| |_|
                         _/ |                 __/ |
                        |__/                 |___/
'''+RESET)


print("FOLLOW -> https://github.com/Navtej-Singh-1503/")
time.sleep(2)


def fol():
    query = input("WANT TO FOLLOW ME? [Y/N] : ").strip().lower()

    if query in ["y", "yes"]:
        print("THANKS!!!")
        webbrowser.open("https://github.com/Navtej-Singh-1503/")

    elif query in ["n", "no"]:
        print("Please!!")
        user2 = input("[Y/N] : ").strip().lower()

        if user2 in ["y", "yes"]:
            print("THANKS!!!")
            webbrowser.open("https://github.com/Navtej-Singh-1503/")
        elif user2 in ["n", "no"]:
            print("OK!!")
        else:
            print("Invalid input!!")
    else:
        print("Invalid input!!")


print(BLUE + "Enter Tier number 1-5")
print("1st one is the most dangerous and 5th one is the lightest but still dangerous" + RESET)

user = input(">> ").strip()
print(RESET)


if user in ["1", "01"]:
    print(B_Red + """
1. Cerberus – Advanced banking trojan + spyware                FIND - Spyware
2. AnubisSpy – Banking fraud + mic/screen spying               FIND - RAT
3. Exodus – Government-grade spyware                           FIND - Spyware
4. Skygofree – Nation-state level surveillance                 FIND - Spyware
5. Chrysaor – APT-level Android spyware                        FIND - Threat
6. Bahamut – Targeted cyber-espionage                          FIND - Cyber Espionage
7. Monokle – Military-grade spyware                            FIND - Spyware
8. Tempting Cedar – Advanced persistent threat (APT)           FIND - Cyber Espionage
""" + RESET)
    fol()


elif user in ["2", "02"]:
    print(ORANGE + """
1. BRATA – Screen recording banking trojan                     FIND - Banking Trojan
2. BankBot – Fake overlays, OTP theft                          FIND - Banking Trojan
3. ExoBot – Banking trojan with remote commands                FIND - Banking Trojan
4. Gustuff – Banking + crypto wallet theft                     FIND - Banking Trojan
5. MysteryBot – Keylogging & overlays                          FIND - Banking Trojan
6. Marcher – Large-scale banking phishing                      FIND - Banking Trojan
7. Svpeng – OTP & SMS banking fraud                            FIND - SMS Trojan
8. Asacub – SMS-based banking attacks                          FIND - Banking Trojan
9. Hydra – Credential stealing trojan                          FIND - Banking Trojan
10. Slempo – Banking & SMS spyware                             FIND - SMS Spyware
11. SpyBanker – Financial credential stealer                   FIND - Banking Trojan
""" + RESET)
    fol()


elif user in ["3", "03"]:
    print(YELLOW + """
1. GoldenRAT – Full remote access                              FIND - RAT
2. Premier RAT – Camera, mic, file control                     FIND - RAT
3. TeleRAT – Remote control via Telegram                       FIND - RAT
4. Viper RAT – RAT dropper                                     FIND - RAT
5. Zoopark – Long-term surveillance spyware                    FIND - Spyware
6. Triout – Call logs, SMS, spying                             FIND - Spyware
7. LokiBot – Credential stealer                                FIND - Others
8. CometBot – Botnet malware                                   FIND - Botnet
9. BianLian – Data exfiltration trojan                         FIND - Trojan
""" + RESET)
    fol()

elif user in ["4", "04"]:
    print(YELLOW+"""
1. Triada – Root-level malware                                 FIND - Malware, Tought Malware
2. Ztorg (Downloader / Payload) – Malware installer            FIND - Malware, Install Malware
4. Dvmap – Privilege escalation trojan                         FIND - Malware, Install Malware
5. Retefe – Banking trojan (older)                             FIND - Banking Torjen
6. MazarBot – SMS botnet                                       FIND - Botnet
7. Podec – Premium SMS fraud                                   FIND - SMS Torjen
8. SmsSpy – SMS monitoring                                     FIND - SMS Spyware
9. Slocker – Ransomware (limited)                              FIND - Ransomware
"""+RESET)
    fol()

elif user in ["5", "05"]:
    print(GREEN + """
1. AdultSwine – Scareware                                      FIND - Scareware
2. HiddenAd – Adware                                           FIND - Adware
3. Joker – Premium subscription fraud                          FIND - SMS Trojan
4. KevDroid – Adware trojan                                    FIND - Adware
5. Catelites – Aggressive adware                               FIND - Adware
6. YellYouth – Adware                                          FIND - Adware
7. FlexNet – Adware                                            FIND - Adware
8. GlanceLove – Adware                                         FIND - Adware
9. TinyZ – Lightweight trojan                                  FIND - Trojan
10. Raxir – Basic data-stealing trojan                         FIND - Trojan
11. Pornhub (Fake App) – Trojanized app                        FIND - Adware
""" + RESET)
    fol()

else:
    print(RED + "Invalid Tier Number!" + RESET)

