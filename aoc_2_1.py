### AOC 2-1

raw_input = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

clean_input = raw_input.strip('\n').split('\n')

def parseLine(line):
	policy = line.split(':')[0]
	password = line.split(':')[1]
	policy_details = policy.split(" ")
	policy_text = policy_details[1]
	policy_low_count = int(policy_details[0].split("-")[0])
	policy_high_count = int(policy_details[0].split("-")[1])
	return (policy_low_count, policy_high_count, policy_text, password)

def findCountInText(sample, text):
	count = 0
	pos = text.find(sample)
	while pos != -1:
		count = count+1
		pos = text.find(sample, pos+len(sample))
	return count

def testLine(low, high, sample, password):
	count = findCountInText(sample, password)
	return count >= low and count <= high


passCount = 0
for line in clean_input:
	parsedLine = parseLine(line)
	if testLine(*parsedLine):
		passCount = passCount + 1

print("Passed: ", passCount)
