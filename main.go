package main

import "github.com/GVSU-Sports-Analytics/GV-Crawler/spider"

func main() {
	s := spider.Spider{}
	err := s.GetYears()
	if err != nil {
		return
	}
}
