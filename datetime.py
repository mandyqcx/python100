import sys
import datetime
from config import utils, dbutils, logutils, servinfo

scriptName = utils.getScriptName(__file__)
logger = logutils.getLogger(scriptName)


#@utils.oneday('today')
def main():
    begin_str = '2018-10-01 00:00:00'
    end_str = '2018-10-31 00:00:00'
    begin_dt = datetime.datetime.strptime(begin_str, '%Y-%m-%d %H:%M:%S')
    end_dt = datetime.datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S')
    day_list = []
    while begin_dt <= end_dt:
        day_str = str(begin_dt)
        day_list.append(day_str)
        begin_dt = begin_dt + datetime.timedelta(days=1)
    for begin_str in day_list:
        begintime = datetime.datetime.strptime(begin_str, '%Y-%m-%d %H:%M:%S')
        endtime = begintime + datetime.timedelta(hours=16) - datetime.timedelta(microseconds=1)
        end_str = str(endtime)
        print begin_str
        cmd = servinfo.info.getPsqlCmd(scriptName, begin_time=begin_str, end_time=end_str)
        result = utils.runShell(cmd, logger)
        if not result.status:
            return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
