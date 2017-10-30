systolic_pressure = int(raw_input("What is the systolic blood pressure (mmHg)? "))

heart_rate = int(raw_input("What is the heart rate (bpm)? "))

body_temperature = int(raw_input("What is the body temperature (Celsius)? "))

respiratory_rate = int(raw_input("What is the respiratory rate? (breaths/minute) "))

urine_output = int(raw_input("What is the 4 hour urine output (millilitres)? "))

consciousness = int(raw_input("""State the level of consciousness:
1 - Unresponsive
2 - Pain
3 - Agitation/Confusion
4 - Voice
5 - Alert
 """))

print """\nPATIENT REPORT:
This patient has a systolic blood pressure of %r mmHg,
a heart rate of %r bpm, a body temperature of %r degrees Celsius, a respiratory rate of %r breaths per minute, a urine output of %r millitres every 4 hours
and has a response level of %r.\n""" % (systolic_pressure, heart_rate, body_temperature, respiratory_rate, urine_output, consciousness)

if systolic_pressure < 89:
    print "Blood pressure is low."
elif systolic_pressure > 90 and systolic_pressure < 120:
    print "Blood pressure is normal."
elif systolic_pressure > 121 and systolic_pressure < 140:
    print "Blood pressure is high."
elif systolic_pressure > 141:
    print "Blood pressure is very high."

if heart_rate < 49:
    print "Heart rate is low."
elif heart_rate > 50 and heart_rate < 100:
    print "Heart rate is normal."
elif heart_rate > 101 and heart_rate < 140:
    print "Heart rate is high."
elif heart_rate >  141:
    print "Heart rate is very high."

if respiratory_rate < 5:
	print "Respiratory rate is very low."
elif respiratory_rate >5 and respiratory_rate < 8:
	print "Respiratory rate is low."
elif respiratory_rate > 21 and respiratory_rate < 35:
	print "Respiratory rate is high."
elif respiratory_rate > 35:
	print "Respiratory rate is very high."
else:
	print "Respiratory rate is normal."


if urine_output < 79:
    print "Urine output is low."
elif urine_output > 80 and urine_output < 120:
    print "Urine output is normal."
elif urine_output > 121:
    print "Urine output is high."


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
