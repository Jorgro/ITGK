doll_dic = {'green': [], 'blue': [], 'red': []}



with open('input-dolls.txt', 'r') as file:
    for line in file:
        line=line.strip()
        line = line.split(',')
        ge = doll_dic.get(line[0])
        ge.append(int(line[1]))
        doll_dic[line[0]] = ge
for key, value in doll_dic.items():
    value.sort()
    value.reverse()



from urllib.request import urlopen

dolls=[[line[0],int(line[1])] for line in sorted([tuple(i.decode('utf-8').strip('\n').split(',')) for i in urlopen("https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-dolls.txt")],key=lambda x: int(x[1]))]
result=0
previous=['yellow',0]
print(dolls)
for doll in dolls:
	if doll[0]!=previous[0] and doll[1]>previous[1]:
		result+=1
		previous=doll

print(result)
