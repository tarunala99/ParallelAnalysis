#!/usr/bin/env python
import sys
import os
list1=['Draft_talk:', 'Draft:', 'Gadget_talk:', 'Gadget:', 'Gadget_definition_talk:', 'Gadget_definition:', 'Talk:', 'User_talk:', 'User:', 'Wikipedia_talk:', 'Wikipedia:', 'File_talk:', 'File:', 'MediaWiki_talk:', 'MediaWiki:', 'Topic:', 'Education_Program_talk:', 'Education_Program:', 'TimedText_talk:', 'TimedText:', 'Book:', 'Book_talk:', 'Portal:', 'Portal_talk:', 'Template_talk:', 'Template:', 'Help_talk:', 'Help:', 'Category_talk:', 'Category:', 'Module_talk:', 'Special:', 'Module:', 'Media:','Draft_talk%3a', 'Draft%3a', 'Gadget_talk%3a', 'Gadget%3a', 'Gadget_definition_talk%3a', 'Gadget_definition%3a', 'Talk%3a', 'User_talk%3a', 'User%3a', 'Wikipedia_talk%3a', 'Wikipedia%3a', 'File_talk%3a', 'File%3a', 'MediaWiki_talk%3a', 'MediaWiki%3a', 'Topic%3a', 'Education_Program_talk%3a', 'Education_Program%3a', 'TimedText_talk%3a', 'TimedText%3a', 'Book%3a', 'Book_talk%3a', 'Portal%3a', 'Portal_talk%3a', 'Template_talk%3a', 'Template%3a', 'Help_talk%3a', 'Help%3a', 'Category_talk%3a', 'Category%3a', 'Module_talk%3a', 'Special%3a', 'Module%3a', 'Media%3a',".png",".gif",".jpg",".jpeg",".tiff",".tif",".xcf",".mid",".ogg",".ogv",".svg",".djvu",".oga",".flac",".opus",".wav",".webm",".ico",".txt"]
list2=["404_error/","Main_Page","Hypertext_Transfer_Protocol","Search"]
##the list numbers have been changed 
for line in sys.stdin:
	k=line.strip()
	l=k.split()
	if(len(l)==4 and (l[0]=="en" or l[0]=="en.m")):
		flag=0
		for b in list1:
			if b.upper() in l[1].upper():
				ty=len(b)+(l[1].upper()).find(b.upper())
				if(ty==len(l[1])):
					flag=1
					break
		for b in list1:
			if b==l[1]:
				flag=1
				break
		if(flag==0):
			if(l[1][0].isupper() or not l[1][0].isalpha()):
					u=os.environ["mapreduce_map_input_file"]
					u=u.split("-")
					print '%s\t%s\t%s\t%s\t' % (l[1],l[0],l[2],u[-2])