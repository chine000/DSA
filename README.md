# Content

- Homework：
   * [HW1 - Quick Sort](https://github.com/chine000/DSA/tree/master/HW1)
   * [HW2 - Merge Sort & Heap Sort](https://github.com/chine000/DSA/tree/master/HW2)
   * [HW3 - BST](https://github.com/chine000/DSA/tree/master/HW3)
   * [HW4 - Hash Table](https://github.com/chine000/DSA/tree/master/HW4)
   * [HW5 - BFS & DFS](https://github.com/chine000/DSA/tree/master/HW5)
   * [HW6 - Dijkstra & Kruskal](https://github.com/chine000/DSA/tree/master/HW6)
- Leetcode：

- My Learning Note：
   * [Week 1](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 2](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 3](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 4](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 5](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 6](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 7](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 8](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 9](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 10](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 11](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 12](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 13](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 14](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 15](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 16](https://github.com/chine000/DSA/blob/master/README.md)
   * [Week 17](https://github.com/chine000/DSA/blob/master/README.md)




# About Me

 ```
 巨資三B 金元萱
 1999/05/26 出生
 誤打誤撞進了巨資系
 背誦能力強邏輯爛的文組生
 那一學期學了什麼就會比較熟悉那個程式語言
 所以這學期最熟悉的就是 python
 ```

# After Learning DSA
原本的我是很討厭程式語言的，大部分的課程都是跟著老師打程式碼，不清楚自己有沒有懂，不清楚自己學這些做什麼，只牢牢記住考試會考哪些。

因為都是為了要應付考試，而程式卻是必須去深入學習、嘗試，才能慢慢領悟進步的一門學問，所以過去的我面對程式設計課總是心很累頭很痛，一知半解卻要強迫自己記起來其實是最累的。

後來接觸了這門課後，一開始聽說要先自己寫題目真的很痛苦，程式基礎本來就不好，之前學的也都忘光了，那時在練習 codesignal 時連 return 是什麼都不知道，卻沒想到真正崩潰的部分在後面。

進入了個人作業期，第一次作業：Quick Sort，那時跟同學一起討論，雖然概念都是看網路上的，卻慢慢對於 python 的基本格式熟悉了一點，最後分數很低讓我有點對於這堂課的硬度無所適從。到了第二次作業：Merge Sort & Heap Sort，依然還是被判定與同學、參考資料高度相似，但那時我已經很努力地加入我能想到的所有點子了，雖然分數沒起色還是對於自己小小的進步感到開心。第三次作業：BST，是我真正大幅進步的一次作業，開始自己著手寫程式碼，用自己的想法設計迴圈、判斷式，還寫出了高達 300 多行的程式碼。

後來的作業對我來講都相對輕鬆，這時的我已經不是只會跟著老師打程式碼的學生了，我也可以寫出屬於自己的程式碼，即使這門課曾讓我生氣到想退選，也曾讓我崩潰到無法顧及其他科目，最終這學期使我收穫最多的還是這門課，還是謝謝老師的堅持與後來的教法改變，讓我們在課堂上能學習到知識，而不是只能自己回家自學。
另外，對於作業的評分機制還是有些小小不平，畢竟自己從一開始到最後的作業都是用盡全力的寫，還是因為遲交、被判抄襲等原因被扣了許多分數，還是希望未來關於作業溝通的部分不要只有信箱，其實用 line 群組公告事項以及問題詢問會更為快速，也會減少學生對於作業理解的誤會。

# My Learning Note


## Week 1

中秋節放假  

## Week 2 

**Linked List & Array**

   ![](https://miro.medium.com/max/1732/1*aeJZmbE3xBDZfYOu6p5CPw.png)

- Linked List：由節點（node）組成資料，再由pointer指向下一個節點，藉此串連起來，以null表達終點，可以不連續的資料型態儲存在記憶體中。
   * 優點：可利用記憶體中零散空間，需要多少就使用多少
   * 缺點：無法隨機存取、查詢，需走訪各節點

- Array：以連續的資料型態儲存在記憶體中。
   * 優點：使用容易
   * 缺點：刪除與插入資料較為麻煩、浪費不必要的記憶體空間
   
## Week 3

**Stack & Queue**

![](https://www.thecrazyprogrammer.com/wp-content/uploads/2016/05/Difference-Between-Stack-and-Queue.jpg)

- Stack：資料以堆疊的方式呈現（疊盤子），先進後出，例子：undo，回上一頁。
   * Push：放資料進Stack
   * Pop：將最上面資料移除
   * Top：讀取最上面資料
   * IsEmpty：確認Stack裡是否有資料
   * getSize：回傳羅馬資料個數

- Queue：資料以排列方式呈現（排隊），先進先出，例子：CPU、印表機，一次照順序執行一個需求。
   * Push：放資料進Queue
   * Pop：將最前面資料移除，又稱Dequeue
   * getFront：讀取第一筆資料
   * getBack：讀取最後一筆資料
   * IsEmpty：確認Queue裡是否有資料
   * getSize：回傳資料個數

## Week 4

**Set Mismatch**

- 題目：一個list為[1,2,3,3,3,5]，排出缺失值與重複值。
- 構想：先設一個holder=[0,0,0,0,0,0]，其位置i分別為0,1,2,3,4,5，將list依序填入holder，holder中list[i＝0]-1為0＝holder[0]=list[0]=1，依序檢驗，重複值為3，缺失值為holder.index(0)+1=4。

**Leetcode | Roman to Integer**

- 題目：指定數字為羅馬符號，依照題目給的符號跑出對應數字。
- 構想：先將羅馬符號指定為對應數字{'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}，設定i位置從0至符號個數-1，以符號第i位小於或大於i+1位做判別。 


**Insertion Sort**

- Insertion Sort：將資料以左至右依序檢視，由第一筆開始插入以排序好之資料，插入時以右至左檢視資料。
> `6` 5 3 1 8 7 2 -> 6 `5` 3 1 8 7 2 -> 5 6 `3` 1 8 7 2 -> 3 5 6 `1` 8 7 2 以此類推 
- bubble sort：將資料由左至右兩兩相互比較、交換位子，最後一位則為已排序好之資料，再從頭開始至全部資料排序結束。
> `6` `5` 3 1 8 7 2 -> 5 `6` `3` 1 8 7 2 -> 5 3 `6` `1` 8 7 2 以此類推
- quick sort：在資料中找基準點，以基準點將資料分為兩堆，在兩堆中繼續找基準點分為四堆，直至排序完成。
   * n*1/2**x＝1 -> log2n=x.
> 6 5 `3` 1 8 7 2 -> 1 2 `3` 6 5 8 7 -> `1` 2 3 6 5 8 `7` -> 1 2 3 6 5 `7` 8 以此類推

## Week 5

國慶日放假


## Week 6

**Heep Sort**

![](https://1.bp.blogspot.com/-5WRKOWTm3NM/W--3ORaY2LI/AAAAAAAEHLw/wbZf81L8bBYZHZR6stpCTbfptMTkMaAKgCLcBGAs/s1600/2018_11_17_heap.png)

堆積排序法：將一個數列排成完全二元樹，每一個父節點必須大於兩個子節點，形成 Max Heap，將第一個節點與最後一個節點交換，此時最後一個節點為最大的數並以排列完成，忽略最後一個節點重複前面步驟，直至數列排列完成。

   ```
   Min Heap：頂層節點數值必定大於下層的二元樹
   Max Heap：頂層節點數值必定小於下層的二元樹
   Heapify：將一個數列排成完全二元樹
   ```
## Week 7

**Merge Sort** 

![](https://kopu.chat/wp-content/uploads/2017/08/merge.gif)

合併排序法：將一個數列不斷對半分成兩個小數列，直至每一個小數列剩下一個元素為止，再將小數列倆倆排序後合併至最後的排序完成數列。

- 6 2 9 5 對半分，6 2、9 5 再對半分。
- 6、2 排序後合併，9、5 排序後合併。
- 2 6、5 9 排序後合併。

## Week 8

**Binary Tree**

![](https://pic.pimg.tw/emn178/1354416914-2701915548_n.png)

二元樹：將數列排成每個節點最多只有兩個分支的樹結構。通常分支被稱作「左子樹」或「右子樹」，具有左右次序，不能隨意顛倒。

## Week 9

**Binary Search Tree** 

![](https://cdn.softwaretestinghelp.com/wp-content/qa/uploads/2019/08/1-sample-BST.png)

二元搜尋樹：將數列排成完全二元樹，一個父節點最多有兩個子節點，父節點大於左子節點、小於右子節點，每一個節點會指向下一個節點，最後一個節點會指向 None，以這個條件去執行新增、查詢、刪除，以及修改節點的功能。

- insert：若要新增一個值至 BST ，會由上往下循著去與每一個父節點與子節點比較大小，最終此值會放在 BST 的最尾端（不會有子節點），而並非在中途插入新增。
- search：若要查詢 BST 中的一個值，首先必須先確定此值有無在 BST 中，有的話可由上往下循著去與每一個父節點與子節點比較大小去找到此值。
- delete：若要刪除 BST 中的一個值，首先必須先確定此值有無在 BST 中，有的話可由上往下循著去與每一個父節點與子節點比較大小去找到此值，要將此值刪除，須先注意此值有無子節點，若沒有孩子，須將此值的父節點指向 None，若有孩子，須將此值的父節點指向此值的孩子，並將 BST 中的第一個父節點替換成此值的右子節點中的最小值，要注意的是，有重複之值必須重複刪除。
- modify：若要將 BST 中的一個值修改成另一個值，先進行刪除的動作，接下來再新增，刪除了幾個重複的值，就必須新增幾個新的值。

## Week 10

**Red Black Tree** 

 ![](https://yotsuba1022.gitbooks.io/data-structure-note/assets/rbtree-2.png)

紅黑樹：為增加了某些特性的二元搜尋樹，在每個節點增加一個屬性表示節點顏色，值為紅色或者黑色。它可以保持樹的大致平衡，在插入或刪除節點的時候,，檢查是否破壞了樹的特性，若破壞了則進行糾正，進而保持樹的平衡。

- 每個節點不是紅就是黑的。
- 根是黑色的。
- 若節點是紅色的，則其子節點必為黑色，反之不必為真。
- 每個空子節點都是黑色的。
- 從根節點到葉節點或空子節點的每條路徑，必須包含相同數目的黑色節點。

## Week 11

**Hash Table** 

![](https://i.imgur.com/D85eZMz.png)

雜湊表：將資料先透過雜湊函式加密後取得數字，並除以欲分出的堆數（幾個櫃子），取餘數為第幾類（第幾個櫃子），若兩筆資料的餘數相同則必須擺進同一個櫃子，此狀況為發生了「碰撞」，較後進入 Hash Table 的資料一般都是以 linked list 或 BST 的型態接在上一筆資料後面。

   ```
   Hash Function：將大量的資料壓縮變小成雜湊值，並固定格式，具唯一性不易發生碰撞為較好的雜湊函示，也就是一個櫃子只放一筆資料，這時 Hash Table 的時間複雜度會比較小，另外，雜湊函式同時具有保護資料的特性。
   ```
   
## Week 12

**Breadth-First Search** 

![](http://alexvolov.com/wp-content/uploads/2015/02/bfs_2_lvl.png)

廣度優先搜尋：通常會將資料轉為樹或是圖形的型態，從起始點開始，先廣後深地一一走訪相鄰且未走訪過的節點，直到尋遍所有節點為止，使用 queue 使資料先進先出。走訪時將起始點設為 level 0，走訪其相鄰的點並設為 level 1，將 level 1 走訪完畢並設其相鄰點為 level 2，以此類推，直至所有節點走訪完畢。

## Week 13

**Depth-First Search** 

![](http://alexvolov.com/wp-content/uploads/2015/02/DFS.png)

深度優先搜尋：分為遞歸與非遞歸的方式，與 BFS 相同，先將資料轉為樹或是圖形的型態，並以先深後廣之方式做訪節點。走訪時，若採用遞歸的方式，會先由起始點開始，走訪其第一個相鄰的點，並從這個分支依序走訪至結束，再返回起始點之其他節點，以相同的方式尋遍所有節點；若採用非遞歸的方式，則是由起始點開始，走訪起始點之最後一個相鄰點，並從這個分支依序走訪至結束，再返回起始點之前一個相鄰節點，以相同的方式尋遍所有節點。

**BFS 與 DFS 之比較**

BFS 與 DFS 是很相似的概念，都是循著相鄰的點一一走訪，最大的差異在於，BFS 是先將同一深度的結點走訪完，以廣度為優先走訪的順序，才再走訪下一個 level 的節點；而 DFS 不論是遞歸或是非遞歸，都是先走訪完起始點的一個相鄰分支，直到遇到死路才返回，意即以深度為優先走訪的順序。

## Week 14

**Minimum Spanning Tree**

Kruskal：以節點建圖，並以增加邊為主軸的演算法。首先將所有的邊依權重大小排序，從權重最小的邊開始增加，若要形成邊的兩端節點未在同一條連通的邊上即可加入，每次要加入一條邊便需檢查有無可能形成 loop，確保圖形為非封閉而是有開口的，最終連完所有節點、增加了點個數 +1 條邊即完成。

## Week 15

**Shortest Path**

Dijkstra：以某一節點為起始點，最後計算出起始點至各點的最短路徑之演算法。首先以某一節點作為起始點，在與其相連且未被選取的節點裡，選擇一個離出發點距離最短的節點新增，由於新增節點的邊之權重可能會影響目前起始點到各點的距離，因此每次新增一個節點，必須確保起始點到達其他節點的距離為最短路徑，如此重覆加入新節點，直到所有的節點都被加入為止即完成。

## Week 16

期末考說明

## Week 17

提早回家投票放假
