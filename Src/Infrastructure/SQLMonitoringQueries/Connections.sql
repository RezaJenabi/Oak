SELECT        
	[myConnection].[session_id] AS [SessionId], 
	[myConnection].[connect_time] AS [ConnectionEstablishTime], 
	[myConnection].[last_read] AS [LastReadTime], 
	[myConnection].[last_write] AS [LastWriteTime],
	CONCAT([myConnection].[client_net_address],':',[myConnection].[client_tcp_port]) AS [ClientAddress],
	CONCAT([myConnection].[local_net_address],':',[myConnection].[local_tcp_port]) AS [LocalAddress],
	[myConnection].[connection_id] AS [ConnectionId]
FROM            
	[sys].[dm_exec_connections] AS [myConnection];
