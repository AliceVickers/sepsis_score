print "What is the respiratory rate (breaths per minute)?"
respiratory_rate = int(raw_input("> "))

print "What is the systolic blood pressure (mmHg)?"
systolic_pressure = int(raw_input("> "))

print "What is the heart rate (bpm)?"
heart_rate = int(raw_input("> "))

print "What is the body temeprature (Celsius)"
body_temperature = int(raw_input("> "))

print "What is the 4 hour urine output?"
urine_output = int(raw_input("> "))

print "State the patient response level:\n"
print """Alert = 0
Voice = 1
Agitation/Confusion = 2
Pain = 3
Unresponsive = 4\n """
response_level = raw_input("> ")

print """\nPATIENT REPORT:
This patient has a respiratory rate of %r breaths per minute,
a systolic blood pressure of %r mmHg,
a heart rate of %r bpm, a body temeprature of %r Celsius,
a urine output of %r every 4 hours
and has a response level of %r.\n""" % (
	respiratory_rate, systolic_pressure,
	heart_rate, body_temperature, urine_output, response_level)

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

if respiratory_rate <5 and systolic_pressure <70 and heart_rate <40 and urine_output <60 and response_level == "4":
	print "Sepsis warning level is high - antibiotics required urgently."
elif respiratory_rate >5 and respiratory_rate >8 and systolic_pressure >70 and systolic_pressure <79 and heart_rate >40 and heart_rate <49 and urine_output >60 and urine_output <79 and response_level == "3":
	print "Sepsis warning level is orange."
elif respiratory_rate >5 and respiratory_rate >8 and systolic_pressure >80 and systolic_pressure <89 and heart_rate >40 and heart_rate <49 and urine_output >80 and urine_output <120 and response_level == "2":
	print "Spesis warning level is yellow."
