template <typename T>
struct node{
    node<T> *l, *r, *p;
    T key;
    int cnt;
};

template <typename T>
struct splaytree{
    node<T> *root;
    
    void update(node<T> *x){
        x->cnt = 1;
        if(x->l) x->cnt+= x->l->cnt;
        if(x->r) x->cnt+= x->r->cnt;
    }
    
    void rotate(node<T> *x){ // x goes to parent of x
        node<T> *p = x->p, *b;
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
        root = x;
    }
    
    void kth(int k){ // kth node becomes the root (0-based)
        node<T> *x = root;
        while(1){
            while(x->l && x->l->cnt > k) x = x->l;
            if(x->l) k-= x->l->cnt;
            if(!k--) break;
            x = x->r;
        }
        splay(x);
    }
    
    void insert(T key){ // The node with "key" key becomes the root
        node<T> *p = root, **pp;
        if(!p){
            node<T> *x = new node<T>;
            root = x;
            x->l = x->r = x->p = NULL, x->key = key;
            return;
        }
        while(1){
            if(key == p->key) return;
            if(key < p->key){
                if(!p->l){pp = &p->l; break;}
                p = p->l;
            }
            else{
                if(!p->r){pp = &p->r; break;}
                p = p->r;
            }
        }
        node<T> *x = new node<T>;
        *pp = x;
        x->l = x->r = NULL, x->p = p, x->key = key;
        splay(x);
    }
    
    bool find(T key){ // The node with "key" key becomes the root
        node<T> *p = root;
        if(!p) return false;
        while(p){
            if(key == p->key) break;
            if(key < p->key){
                if(!p->l) break;
                p = p->l;
            }
            else{
                if(!p->r) break;
                p = p->r;
            }
        }
        return key == p->key;
    }
    
    void remove(T key){
        if(!find(key)) return;
        node<T> *p = root;
        if(p->l){
            if(p->r){
                root = p->l; root->p = NULL;
                node *x = root; while(x->r) x = x->r;
                x->r = p->r, p->r->p = x;
                delete p; return;
            }
            root = p->l; root->p = NULL;
            delete p; return;
        }
        if(p->r){
            root = p->r; root->p = NULL;
            delete p; return;
        }
        delete p; root = NULL;
    }
    
    void interval(int l, int r){ // l to r goes to root->r->l; make sure they are not ends
        kth(l-1);
        node<T> *x = root;
        root = x->r; root->p = NULL;
        kth(r-l+1);
        x->r= root; root->p = x; root = x;
    }
};