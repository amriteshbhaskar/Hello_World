def partition(a,l,h):
	p=a[h]
	t=l-1
	for i in range(l,h+1):
		if a[i]<p:
			t+=1
			a[t],a[i]=a[i],a[t]
	a[t+1],a[h]=a[h],a[t+1]
	return t+1


def quicksort(a,l,h):
	if l<h:
		
