from crontab import CronTab

my_cron = CronTab()


print(my_cron)

for j in my_cron:
	print(j)
job = my_cron.new(command='python3 /home/pi/AzanPlayer/test.py > logs.txt')
job.minute.on(27)
job.hour.on(16)
my_cron.write()
print("done")
