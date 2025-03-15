#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

vector<int> findMajorElement(vector<int>& nums){
    unordered_map<int,int> count;
    int n=nums.size();
    for(int num:nums){
        count[num]++;
    }
    vector<int> result;
    for (auto it : count) {
        if (it.second > n / 3) {
            result.push_back(it.first);
        }
    }
    if (result.empty()) {
        return {-1};
    }

    return result;
}
int main(){
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i=0;i<n;i++){
        cin>>nums[i];
    }
    vector<int> result=findMajorElement(nums);
    for(int n : result){
        cout << n <<" ";
    }
    cout<<endl;
    return 0;
}