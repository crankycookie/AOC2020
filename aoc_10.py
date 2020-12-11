input = """
2
49
78
116
143
42
142
87
132
86
67
44
136
82
125
1
108
123
46
37
137
148
106
121
10
64
165
17
102
156
22
117
31
38
24
69
131
144
162
63
171
153
90
9
107
79
7
55
138
34
52
77
152
3
158
100
45
129
130
135
23
93
96
103
124
95
8
62
39
118
164
172
75
122
20
145
14
112
61
43
141
30
85
101
151
29
113
94
68
58
76
97
28
111
128
21
11
163
161
4
168
157
27
72
"""

InputList = [int(i) for i in input.strip("\n").split("\n")]
InputList.sort()

def easyDifferencesFromJolt():
  diffCounter = [0,0,0]
  currentJolt = 0
  targetJolt = InputList[-1] + 3

  for i in InputList:
    diff = i-currentJolt
    if diff > 3:
      print("Unable to reach finalJolt")
      break
    else:
      diffCounter[diff-1] += 1
      currentJolt = i

  if currentJolt + 3 == targetJolt:
    diffCounter[2] += 1

  print("Current Jolt:", currentJolt)
  print("Target Jolt:", targetJolt)
  print("DiffCounter:", diffCounter)
  return diffCounter

# easyDifferencesFromJolt()

cacheMap = [None for x in range(len(InputList))]

def countPathsToFinalJolt(adapterList, currentJolt = 0):
  targetJolt = InputList[-1]
  totalPaths = 0

  # Nothing else in the list matters since this is the final jolt
  if currentJolt == targetJolt:
    return 1

  # Go through each possible diff
  for diff in [1,2,3]:
    adapterVal = currentJolt + diff
    if adapterVal in adapterList:
      adapterIdx = adapterList.index(adapterVal)
      cacheIdx = InputList.index(adapterVal)
      if cacheMap[cacheIdx] == None:
        cacheMap[cacheIdx] = countPathsToFinalJolt(adapterList[adapterIdx+1:], adapterVal)
      totalPaths += cacheMap[cacheIdx]

  return totalPaths


print(countPathsToFinalJolt(InputList))
