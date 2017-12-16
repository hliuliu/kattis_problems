#tle



class node(object):
	def __init__(self,value,nxt=None):
		self.value=value
		self.next=nxt


def ll(l):
	head=node(None)
	curr=head
	for v in l:
		curr.next=node(v)
		curr=curr.next
	return head.next




n=int(raw_input())

ballons=map(int,raw_input().split())
head=ll(ballons)

count=0

while head!=None:
	curr=head
	back=None
	ht=head.value
	while curr!=None:
		if ht==curr.value:
			ht-=1
			if curr==head:
				head=head.next
			else:
				back.next=curr.next
		else:
			back=curr
		curr=curr.next
	count+=1


print count

