

## Toys

### Problem Description: https://open.kattis.com/problems/toys


### Solution:

Here, we want to fix $K$ and let $T$ vary over the positive integers.
Let $f(T)$ denote the solution for $T$ toys.
Notice that $f(T)\in \{0,1,2,...,T-1\}$ and $f(1)=0$.
Consider when $T>1$. Once the child removes the toy at position $K-1$, 
she has to continue the same game with only $T-1$ toys, except that she begins at toy $K \mod T$ instead of toy 0.
We can view this as an offset and relabel the toy positions consistently so the labels maintain the same orientation with the game starting at toy 0.
The relabeling is, $\mod T$, as follows: $K\to 0$, $K+1\to 1$, ..., $T-1 \to T-K-1$, $0 \to T-K$, ..., $K-2 \to T-2$.
The remaining goal is to calculate $f(T-1)$ wrt the relabelled toys. To recover the original label to toy $i$ wrt to the new labelling, we can compute 
$i+K \mod T$. 
Thus, $f(T)=f(T-1)+K \mod T$.

We now have a recurrence relation for $f(T)$. Based on the input side, evaluating $f(T)$ recursively top down take too much overhead.
Instead, we evaluate $f(T)$ iteratively bottom up. We initialize a variable $x$ to be $f(1)=0$ and update $x$ in a loop. At the beginning of the $i$-th iteration,
$x$ would be $f(i)$, so we require a total of $T-1$ interations.

