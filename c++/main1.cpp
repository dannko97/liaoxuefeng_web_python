#include <iostream>
#include <fstream>
#include <string>
using namespace std;



#define INF 65535
int n,m,s,t;
int cost[][],dis[],vis[],p[];

void Dijkstra(int src)  // src传入的起点
{
    for (int i=0; i<m; i++)  // 初始化起点到所有点的距离
    {
        dis[i] = cost[src][i];
        vis[i] = 0;
        p[i] = 0;
    }
    dis[src] = 0; //到自身距离为0
    vis[src] = 1; //标记 src = 0
    for (int i = 0; i < m; ++i) {
        int ans = INF, k;
        for (int j = 0; j < m; ++j) {
            // 寻找未被访问过距离起点最近的
            if (!vis[j] && dis[j] < ans)
            {
                k = j;
                ans = dis[j];
            }
        }
        vis[k] = 1; // 标记已访问
        if(ans == INF)
            break; // 表示剩下所有点都不通
        for (int j = 0; j < m; ++j) {
            // 松弛操作，更新起点到所有未访问点的距离
            if (!vis[j] && dis[k] + cost[k][j]<dis[j])
            {
                dis[j] = dis[k] + cost[k][j];
                p[j] = k; // 存储前驱节点
            }
        }
    }
}




int main() {
    // 读入net.in
    fstream infile;
    infile.open("net.in", ios::in);
    if (!infile.is_open())
    {
        cout << "fail to open file" << endl;
        return 0;
    }

    infile >> n >> m >> s >> t;
    cout << n << m << s << t << endl;





    return 0;
}
