SELECT
	[mySession].[session_id] AS [SessionId],
	[mySession].[login_time] AS [SessionEstablishTime],
	ISNULL([mySession].[program_name],'Internal Session') AS [ProgramName],
	[mySession].[login_name] AS [SQLServerLoginName],
	[mySession].[original_login_name] AS [LoginName],
	[mySession].[status] AS [Status],                                 
	ISNULL([mySession].[host_name],'Internal Session') AS [HostName],
	[mySession].[last_request_end_time] [LastRequestEndTime],
	[mySession].[last_request_start_time] [LastRequestStartTime],
	DB_NAME([mySession].[database_id]) AS [DataBase],
	DB_NAME([mySession].[cpu_time]) AS [CPUTime],
	DB_NAME([mySession].[memory_usage]) AS [MemoryUsage]
FROM 
	sys.dm_exec_sessions AS [mySession]