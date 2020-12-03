
def createGraph(graph ,node,values):

    if len(graph.keys()) < 1:
        graph[node]=[values]
    else:

        if node in graph.keys():
            graph[node].append(values)
           # print("here in if",node)
        else:
            graph[node]=[]
            graph[node].append(values)
           # print("here in else",node)
    return(graph)


def  dfs(graph,node,vis):
        if node in graph.keys():
            vis[node]=1
            for i in graph[node]:
                if not vis[i]:
                    print(vis,i)
                    dfs(graph,i,vis)

        return vis





graph={}
graph=createGraph(graph,1,0)
graph=createGraph(graph,1,2)
graph=createGraph(graph,1,3)
graph=createGraph(graph,1,4)
graph=createGraph(graph,0,1)
graph=createGraph(graph,0,4)
graph=createGraph(graph,2,1)
graph=createGraph(graph,2,3)
graph=createGraph(graph,3,1)
graph=createGraph(graph,3,4)
graph=createGraph(graph,3,2)
graph=createGraph(graph,4,1)
graph=createGraph(graph,4,0)
graph=createGraph(graph,4,3)
print(graph)
# dic={1:"j",2:"u",3:"y"}
# for i in dic:
#     print(i)
print(dfs(graph,3,[0]*len(graph)))
