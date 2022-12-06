package spider

import (
	"fmt"
	"github.com/PuerkitoBio/goquery"
	"net/http"
)

// right now just starting with baseball
const startUrl = "https://gvsulakers.com/sports/baseball/schedule/2023"

type Spider struct {
	mainPage *goquery.Document
	years    []string
}

func GetLink(url string) (*goquery.Document, error) {
	r, err := http.Get(url)
	if err != nil {
		return nil, err
	}

	defer r.Body.Close()

	doc, err := goquery.NewDocumentFromReader(r.Body)
	if err != nil {
		return nil, err
	}
	return doc, nil
}

func (s *Spider) GetYears() error {
	doc, err := GetLink(startUrl)
	if err != nil {
		return fmt.Errorf("error getting link: %v", err)
	}

	// find dropdown menu
	dd := doc.Find("div .sidearm-schedule-select")
	fmt.Println(dd.Text())

	return nil
}
