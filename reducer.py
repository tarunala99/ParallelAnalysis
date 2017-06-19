#!/usr/bin/env python
from operator import itemgetter
import sys
current_word = None
current_count = 0 
word = None
dict1={}
for line in sys.stdin:
	line=line.strip()
	word,web,count,date =line.split('\t')
	try:
		count=int(count)
	except ValueError:
		continue
	if current_word == word:
		current_count += count
		if date in dict1:
			dict1[date]=dict1[date]+count
		else:
			dict1[date]=count
	else:
		if (current_word and current_count>100000):
			sys.stdout.write('%s\t%s\t' % (current_count, current_word))
			count1=1
			while(count1<=31):
				wq="201605"+str(count1/10)+str(count1%10)
				if(wq in dict1):
					sys.stdout.write('%s:%s\t' % (wq, dict1[wq]))
				else:
					sys.stdout.write('%s:%s\t' % (wq, 0))
				count1=count1+1
			sys.stdout.write('\n')
			sys.stdout.flush()
		dict1={}
		current_count=count
		current_word=word
		dict1[date]=count
if(current_word == word and current_count>100000):
	sys.stdout.write('%s\t%s\t' % (current_count, current_word))
	count1=1
	while(count1<=31):
		wq="201605"+str(count1/10)+str(count1%10)
		if(wq in dict1):
			sys.stdout.write('%s:%s\t' % (wq, dict1[wq]))
		else:
			sys.stdout.write('%s:%s\t' % (wq, 0))
		count1=count1+1
	sys.stdout.write('\n')
	sys.stdout.flush()
			
