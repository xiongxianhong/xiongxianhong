#coding:gbk
"""
目的:完成RPSLS游戏
作者:熊先红
2019/11/20
"""

import random

def name_to_number(name):
	if name=="石头":
		return 0
	if name=="史波克":
		return 1
	if name=="布":
		return 2
	if name=="蜥蜴":
		return 3
	if name=="剪刀":
		return 4
	if name!="石头" or "史波克" or "布" or "蜥蜴" or "剪刀":
		return 233
		
def number_to_name(number):
	if number==0:
		return "石头"
	if number==1:
		return "史波克"
	if number==2:
		return "布"
	if number==3:
		return "蜥蜴"
	if number==4:
		return "剪刀"

def rpsls(player_choice):
	print("您的选择为:",player_choice)
	player_number=name_to_number(player_choice)
	comp_number=random.randrange(0,5)
	comp_choice=number_to_name(comp_number)
	print("计算机的选择为:",comp_choice)
	if player_number-comp_number in range(-4,-2) or player_number-comp_number in range(1,3):
		print("您赢了")
	elif player_number-comp_number in range(-2,0) or player_number-comp_number in range(3,5):
		print("计算机赢了")
	elif player_number-comp_number==0:
		print("您和计算机出的一样呢")
	if player_number==233:
		print("Error:No Correct Name")

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
