import schedule
import time
import datetime

def Task_minute():
    print("TAsk based on minutes gets schedules at: ",datetime.datetime.now())

def Task_Hour():
    print("TAsk based on hour gets schedules at: ",datetime.datetime.now())

def Task_Day():
    print("TAsk based on day gets schedules at: ",datetime.datetime.now())



def main():
    print("Inside Task Schedular")
    print("Current time is: ",datetime.datetime.now())

    schedule.every(1).minutes.do(Task_minute)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().saturday.at("18:00").do(Task_Day)
    while(True):
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
