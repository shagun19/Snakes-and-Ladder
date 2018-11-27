#!/bin/python
from __future__ import print_function
from colorclass import Color, Windows
from terminaltables import SingleTable
import termcolor
import random
import itertools

def table_server_status():
    """Return table string to be printed."""
    '''table_data = [
        [Color('Low Space'), Color('{autocyan}Nominal Space{/autocyan}'), Color('Excessive Space')],
        [Color('Low Load'), Color('Nominal Load'), Color('{autored}High Load{/autored}')],
        [Color('{autocyan}Low Free RAM{/autocyan}'), Color('Nominal Free RAM'), Color('High Free RAM')],
    ]'''
    num=termcolor.colored('   88   ',"red","on_yellow",attrs=["blink"])
    table_data = [
        [Color('{autocyan}FINISH{/autocyan}'), Color('99'), Color('98'), Color('97'), Color('96'), Color('95'), Color('94'), Color('93'), Color('92'), Color('91')],
        [Color('81'), Color('82'), Color('83'), Color('84'), Color('85'), Color('86'), Color('87'), Color('%s'%num), Color('89'), Color('90')],
        [Color('80'), Color('79'), Color('78'), Color('77'), Color('76'), Color('75'), Color('74'), Color('73'), Color('72'), Color('71')],
        [Color('61'), Color('62'), Color('63'), Color('64'), Color('65'), Color('66'), Color('67'), Color('68'), Color('69'), Color('70')],
        [Color('60'), Color('59'), Color('58'), Color('57'), Color('56'), Color('55'), Color('54'), Color('53'), Color('52'), Color('51')],
        [Color('41'), Color('42'), Color('43'), Color('44'), Color('45'), Color('46'), Color('47'), Color('48'), Color('49'), Color('50')],
        [Color('40'), Color('39'), Color('38'), Color('37'), Color('36'), Color('35'), Color('34'), Color('33'), Color('32'), Color('31')],
        [Color('21'), Color('22'), Color('23'), Color('24'), Color('25'), Color('26'), Color('27'), Color('28'), Color('29'), Color('30')],
        [Color('20'), Color('19'), Color('18'), Color('17'), Color('16'), Color('15'), Color('14'), Color('13'), Color('12'), Color('11')],
        [Color('{autocyan}Start!{/autocyan}'), Color('   02   '), Color('   03   '), Color('   04   '), Color('   05   '), Color('   06   '), Color('   07   '), Color('   08   '), Color('   09   '), Color('   10   ')],
    ]
    print("\n")
    table_instance = SingleTable(table_data, 'Snakes and Ladders')
    table_instance.inner_heading_row_border = False
    table_instance.inner_row_border = True
    table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center', 5: 'center', 6: 'center', 7: 'center', 8: 'center', 9: 'center'}
    return table_instance.table

def get_score(num_players):
	test_data_1=[6,5,5,5,5,5,5,5,5,5,5,5,5,5,2,6,6,5,4,5,6,1,2,3]
	#test_data_1=[1,3,1,4,6,1,3,1,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,1,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,4,6,5,6,3,2,4,6,3,1,4,6,5,5,5,6]
	test_data_2=[1,3,1,1,3,1,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,4,6,3,1,4,6,5,6,3,2,4,6,3,1,4,6,1,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6]
	test_data_3=[1,3,1,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,4,6,1,3,1,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,5,5,5,6,6,6,6,3,1,4,6,5,6,3,1,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,4,6,2,4,6,3,1,4,6,5,5,5,6]
	test_data_4=[1,3,1,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,4,1,3,1,4,6,6,5,5,5,1,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,4,6,6,5,5,5,6,6,6,6,3,1,4,6,5,5,5,6,6,6,6,3,1,4,6,6,6,6,6,3,1,4,6,5,5,5,6,6,6,5,6,3,2,4,6,3,1,4,6,5,5,5,6]
	test_data=[test_data_1,test_data_2,test_data_3,test_data_4]
	list_of_winners={}
	count=1
	list_players={} ; total_players=num_players
	for i in range(0,num_players):
		list_players.update({ i : 0})
	print(list_players)
	property_dict={1:38,4:14,9:31,17:7,21:42,28:84,51:67,54:34,62:19,64:60,72:91,80:99,87:36,93:73,95:75,98:79}
	dice=[0,0,0]
	print('*************This is a %d player game************'%(num_players))
	while num_players>0:
		while 100 not in list_players.values():
			for i in range(0,num_players):
				player_id=list_players.keys()[i]
				print('-------Turn for player {}: Run {}-----'.format(player_id+1,count))
				dice[0]=random.randint(1,6)
				print('Player {}: You get:[{}] '.format(player_id+1,dice[0]))
				if list_players[player_id]==0 and dice[0]!=6:
					print('You cannot start until you obtain 6!')
					continue
				elif list_players[player_id]==0 and dice[0]==6:
					print('Awesome you enter the game')
					dice[1]=random.randint(1,6)
					if dice[1]!=6:
						print('you got:[{}] to begin the game'.format(dice[1]))
						final_position=get_points(dice[1],0,0,list_players[player_id])
						list_players[player_id]=final_position
						print("New value:%d"%list_players[player_id])
						continue
					elif dice[1]==6:
						print('Whoa another chance in the beginning!!')
						dice[2]=random.randint(1,6)
						if dice[2]!=6:
							print('you got:[{}][{}]'.format(dice[1],dice[2]))
							final_position=get_points(dice[1],dice[2],0,list_players[player_id])
							list_players[player_id]=final_position
							print("New value:%d"%list_players[player_id])
							continue
						elif dice[2]==6:
							print("oops 3 consecutive sixes!")
							continue
						else:
							print('something\'s wrong')	
							continue
					else:
                                		print('something\'s wrong')
						continue
				elif list_players[player_id]!=0 and dice[0]!=6:
					print('You get [{}]'.format(dice[0]))
					final_position=get_points(dice[0],0,0,list_players[player_id])
					list_players[player_id]=final_position
					print("New value:%d"%list_players[player_id])
					continue
				elif list_players[player_id]!=0 and  dice[0]==6:
					print('You get another turn!')
					dice[1]=random.randint(1,6)
					if dice[1]!=6:
						print('You get [{}][{}]  '.format(6,dice[1]))
						final_position=get_points(dice[0],dice[1],0,list_players[player_id])
						list_players[player_id]=final_position
						print("New value:%d"%list_players[player_id])
						continue
					elif dice[1]==6:
						print('2 sixes:  means another turn\n')
						dice[2]=random.randint(1,6)
						if dice[2]!=6:
							print('You get [{}][{}][{}]'.format(6,6,dice[2]))
							final_position=get_points(dice[0],dice[1],dice[2],list_players[player_id])
                                        		list_players[player_id]=final_position
							print("New value:%d"%list_players[player_id])
							continue
						else:
							print('Shucks! 3 sixes cancel, you cannot move')
							continue
					else:
                                		print('something\'s wrong')
						continue
				else:
                                	print('something\'s wrong')
					continue
			count=count+1
		k1=[]
		for k,v in list_players.items():
			if (v == 100):
				k1.append(k)
				del list_players[k]
		#order_winner=total_players-len(list_players)
		num_players=num_players-len(k1)
		for j in range(0,len(k1)):
			list_of_winners.update({k1[j]+1:count-1})
			print('[[ Player: %d DONE]]'%(k1[j]+1))
	rank=1
	#print(list_of_winners)
	for key in sorted(list_of_winners.iteritems(), key=lambda (k,v): (v,k)):
		print('Rank %d: Player %d: Steps: %d'%(rank,key[0],key[1]))
		rank=rank+1

def get_points(a,b,c,position):
	property_dict={1:38,4:14,9:31,17:7,21:42,28:84,51:67,54:34,62:19,64:60,72:91,80:99,87:36,93:73,95:75,98:79}
	original_val=position
	curr=[]
	list_dice_values=[a,b,c]
	list_temp=[]
	if b==0 and c==0:
		position=position+a
		while position in property_dict.keys():
			position=property_dict[position]
		final_position=position
		if final_position > 100 :
			print('Cannot move')
			return original_val
		else:
			return final_position
	for k in itertools.permutations(list_dice_values):
		list_temp.append(k)
	list_final=list(set(list_temp))
	for i in range(0,len(list_final)):
		curr.append(position)
	for i in range(0,3):
		for j in range(0,3):	
			temp=int(list_final[i][j])
			curr[i]=curr[i]+temp
			while curr[i] in property_dict.keys():
				curr[i]=property_dict[curr[i]]
	
	final_position=max(curr)
	newlist=curr
        newlist.sort()
	if final_position > 100:
                print('Cannot move')
		if newlist[1]<100:
			final_position=newlist[1]
			combination=curr.index(final_position)
			if final_position>original_val:
				print("Combination chosen:")
				print(list_final[combination])
				return final_position
			else:
				print('Illegitimate move: orginal value retained')
				return original_val
		elif newlist[0]<100:
			final_position=newlist[0] 
			combination=curr.index(final_position)
			if final_position>original_val:
				print("Combination chosen:")
				print(list_final[combination])
				return final_position
			else:
				print('Illegitimate move: orginal value retained')
				return original_val
		elif newlist[0]>100 and newlist[1]>100:
			return original_val
	else:
		combination=curr.index(final_position)
	 	print("Combination chosen:")
		print(list_final[combination])
                return final_position
				

def main():
	print(table_server_status())
	print()
	num=2
	get_score(num)


if __name__ == '__main__':
    main()
