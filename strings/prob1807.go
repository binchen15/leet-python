import (
    "strings"
)

func evaluate(s string, knowledge [][]string) string {

    dict := map[string]string{}

    for _, list := range knowledge {
        key, value := list[0], list[1]
        dict[key] = value
    }

    ans := []string{}

    flag := false  // key mode
    var key []string
    for _, char := range s {
        if char != '(' && char != ')' {
            if !flag {
                ans = append(ans, string(char))
            } else {
                key = append(key, string(char))
            }
        } else if char == '(' {
            flag = true
            key = []string{}
        } else if char == ')' {
            token := strings.Join(key, "")
            val, ok := dict[token]
            if !ok {
                ans = append(ans, "?")
            } else {
                ans = append(ans, val)
            }
            flag = false
        }
    }

    return strings.Join(ans, "")

}

