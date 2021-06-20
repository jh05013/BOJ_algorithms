const int SKIP_HEIGHT = 20;
int gen_height(){
    int h = 1;
    while(h < SKIP_HEIGHT && (rand()&1)) h++;
    return h;
}

template<typename T>
struct SkipNode{
    int h;
    vector<SkipNode<T>*> nexts;
    bool is_valid;
    T val;
    SkipNode(int H): h{H}, nexts(H), is_valid(false) {}
    SkipNode(int H, T V): h{H}, nexts(H), is_valid(true), val(V) {}
    SkipNode* nxt(){return nexts[0];}
};

template<typename T>
struct LayeredLookup{
    vector<SkipNode<T>*> ptrs;
    
    SkipNode<T>* operator[](size_t i){return ptrs[i];}

    void insert_after(T val){
        int h = gen_height();
        SkipNode<T> *node = new SkipNode<T>(h, val);
        for(int i=0; i<h; i++){
            SkipNode<T> *l = ptrs[i];
            node->nexts[i] = l->nexts[i], l->nexts[i] = node;
        }
    }

    void remove_after(){
        SkipNode<T> *targ = ptrs[0]->nxt();
        if(!targ->is_valid) return;
        for(int i=0; i<sz(targ->nexts); i++)
            ptrs[i]->nexts[i] = targ->nexts[i];
    }
};

template <typename T>
struct SkipList{
    SkipNode<T> *head, *tail;
    SkipList():
        head(new SkipNode<T>(SKIP_HEIGHT)), tail(new SkipNode<T>(SKIP_HEIGHT)){
        fill(entire(head->nexts), tail);
    }

    vector<T> to_list(){
        vector<T> L;
        SkipNode<T> *ptr = head->nxt();
        while(ptr != tail) L.push_back(ptr->val), ptr = ptr->nxt();
        return L;
    }

    ////////////////////////// Search

    // last node such that pred(node), or head if it doesn't exist.
    LayeredLookup<T> layered_last(function<bool(SkipNode<T>*)> pred){
        LayeredLookup<T> nodes;
        SkipNode<T> *ptr = head;
        for(int i=SKIP_HEIGHT-1; i>=0; i--){
            while(1){
                SkipNode<T> *nxt = ptr->nexts[i];
                if(nxt == tail || !pred(nxt)) break;
                ptr = nxt;
            }
            nodes.ptrs.push_back(ptr);
        }
        reverse(entire(nodes.ptrs));
        return nodes;
    }

    SkipNode<T>* last(function<bool(SkipNode<T>*)> pred){
        SkipNode<T> *ptr = head;
        for(int i=SKIP_HEIGHT-1; i>=0; i--){
            while(1){
                SkipNode<T> *nxt = ptr->nexts[i];
                if(nxt == tail || !pred(nxt)) break;
                ptr = nxt;
            }
        }
        return ptr;
    }

    // last node that is <= val, or head if it doesn't exist,
    // assuming sorted in increasing order.
    LayeredLookup<T> layered_last_le(T val){
        return layered_last([&](SkipNode<T> *node){return node->val <= val;});
    }
    LayeredLookup<T> layered_last_lt(T val){
        return layered_last([&](SkipNode<T> *node){return node->val < val;});
    }
    SkipNode<T>* last_le(T val){
        return last([&](SkipNode<T> *node){return node->val <= val;});
    }
    SkipNode<T>* last_lt(T val){
        return last([&](SkipNode<T> *node){return node->val < val;});
    }
    // first node that is >= val, or tail if it doesn't exist, assume sorted.
    SkipNode<T>* first_ge(T val){return last_lt(val)->nxt();}
    SkipNode<T>* first_gt(T val){return last_le(val)->nxt();}

    ////////////////////////// Insert

    void insert_first(T val){
        int h = gen_height();
        SkipNode<T> *node = new SkipNode<T>(h, val);
        for(int i=0; i<h; i++){
            SkipNode<T> *l = head;
            SkipNode<T> *r = l->nexts[i];
            l->nexts[i] = node, node->nexts[i] = r;
        }
    }

    // insert val.
    // if allow_duplicate, insert even if val already exists.
    void insert_inc(T val, bool allow_duplicate = true){
        LayeredLookup<T> nodes = layered_last_le(val);
        if(!allow_duplicate){
            SkipNode<T>* node = nodes[0];
            if(node->is_valid && node->val == val) return;
        }
        nodes.insert_after(val);
    }

    ////////////////////////// Remove

    // remove val.
    // if allow_inexact, remove the first node >= val.
    void remove_inc(T val, bool allow_inexact = true){
        LayeredLookup<T> nodes = layered_last_lt(val);
        SkipNode<T> *targ = nodes[0]->nxt();
        if(!targ->is_valid) return;
        if(!allow_inexact && targ->val != val) return;
        for(int i=0; i<sz(targ->nexts); i++)
            nodes[i]->nexts[i] = targ->nexts[i];
    }
};