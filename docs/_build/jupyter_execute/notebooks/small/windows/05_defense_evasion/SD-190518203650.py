# Empire Enabling RDP

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518203650 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/master/lib/modules/powershell/management/enable_rdp.py |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_enable_rdp.tar.gz |

## Dataset Description
This dataset represents adversaries enabling RDP and adding a firewall exception to a compromised system

## Adversary View
```
(Empire: TKV35P8X) > usemodule management/enable_rdp*           
(Empire: powershell/management/enable_rdp) > info

              Name: Enable-RDP
            Module: powershell/management/enable_rdp
        NeedsAdmin: True
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @harmj0y

Description:
  Enables RDP on the remote machine and adds a firewall
  exception.

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        TKV35P8X                  Agent to run module on.                 

(Empire: powershell/management/enable_rdp) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 21
[*] Tasked agent TKV35P8X to run module powershell/management/enable_rdp
(Empire: powershell/management/enable_rdp) > The operation completed successfully.


(Empire: powershell/management/enable_rdp) > 
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_enable_rdp.tar.gz"
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
        