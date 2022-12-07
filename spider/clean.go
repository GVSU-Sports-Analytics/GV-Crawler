package spider


import "strings"


func CleanText(str string) string {
	return strings.ReplaceAll(str, " ", "")
}
