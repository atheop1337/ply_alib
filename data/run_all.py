from libraries.twentyfivezeroone import const, EvaSociety
import configparser

def main():
    config = configparser.ConfigParser()
    config.read(const().directory + "/settings.ini")
    safonoff_bool = str(config.get("safonoff", "boolean"))

    EvaSociety().execeva(f"{const().main_directory}/main.py", False)
    EvaSociety().execeva(f"{const().data_directory}/run_serverMonitor.py", True)

    if safonoff_bool == "True":
        EvaSociety().execeva(f"{const().data_directory}/run_ai.py", True)

if __name__ == "__main__":
    main()
