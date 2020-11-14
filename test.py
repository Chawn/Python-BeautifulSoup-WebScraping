import re

txt = """<tr onclick="window.open(&#39;asset_open.asp?law_suit_no=8274&amp;law_suit_year=2551&amp;Law_Court_ID=039&amp;deed_no=171367&amp;addrno=-&#39;,null,&#39;width=1300,height=900,status=yes,toolbar=no,menubar=yes,location=no,scrollbars=yes,resizable=yes&#39;); return false;"> """
matches = re.findall("deed_no=.+&amp;", txt)[0]
matches = matches.replace("deed_no=","")
matches = matches.replace("&amp;","")
print(matches)