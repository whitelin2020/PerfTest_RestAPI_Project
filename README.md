# Restful  API  Performace Test  Project

1. This is a Rest API Performance test Project, we use the https://gorest.co.in/ website as our test site.You need to obtain the API Token to  run this project. You can apply the API Token from https://gorest.co.in/consumer/login.

2. You need to copy  configuration.py  from configuration.py.template file under the same conf folder.

3. You need to replace this API Token which you got to the placeholder <APIToken>. 

4. Run test script follow below order :
run_query_user_api.sh  ----> run_create_user_api.py ---> run_create_user_csv.py ---> run_update_user_api.sh ---> run_delete_user_api.sh

5. If you are using jenkin server as your CI server. You need to set up credentials  ID as "API_SECRET"  with the API token which you got.And then , you setup a pipeline as "Pipeline script from SCM" to use this repository URL and master Branch. Set Script Path as "Jenkinfile". So , you can set up and run the entire CI piple line to run this performance test.

6. The Performance test result will generate a folder  under the "result" directionary. Each folder will have four different files.
html file : give you a basic information and summary the test result for one API.
[Script_PREFIX]_stats.csv, [Script_PREFIX]_stats_history.csv and [Script_PREFIX]_failures.csv : store current request stats to files in CSV format.

7. After running each api test script  , it will generate a log file under logs folder.
