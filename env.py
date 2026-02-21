from dotenv import load_dotenv, dotenv_values

userdata = dotenv_values()

print(userdata.get("MODEL"))
print(userdata.get("TEMPERATURE"))
print(userdata.get("BASE_URL"))