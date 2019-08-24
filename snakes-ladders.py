#!/bin/python
import random
import itertools
import sys
import time


def get_score(num_players):
	list_of_winners={}
	count=1
	list_players={} ; total_players=num_players
	for i in range(0,num_players):
		list_players.update({ i : 0})
	property_dict={1:38,4:14,9:31,17:7,21:42,28:84,51:67,54:34,62:19,64:60,72:91,80:99,87:36,93:73,95:75,98:79}
	dice=[0,0,0]
	print('*************This is a %d player game************'%(num_players))
	while num_players>1:
		while 100 not in list_players.values():
			for i in range(0,num_players):
				player_id=list_players.keys()[i]
				time.sleep(0.75)
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
		if(rank==int(sys.argv[1])):
			print('Rank %d: Player %d: Finishes last'%(rank,list_players.keys()[0]+1))
		

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
	if(int(sys.argv[1])<2):
		print('Minimum two players are required, game exiting...')
		sys.exit(0)
	get_score(int(sys.argv[1]))


if __name__ == '__main__':
    main()
