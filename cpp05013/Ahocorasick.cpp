const int ALPHA = 26;
struct Node{
    bool end = false, root;
    Node *fail = nullptr, *out = nullptr;
    Node *nxt[ALPHA]; 
    Node(bool root = false): root{root} {fill(nxt, nxt+ALPHA, nullptr);}
    ~Node(){for(int i=0; i<ALPHA; i++) if(nxt[i]) delete nxt[i];}
};

struct Trie{
    int tonum(char c){return c - 'a';}
    
    Node* root = new Node(true);
    bool labeled = false;
    void kill(){delete root;}
    void add(string& s){
        Node* n = root;
        for(char& c: s){
            int x = tonum(c);
            if(!n->nxt[x]) n->nxt[x] = new Node();
            n = n->nxt[x];
        }
        n->end = true;
    }
    void label(){
        queue<Node*> Q; Q.push(root);
        while(!Q.empty()){
            Node *p = Q.front(); Q.pop();
            for(int i=0; i<ALPHA; i++) if(p->nxt[i]){
                Node *pp = p, *q = p->nxt[i];
                while(1){
                    if(pp->root){q->fail = pp; break;}
                    if(pp->fail->nxt[i]){q->fail = pp->fail->nxt[i]; break;}
                    pp = pp->fail;
                }
                Q.push(q);
            }
            if(p->root) continue;
            else if(p->end) p->out = p;
            else if(p->fail->out) p->out = p->fail->out;
        }
    }
    int aho(string& s){
        if(!labeled) labeled = true, label();
        Node *p = root; size_t i = 0;
        while(i <= s.size()){
            if(p->out) return 1; // change this as you need
            if(i == s.size()) break;
            int c = tonum(s[i]);
            if(p->nxt[c]) p = p->nxt[c], i++;
            else if(p->root) i++;
            else p = p->fail;
        }
        return 0; // change this as you need
    }
};