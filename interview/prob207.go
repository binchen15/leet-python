func canFinish(numCourses int, prerequisites [][]int) bool {
    
    m := len(prerequisites)
    if m == 0 {
        return true
    }

    // count prerequsites of each course
    inDegree := make([]int, numCourses)

    hmap := map[int][]int{}
    for _, pair := range prerequisites {
        course, pre := pair[0], pair[1]
        inDegree[course] += 1
        list, ok := hmap[pre]
        if ! ok {
            hmap[pre] = []int{course}
        }
        hmap[pre] = append(list, course)
    }

    queue := []int{}

    for i := 0; i < numCourses; i++ {
        if inDegree[i] == 0 {
            queue = append(queue, i) 
        }
    }

    remain := numCourses
    var course int
    for len(queue) > 0 {
        queue, course = queue[1:len(queue)], queue[0] 
        remain -= 1
        list, ok := hmap[course]
        if ok {
            for _, tmp := range list{
                inDegree[tmp] -= 1
                if inDegree[tmp] == 0 {
                    queue = append(queue, tmp)
                }
            }
        }

    }

    return remain == 0

}
