template <typename T>
struct node{
    node<T> *l, *r, *p;
    int cnt;
    T lazy;
    // define some properties here
};

template <typename T>
struct splaytree{
    node<T> *root;
    
    splaytree<T>(int n){
        node<T> *x;
        root = x = new node<T>;
        x->l = x->r = x->p = NULL;
        x->cnt = n;
        // initialize some properties here
        for(int i=1; i<n; i++){
            x->r = new node<T>;
            x->r->p = x; x = x->r;
            x->l = x->r = NULL;
            x->cnt = n-i;
            // initialize some properties here
        }
    }
    
    void update(node<T> *x){
        x->cnt = 1;
        // initialize some properties here
        if(x->l){
            x->cnt+= x->l->cnt;
            // update some properties here
        }
        if(x->r){
            x->cnt+= x->r->cnt;
            // update some properties here
        }
    }
    
    void unlazy(node<T> *x){
        // apply unlazy properties to x
        if(x->l){
            x->l->lazy+= x->lazy;
            // apply lazy properties to x->l
        }
        if(x->r){
            x->r->lazy+= x->lazy;
            // apply lazy properties to x->r
        }
        x->lazy = 0;
    }
    
    void rotate(node<T> *x){ // x goes to parent of x
        node<T> *p = x->p, *b;
        unlazy(p); unlazy(x);
        if(x == p->l) p->l = b = x->r, x->r = p;
        else p->r = b = x->l, x->l = p;
        x->p = p->p, p->p = x;
        if(b) b->p = p;
        (x->p ? p == x->p->l ? x->p->l : x->p->r : root) = x;
        update(p); update(x);
    }
    
    void splay(node<T> *x){ // x becomes the root
        while(x->p){
            node<T> *p = x->p, *g = p->p;
            if(g) rotate((x == p->l) == (p == g->l) ? p : x);
            rotate(x);
        }
    }
    
    void kth(int k){ // kth node becomes the root (0-based)
        node<T> *x = root; unlazy(x);
        while(1){
            while(x->l && x->l->cnt > k) x = x->l, unlazy(x);
            if(x->l) k-= x->l->cnt;
            if(!k--) break;
            x = x->r, unlazy(x);
        }
        splay(x);
    }

    void interval(int l, int r){ // l to r goes to root->r->l; make sure they are not ends
        kth(l-1);
        node<T> *x = root;
        root = x->r; root->p = NULL;
        kth(r-l+1);
        x->r= root; root->p = x; root = x;
    }
};