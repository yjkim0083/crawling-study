import subprocess

total_page=145007
period=5000

while True:
    start_page = total_page
    end_page = total_page - period
    total_page = total_page - period - 1

    if end_page < 0:
        end_page = 1
        subprocess.call('nohup python new_total_crawl.py --start={} --end={}'.format(start_page, end_page), shell=True)
        break
    else:
        subprocess.call('nohup python new_total_crawl.py --start={} --end={}'.format(start_page, end_page), shell=True)


