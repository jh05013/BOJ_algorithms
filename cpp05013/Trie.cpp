const int ALPHA = 26;
struct Node{
    bool end = false, root;
    Node *nxt[ALPHA]; 
    Node(bool root = false): root{root} {fill(nxt, nxt+ALPHA, nullptr);}
    ~Node(){for(int i=0; i<ALPHA; i++) if(nxt[i]) delete nxt[i];}
};

struct Trie{
    int tonum(char c){return c - 'a';}
    Node *root = new Node(true);
    void kill(){delete root;}
    void add(string& s){
        Node *n = root;
        for(char& c: s){
            int x = tonum(c);
            if(!n->nxt[x]) n->nxt[x] = new Node();
            n = n->nxt[x];
        }
        n->end = true;
    }
};