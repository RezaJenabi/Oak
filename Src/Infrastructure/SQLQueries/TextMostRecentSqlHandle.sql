SELECT 
	[myText].[text]
FROM 
	[sys].[dm_exec_sql_text]([myConnection].[most_recent_sql_handle]) AS [myText];
--[myConnection].[most_recent_sql_handle] get from dm_exec_connections