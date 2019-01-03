template <typename T>
struct MedianHeap{
    priority_queue<T> minh;
    priority_queue<T, vector<T>, greater<T>> maxh;
    
    bool empty(){return minh.empty() && maxh.empty();}
    T top(){
        if(empty()) throw;
        if(minh.size() >= maxh.size()) return minh.top();
        return maxh.top();
    }
    void rebalance(){
        while(minh.size() > maxh.size()+1) maxh.push(minh.top()), minh.pop();
        while(maxh.size() > minh.size()+1) minh.push(maxh.top()), maxh.pop();
    }
    void push(T v){
        if(empty() || v > top()) maxh.push(v);
        else minh.push(v);
        rebalance();
    }
    T pop(){
        T m = top();
        if(minh.top() == m) minh.pop();
        else maxh.pop();
        rebalance();
        return m;
    }
};