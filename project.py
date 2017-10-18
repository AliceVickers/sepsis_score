systolic_pressure = int(raw_input("What is the systolic blood pressure (mmHg)? "))

heart_rate = int(raw_input("What is the heart rate (bpm)? "))

body_temperature = int(raw_input("What is the body temperature (Celsius)? "))

respiratory_rate = int(raw_input("What is the respiratory rate? "))

urine_output = int(raw_input("What is the 4 hour urine output? "))

consciousness = int(raw_input("""State the level of consciousness:
1 - Unresponsive
2 - Pain
3 - Agitation/Confusion
4 - Voice
5 - Alert
6 - Hello """))

print """\nPATIENT REPORT:
This patient has a respiratory rate of %r breaths per minute,
a systolic blood pressure of %r mmHg,
a heart rate of %r bpm, a body temeprature of %r Celsius,
a urine output of %r every 4 hours
and has a response level of %r.\n""" % (
	respiratory_rate, systolic_pressure,
	heart_rate, body_temperature, urine_output, consciousness)

if respiratory_rate < 5:
	print "Respiratory rate is very low!"
elif respiratory_rate >5 and respiratory_rate < 8:
	print "Respiratory rate is low!"
elif respiratory_rate > 21 and respiratory_rate < 35:
	print "Respiratory rate is high!"
elif respiratory_rate > 35:
	print "Respiratory rate is very high!"
else:
	print "Respiratory rate is normal."

if response_level == "0":
	print "Patient is responsive."
elif response_level == "1":
	print "Patient is mildly repsonsive."
elif response_level == "2":
	print "Patient response is concerning."
elif response_level == "3":
	print "Patient response is concerning."
elif response_level == "4":
	print "Patient is unconscious."

## this doesn't work right now!
if respiratory_rate <5 and systolic_pressure <70 and heart_rate <40 and urine_output <60 and response_level == "4":
	print "Sepsis warning level is high - antibiotics required urgently."
elif respiratory_rate >5 and respiratory_rate >8 and systolic_pressure >70 and systolic_pressure <79 and heart_rate >40 and heart_rate <49 and urine_output >60 and urine_output <79 and response_level == "3":
	print "Sepsis warning level is orange."
elif respiratory_rate >5 and respiratory_rate >8 and systolic_pressure >80 and systolic_pressure <89 and heart_rate >40 and heart_rate <49 and urine_output >80 and urine_output <120 and response_level == "2":
	print "Spesis warning level is yellow."



if systolic_pressure in range (100, 180) and heart_rate in range (50, 100) and respiratory_rate in range (9, 20):
	print "Patient in WHITE category"
if (systolic_pressure in range (90, 99) and consciousness == 1) or (heart_rate in range (101, 110)):
	print "Patient in YELLOW category"
#if systolic_pressure in range (80, 89) and urine_output in range (80, 120) and consciousness == 2 or (respiratory_rate in range (21, 30) and systolic_pressure > 180 and heart_rate in range (111, 130)):
#	print "Pateint in GOLD category"
if (systolic_pressure <  70 and heart_rate < 40 and respiratory_rate < 5) or (respiratory_rate > 35 and heart_rate > 140):
	print "Patient in PINK category"
