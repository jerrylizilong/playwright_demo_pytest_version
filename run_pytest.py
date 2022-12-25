import pytest
import os,time
currentPath = os.path.dirname(os.path.abspath(__file__))
date =time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())

def run_test():
    report_path = os.path.join(currentPath , 'reports',str(date))
    allure_report_path = os.path.join(currentPath , 'allure-report',str(date))
    test_folder = os.path.join(currentPath)
    # os.system('python3 -m pytest %s --headed --browser webkit --browser firefox  --alluredir=%s -o log_cli=true -o log_cli_level=INFO' %(test_folder,report_path))
    os.system('python3 -m pytest %s  --numprocesses auto --reruns 2 --headed --browser chromium  --headed --browser webkit --browser firefox  --alluredir=%s -o log_cli=true -o log_cli_level=INFO' %(test_folder,report_path))
    os.system('allure generate %s -o %s -c' %(report_path,allure_report_path))


if __name__=='__main__':
    run_test()
