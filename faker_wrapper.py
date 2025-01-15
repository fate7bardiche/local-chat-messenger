from faker import Faker


fakerDict = {
    "name": "name",
    "name_female": "name-female",
    "name_male": "name-male",
    "address_full": "address-full",
    "email": "email",
    "color_hex": "color-hex",
    "color_rgb": "color-rgb",
    "emoji": "emoji",
    "company": "company",
    "country_calling_code": "country-calling-code",
    "phone_number": "phone-number",
    "user_agent": "user-agent",
    "chrome": "chrome",
    "firefox": "firefox",
    "safari": "safari",
    "opera": "opera",
    "internet_explorer": "internet-explorer",
    "linux_platform_token": "linux-platform-token",
    "mac_platform_token": "mac-platform-token",
    "windows_platform_token": "windows-platform-token",
    "android_platform_token": "android-platform-token",
    "linux_processor": "linux-processor",
    "mac_processor": "mac-processor",
    "windows_platform_token": "windows-platform-token"
}

def fakeDataNameTextList():
    text = ""
    for value in fakerDict.values():
        text += '{}\n'.format(value)
    return text

def getValue(fake: Faker, propName: str):
    if(propName == fakerDict["name"]):
        return fake.name()
    if(propName == fakerDict["name_female"]):
        return fake.name_female()
    if(propName == fakerDict["name_male"]):
        return fake.name_male()
    if(propName == fakerDict["address_full"]):
        return fake.address()
    if(propName == fakerDict["email"]):
        return fake.email()
    if(propName == fakerDict["color_hex"]):
        return fake.color()
    if(propName == fakerDict["color_rgb"]):
        return fake.color(color_format='rgb')
    if(propName == fakerDict["emoji"]):
        return fake.emoji()
    if(propName == fakerDict["company"]):
        return fake.company()
    if propName == fakerDict["user_agent"]:
        return fake.user_agent()
    if propName == fakerDict["chrome"]:
        return fake.chrome()
    if propName == fakerDict["firefox"]:
        return fake.firefox()
    if propName == fakerDict["safari"]:
        return fake.safari()
    if propName == fakerDict["opera"]:
        return fake.opera()
    if propName == fakerDict["internet_explorer"]:
        return fake.internet_explorer()
    if propName == fakerDict["linux_platform_token"]:
        return fake.linux_platform_token()
    if propName == fakerDict["mac_platform_token"]:
        return fake.mac_platform_token()
    if propName == fakerDict["windows_platform_token"]:
        return fake.windows_platform_token()
    if propName == fakerDict["android_platform_token"]:
        return fake.android_platform_token()
    if propName == fakerDict["linux_processor"]:
        return fake.linux_processor()
    if propName == fakerDict["mac_processor"]:
        return fake.mac_processor()
    if propName == fakerDict["windows_platform_token"]:
        return fake.windows_platform_token()
    
    else:
        return "用意されていないデータ名です"
