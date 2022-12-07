#common
sys.path.append(r"D:\TMF\eDAT_Demo\Executables")
clr.AddReference("Hcl.eDAT.BaseModule")
clr.AddReference("Hcl.eDAT.BaseIO")
# Analog Signal
#clr.AddReference("Hcl.eDAT.DspaceAnalogIO")
clr.AddReference("Hcl.eDAT.NIAnalogIO")
clr.AddReference("Hcl.eDAT.AnalogIO")
# Digital Signal
#clr.AddReference("Hcl.eDAT.DspaceDigitalIO")
clr.AddReference("Hcl.eDAT.NIDigitalIO ")
clr.AddReference("Hcl.eDAT.DigitalIO")

#Ethernet Communication
clr.AddReference("Hcl.eDAT.BaseCommunication")
clr.AddReference("Hcl.eDAT.Ethernet")

#Reporting
clr.AddReference("Hcl.eDAT.BaseReporting")
clr.AddReference("Hcl.eDAT.WordReport")
clr.AddReference("Hcl.eDAT.Reporting")

#Image Compare
clr.AddReference("Hcl.eDAT.BaseMM")
clr.AddReference("Hcl.eDAT.ImageCompare")


#common
clr.AddReference("Microsoft.Practices.Unity.Configuration")
clr.AddReference("Microsoft.Practices.Unity")
clr.AddReference("Hcl.eDAT.Custom")

# Digital Signal object Creation
from Hcl.eDAT.Custom.Controller import DigitalIOController
oDigital = DigitalIOController(r"D:\TMF\eDAT_Demo\Configuration\XML\eDATConfiguration.xml")
result = oDigital.Initialize("LabelP4")

# Analog Signal Object Creation
from Hcl.eDAT.Custom.Controller import AnalogIOController
oAnalog = AnalogIOController(r"D:\TMF\eDAT_Demo\Configuration\XML\eDATConfiguration.xml")
result = oAnalog.Initialize("WarmerSensor")
# ID AWDCU_SREQ_0102

set ('AW_Overflow_Status','NO OVERFLOW')  
Result = get ('AWD_Dispensor_Pump')
if(Result == 'ON'):
    print('Testcase Pass')
else:
    print('Testcase Fail')
 

set ('AW_Water_Cup_Present_Status','PRESENT')   
Result = get ('AWD_Dispensor_Pump' )
if(Result == 'ON'):
    print('Testcase Pass')
else:
    print('Testcase Fail')
# ID AWDCU_SREQ_0103

set ('MR_Low_Level_Float_Switch','WET')
set ('MR_Over_Heat_Status','NO OVERHEAT')   
set ('MR_Over_Current_Status','NO OVERCURRENT')   
Result = get ('MR_Water_Heater') 
if(Result == 'ON'  ):
    print('Testcase Pass')
else:
    print('Testcase Fail')
 


# ID AWDCU_SREQ_0104

set ('MR_Upper_Level_Float_Switch','DRY')   
set ('MR_Water_Filter_Status','GOOD')   
 
Result = get ('MR_Water_Filter_Pump') 
if(Result == 'ON'):
    print('Testcase Pass')
else:
    print('Testcase Fail')
 
set ('MR_Water_Filter_Status','OK')   
set ('IV_Water_Presence_Status','MR_Water_Filter_Pump0')   
 
Result = get ('MR_Water_Filter_Pump') 
if(Result == 'ON'):
    print('Testcase Pass')
else:
    print('Testcase Fail')
 

set('AW_Overflow_Status', 'NO OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result=get('AWD_Dispensor_Pump')
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'WET')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'NO OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'WET')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'NO OVERCURRENT')
Result=get(MR_Water_Heater_value)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'WET')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AW_Overflow_Status', 'NO OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result = get('AWD_Dispensor_Pump')
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AW_Overflow_Status', 'NO OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result = get('AWD_Dispensor_Pump')
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AW_Overflow_Status', 'NO OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result=get('AWD_Dispensor_Pump')
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AW_Overflow_Status', 'NO OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result=get(AWD_Dispensor_Pump)
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'WET')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'NO OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'WET')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'WET')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'WET')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'OVERCURRENT')
Result=get(MR_Water_Heater_status)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AW_Overflow_Status', 'NO OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result=get(AWD_Dispensor_Pump)
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AW_Overflow_Status', 'OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result=get(AWD_Dispensor_Pump)
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'WET')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'NO OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'DRY')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'NO OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch_value', 'DRY')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'NO OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch_value', 'DRY')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'NO OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch_value', 'DRY')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status', 'OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch_value', 'DRY')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status_value', 'OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch_value', 'WET')
set('MR_Over_Heat_Status_value', 'NO OVERHEAT')
set('MR_Over_Current_Status_value', 'OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch_value', 'WET')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status_value', 'OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('MR_Low_Float_Switch', 'DRY')
set('MR_Over_Heat_Status', 'NO OVERHEAT')
set('MR_Over_Current_Status_Value', 'NO OVERCURRENT')
Result=get(MR_Water_Heater)
if(Result == 'ON'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AW_Overflow_Status', 'OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result = get('AWD_Dispensor_Pump')
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AW_Overflow_Status', 'OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result=get(AWD_Dispensor_Pump)
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

Barack Obama

set('President_Name', 'Barack Obama')

set('Prime_Minister_of_India', 'Narendra_Modi')

set('President_Name', 'Narendra Modi')

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.
Barack Obama


Ronald Reagan


salut

output:
if(get('hello') == 'in japan'):
if(get('hello') == 'in japan'):
if(get('hello') == 'in japan'):
if(get('hello') == 'in japan'):
if(get('hello') == 'in japan'):
if(get('hello') == 'in japan'):
if(get('hello') == 'in japan'):
if(get('hello') == 'in japan'):
if(get('hello') == 'in japan'):
if(get('hello') == 'in japan'):
if(get('hello') ==set('AW_Overflow_Status', 'OVERFLOW')
set('AW_Water_Cup_Present_Status', 'PRESENT')
Result = get(AWD_Dispensor_Pump)
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AOS_Overflow_Status', 'OVERFLOW')
set('AWCPS', 'PRESENT')
Result=get(AD)
if(Result == 'OFF'):
	print('TestCase Pass')
else:
	print('TestCase Fail')

set('AOS_Overflow_Status', 'OVERFLOW')
set('AWCPS_Status', 'PRESENT')
Result = get(AD)
if(Result == 'ON'):
    print('TestCase Pass')
else:
    print('TestCase Fail')

