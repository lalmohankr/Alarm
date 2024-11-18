import datetime
import time
import winsound

file_path = "sound.wav"
def alarm(set_alarm_timer):
    print(f"Alarm set for {set_alarm_timer}. Waiting...")
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        print(f"Current Date: {date} | Current Time: {current_time}")
        if current_time == set_alarm_timer:
            print("Time to wake up!")
            winsound.PlaySound(file_path, winsound.SND_FILENAME)
            break

def main():
    print("=== Console-Based Alarm Clock ===")
    print("Enter the alarm time in 24-hour format (HH:MM:SS):")
    
    while True:
        try:
            set_alarm_timer = input("Set Alarm Time: ").strip()
            # Validate the time format
            datetime.datetime.strptime(set_alarm_timer, "%H:%M:%S")
            break
        except ValueError:
            print("Invalid time format. Please try again (HH:MM:SS).")

    alarm(set_alarm_timer)

if __name__ == "__main__":
    main()
