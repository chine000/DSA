# Week 13

**Depth-First Search** 

![](http://alexvolov.com/wp-content/uploads/2015/02/DFS.png)

深度優先搜尋：分為遞歸與非遞歸的方式，與 BFS 相同，先將資料轉為樹或是圖形的型態，並以先深後廣之方式做訪節點。走訪時，若採用遞歸的方式，會先由起始點開始，走訪其第一個相鄰的點，並從這個分支依序走訪至結束，再返回起始點之其他節點，以相同的方式尋遍所有節點；若採用非遞歸的方式，則是由起始點開始，走訪起始點之最後一個相鄰點，並從這個分支依序走訪至結束，再返回起始點之前一個相鄰節點，以相同的方式尋遍所有節點。

**BFS 與 DFS 之比較**

BFS 與 DFS 是很相似的概念，都是循著相鄰的點一一走訪，最大的差異在於，BFS 是先將同一深度的結點走訪完，以廣度為優先走訪的順序，才再走訪下一個 level 的節點；而 DFS 不論是遞歸或是非遞歸，都是先走訪完起始點的一個相鄰分支，直到遇到死路才返回，意即以深度為優先走訪的順序。
