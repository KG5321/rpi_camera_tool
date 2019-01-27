import os
from google_drive_rpi import drive_api
from time import strftime
from apscheduler.schedulers.blocking import BlockingScheduler


def drive_init():
    scopes = ['https://www.googleapis.com/auth/drive']
    api = drive_api.drive_api(scopes,'token.pickle','credentials.json')
    api.init_drive()
    return api

def take_picture():
    cmd = 'raspistill -o img.jpg'
    os.system(cmd)

def run_job():
    api = drive_init()
    print("Taking pic")
    take_picture()
    file_name = 'img'+strftime("%H%M%d%m")+'.jpg'
    print("Uploading...")
    api.upload_file(file_name,'img.jpg','')
    print("Done uploading file: "+file_name)    

if __name__ == '__main__':
    print("Starting, taking first picture...")
    run_job()
    scheduler = BlockingScheduler()
    scheduler.add_job(run_job, 'interval', minutes=30)
    scheduler.start()