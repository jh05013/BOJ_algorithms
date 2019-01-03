template <typename T>
struct Persistent{
   struct Node{T v; Node *l, *r; Node():v(0), l(NULL), r(NULL){}};
   vector<Node*> node, root;
   int width;
   Persistent(int d): width(1<<d){root.push_back(first(0, width-1));}
   Node *first(int l, int r){
       int i = node.size();
       Node* x = new Node(); node.push_back(x);
       if(l == r) return node[i];
       
       int m = (l+r)>>1;
       x->l = first(l, m);
       x->r = first(m+1, r);
       return node[i];
   }

   Node *add(Node *shadow, int y, T val, int l, int r){
       if(r<y || y<l) return shadow;
       int i = node.size();
       Node* x = new Node(); node.push_back(x);
       if(l == r){x->v = shadow->v + val; return node[i];}
       
       int m = (l+r)>>1;
       x->l = add(shadow->l, y, val, l, m);
       x->r = add(shadow->r, y, val, m+1, r);
       x->v = x->l->v + x->r->v;
       return node[i];
   }
   void add(int y, T val=1){
       int i = root.size()-1;
       root.push_back(add(root[i], y, val, 0, width-1));
   }
   
   T sum(Node *x, int l, int r, int nl, int nr){
       if(r<nl || l>nr) return 0;
       if(l<=nl && nr<=r) return x->v;
       int m = (nl+nr)>>1;
       return sum(x->l, l, r, nl, m) + sum(x->r, l, r, m+1, nr);
   }
   T sum(int t, int l, int r){return sum(root[t], l, r, 0, width-1);}
   
   int kth(Node *lx, Node *rx, int k, int nl, int nr){
       if(nl == nr) return nl;
       T ncnt = rx->l->v - lx->l->v;
       int m = (nl+nr)>>1;
       if(k <= ncnt) return kth(lx->l, rx->l, k, nl, m);
       else return kth(lx->r, rx->r, k-ncnt, m+1, nr);
   }
   int kth(int l, int r, int k){return kth(root[l-1], root[r], k, 0, width-1);}
};