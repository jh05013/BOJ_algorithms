int main(){OJize();
    random_device RD;
    mt19937 RG(RD());
    uniform_int_distribution UID(1, 6); // from 1 to 6

    for(int i=0; i<10; i++) cout<< UID(RG);
}