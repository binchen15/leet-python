import (
    "fmt"
)

func multiply(num1 string, num2 string) string {
    
    arr1 := []byte(num1)
    arr2 := []byte(num2)
    n1 := len(arr1)
    n2 := len(arr2)
    arr := make([]byte, n1+n2)
    
    // zero := '0'
    var a, b, p, tmp byte
    for j := n2-1; j >= 0; j-- {
        b = arr2[j] - '0' 
        for i := n1-1; i >= 0; i-- {
            a = arr1[i] - '0'
            p = a * b
            tmp = p + arr[i+j+1]
            arr[i+j], arr[i+j+1] = tmp/10 + arr[i+j], tmp%10 
        }
    }
    
    for i := 0; i < n1+n2; i++ {
        arr[i] += '0'
    }
    
    i := 0
    for i < n1+n2-1 && arr[i] == '0' {
        i += 1
    }
    return string(arr[i:])
}
