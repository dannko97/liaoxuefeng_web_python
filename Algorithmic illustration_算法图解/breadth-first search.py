from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'find the mango seller {person} !')
                return
            else:
                search_deque += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == 'm'


search('you')