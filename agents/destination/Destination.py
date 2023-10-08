"""
Source Agent:

Source agents responsible for archival of table.
Cron will be scheduled on source db server based on policy configured on archival service.

Startup Flow:
1) Login to source db and get all schema details: tables/ partitions/ users etc
2) Call Archive service catalog api's to register agents details i.e
     api/v1/service/add, api/v1/dbserver/add, api/v1/table/add, api/v1/schema/add etc

Execution Flow:
1) Retrieve policies information, and get all list of policy to be executed for archive.
2) If policies is ready to execute then it will create record in the execution table to track the execution of archive
    and get the unique id for all policies to be executed.
3) Once policy is retrieved, then it start archival of tables and rename the dump with unique id.
    To archive fetch the detail how old data should be archived. Archieve option 1) Select query
    and it will dump the data to some temp location or we can create partition for data and copy the data files of
    table and rename data file to unique id.
4) Once archive is ready then it will copy all files to destination server( destination details we can get from archive policy)
    It will copy data to temp location on destination server.
5) Update the status of archive in execution table as source_success/source_failed
6) Authorised user can check the status of policy execution and configure policy.


Destination Agent:

Destination agents responsible for process archival to destination database table, and deletion of tables configured in policy.
Cron will be scheduled on destination db server based on policy configured on archival service.

Execution Flow:
Archive Process:
1) Check the temp folder where all the archive is placed and get list of archive and call api /execution/<uid>
    get the policy info from it.
2) Get table and process the archive.
3)  Update the status of archive in execution table as failed/completed.

Deletion
1) Retrieve policies information, and get all list of policy to be executed for deletion.
2) If policies is ready to execute then it will create record in the execution table to track the execution of archive
    and get the unique id for all policies to be executed.
3) Once policy is retrieved, then it start deletion of tables and entry all deletion table name in execution archive service.
5) Update the status of archive in execution table.
6) Authorised user can check the status of policy execution and configure policy.

"""
