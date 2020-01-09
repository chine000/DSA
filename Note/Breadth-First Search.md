# Week 12

**Breadth-First Search** 

![](http://alexvolov.com/wp-content/uploads/2015/02/bfs_2_lvl.png)

廣度優先搜尋：通常會將資料轉為樹或是圖形的型態，從起始點開始，先廣後深地一一走訪相鄰且未走訪過的節點，直到尋遍所有節點為止，使用 queue 使資料先進先出。走訪時將起始點設為 level 0，走訪其相鄰的點並設為 level 1，將 level 1 走訪完畢並設其相鄰點為 level 2，以此類推，直至所有節點走訪完畢。
