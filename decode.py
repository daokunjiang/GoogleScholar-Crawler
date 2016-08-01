from bs4 import BeautifulSoup as bs

with open('xue.txt', 'r', encoding='utf-8') as f:
    doc = bs(f.read(), "lxml")
    x = doc.find_all("tr", class_="gsc_a_tr")
    len_x = len(x)
    paper_name = []
    paper_author = []
    paper_magazine = []
    paper_ref = []
    paper_pubyear = []
    for i in range(0, len_x):
        paper_name_raw = x[i].find_all(class_="gsc_a_at")
        paper_name.append(paper_name_raw[0].string)
        paper_info_raw = x[i].find_all(class_="gs_gray")
        paper_author.append(paper_info_raw[0].string)
        magazine_raw = paper_info_raw[1].contents[0]
        paper_magazine.append(magazine_raw.string)
        paper_ref_raw = x[i].find_all(class_="gsc_a_c")
        paper_ref_a = paper_ref_raw[0].contents[0].string
        if paper_ref_a == '\xa0':
            paper_ref.append('0')
        else:
            paper_ref.append(paper_ref_a)
        paper_pubyear_raw = x[i].find_all(class_="gsc_a_y")
        paper_pubyear.append(paper_pubyear_raw[0].string)
    print(paper_name)
    print(paper_author)
    print(paper_magazine)
    print(paper_ref)
    print(paper_pubyear)

    ref_year_raw = doc.find_all(id="gsc_g_x")[0]
    ref_year = []
    for year in ref_year_raw.children:
        ref_year.append(year.string)

    ref_num_raw = doc.find_all(id="gsc_g_bars")[0]
    ref_num = []
    for num in ref_num_raw.children:
        ref_num.append(num.string)

