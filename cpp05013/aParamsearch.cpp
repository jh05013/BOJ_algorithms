int paramin(int s, int e){ // Add more parameters as you need
    int mid, ans;
    while(s <= e){
        mid = (s+e)/2;
        // Predicate here
        bool pred = true;
        // Predicate ends
        if(pred) e=mid-1, ans=mid;
        else s=mid+1;
    }
    return ans;
}

int paramax(int s, int e){ // Add more parameters as you need
    int mid, ans;
    while(s <= e){
        mid = (s+e)/2;
        // Predicate here
        bool pred = true;
        // Predicate ends
        if(pred) s=mid+1, ans=mid;
        else e=mid-1;
    }
    return ans;
}

double paraminf(double s, double e){ // Add more parameters as you need
    double mid;
    while(e-s > 1e-9){
        mid = (s+e)/2;
        // Predicate here
        bool pred = true;
        // Predicate ends
        if(pred) e=mid;
        else s=mid;
    }
    return e;
}

double paramaxf(double s, double e){ // Add more parameters as you need
    double mid;
    while(e-s > 1e-9){
        mid = (s+e)/2;
        // Predicate here
        bool pred = true;
        // Predicate ends
        if(pred) s=mid;
        else e=mid;
    }
    return e;
}