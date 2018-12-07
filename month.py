import datetime

begin_str = '2018-11-01 00:00:00'
end_str = '2018-11-20 00:00:00'
begin_dt = datetime.datetime.strptime(begin_str, '%Y-%m-%d %H:%M:%S')
end_dt = datetime.datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S')
day_list = []
while begin_dt < end_dt:
    day_str = str(begin_dt)
    day_list.append(day_str)
    begin_dt = begin_dt + datetime.timedelta(hours=1)
for begin_str in day_list:
    begintime = datetime.datetime.strptime(begin_str, '%Y-%m-%d %H:%M:%S')
    endtime = begintime +datetime.timedelta(hours=1)-datetime.timedelta(microseconds=1)
    end_str = str(endtime)
    print begintime, endtime
