class Solution {
public:
    string encode(vector<string>& strs) {
        string res;
        for (string s : strs) res += to_string(s.size()) + "#";
        res += "/";
        for (string s : strs) res += s;
        return res;
    }

    vector<string> decode(string s) {
        vector<int> lens;
        int i = 0;
        int cur = 0;
        while (s[i] != '/') {
            cur = cur * 10 + (s[i] - '0');
            i += 1;
            if (s[i] == '#') {
                lens.push_back(cur);
                cur = 0;
                i += 1;
            }
        }
        i += 1;
        vector<string> res;
        for (int len : lens) {
            res.push_back(s.substr(i, len));
            i += len;
        }
        return res;
    }
};
