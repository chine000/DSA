# Heep Sort

![](https://1.bp.blogspot.com/-5WRKOWTm3NM/W--3ORaY2LI/AAAAAAAEHLw/wbZf81L8bBYZHZR6stpCTbfptMTkMaAKgCLcBGAs/s1600/2018_11_17_heap.png)

堆積排序法：將一個數列排成完全二元樹，每一個父節點必須大於兩個子節點，形成 Max Heap，將第一個節點與最後一個節點交換，此時最後一個節點為最大的數並以排列完成，忽略最後一個節點重複前面步驟，直至數列排列完成。

   ```
   Min Heap：頂層節點數值必定大於下層的二元樹
   Max Heap：頂層節點數值必定小於下層的二元樹
   Heapify：將一個數列排成完全二元樹
   ```
   
# Merge Sort

![](https://kopu.chat/wp-content/uploads/2017/08/merge.gif)

合併排序法：將一個數列不斷對半分成兩個小數列，直至每一個小數列剩下一個元素為止，再將小數列倆倆排序後合併至最後的排序完成數列。

- 6 2 9 5 對半分，6 2、9 5 再對半分。
- 6、2 排序後合併，9、5 排序後合併。
- 2 6、5 9 排序後合併。
