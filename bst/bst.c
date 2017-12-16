
#include <stdio.h>
#include <stdlib.h>


#define MAX_N 300000



typedef struct node Node;

struct node {
	int value;
	Node *left, *right;
	int maxval,minval;
};


Node* node_by_value[MAX_N+1];

Node* root = NULL;

int depth[MAX_N+1];

int parent[MAX_N+1];

int order[MAX_N+1];

int n = -1;


Node* init_node(int el) {
	Node *ptr = (Node*)malloc(sizeof(Node));
	if (ptr!=NULL) {
		ptr -> value =  el;
		ptr -> left = ptr -> right = NULL;
		ptr -> maxval = n;
		ptr -> minval = 1;
	}
	return ptr;
}


int insert(int el, int counter) {
	int i;
	Node * parent_node, * curr_node;
	// printf("root null: %d\n", root==NULL);
	if (root==NULL) {
		root = init_node(el);
		node_by_value[el]= root;
		depth[el] = 0;
		// printf("depth[%d] =%d\n", el,depth[el]);
		for (i=1;i<=n;i++) {
			if (i!=el) {
				parent[i] = el;
			}
		}
	}else {
		parent_node = node_by_value[parent[el]];
		curr_node = init_node(el);
		node_by_value[el] = curr_node;
		if (el>parent[el]) {
			parent_node -> right = curr_node;
			curr_node -> minval = parent[el]+1;
			curr_node -> maxval = parent_node -> maxval;
		}else {
			parent_node -> left = curr_node;
			curr_node -> maxval = parent[el]-1;
			curr_node -> minval = parent_node -> minval;
		}
		depth[el] = depth[parent[el]]+1;
		// printf("depth[%d] =%d\n", el,depth[el]);
		// printf("parent[%d] =%d\n", el,parent[el]);

		for (i= curr_node -> minval; i<= curr_node -> maxval;i++) {
			if (depth[i]<0) {
				parent[i] = el;
			}
		}
		counter += depth[el];
	}
	return counter;
}

void freeall() {
	int i;
	if (root!=NULL) {
		free(root);
	}
	for (i=0;i<n;i++) {
		if(node_by_value[i]!=NULL) {
			free(node_by_value[i]);
		}
	}
}

int main(int argc, char const *argv[])
{
	scanf("%d",&n);
	int i,counter;
	counter = 0;
	for (i=0;i<=n;i++) {
		parent[i] = 0;
		depth[i] = -1;
	}
	for (i=0;i<n;i++) {
		scanf("%d",order+i);
		
		// printf("%d\n", order[i]);
		counter = insert(order[i],counter);
		printf("%d\n", counter);
	}
	// printf("%d\n",depth[1]);
	// freeall();
	return 0;
}




