#coding:gbk
"""
Ŀ��:���RPSLS��Ϸ
����:���Ⱥ�
2019/11/20
"""

import random

def name_to_number(name):
	if name=="ʯͷ":
		return 0
	if name=="ʷ����":
		return 1
	if name=="��":
		return 2
	if name=="����":
		return 3
	if name=="����":
		return 4
	if name!="ʯͷ" or "ʷ����" or "��" or "����" or "����":
		return 233
		
def number_to_name(number):
	if number==0:
		return "ʯͷ"
	if number==1:
		return "ʷ����"
	if number==2:
		return "��"
	if number==3:
		return "����"
	if number==4:
		return "����"

def rpsls(player_choice):
	print("����ѡ��Ϊ:",player_choice)
	player_number=name_to_number(player_choice)
	comp_number=random.randrange(0,5)
	comp_choice=number_to_name(comp_number)
	print("�������ѡ��Ϊ:",comp_choice)
	if player_number-comp_number in range(-4,-2) or player_number-comp_number in range(1,3):
		print("��Ӯ��")
	elif player_number-comp_number in range(-2,0) or player_number-comp_number in range(3,5):
		print("�����Ӯ��")
	elif player_number-comp_number==0:
		print("���ͼ��������һ����")
	if player_number==233:
		print("Error:No Correct Name")

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
