#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7

import quandl
quandl.ApiConfig.api_key = "ENTER YOUR OWN API KEY"


#filenames, abreviations
filenames=[ "CHRIS/CME_GC1",
            "CHRIS/CME_SI1",
	    "CHRIS/CME_PA1",
	    "CHRIS/CME_HG1",
	    "CHRIS/CME_RB1",
	    "CHRIS/CME_CL1",
	    "CHRIS/CME_NG1",
	    "CHRIS/CME_LB1",
	    "CHRIS/CME_C1",
	    "CHRIS/CME_RR1",
	    "CHRIS/CME_S1",
	    "CHRIS/CME_BO1",
	    "CHRIS/CME_W1",
	    "CHRIS/CME_FC1",
	    "CHRIS/CME_LN1"]


abv=[  "gold", "silver", "palladium", "copper", "gasoline-rbob", "crude-oil",
        "natural-gas", "lumber", "us-corn", "rough-rice", "us-soybeans", "us-soybean-oil", "us-wheat",
        "feed-cattle", "lean-hog" ]

for x in range(len(filenames)):
    print(filenames[x])
    data = quandl.get(filenames[x], rows=800)
    data.to_csv(abv[x]+".csv")

#data=quandl.get(filenames[0])
#data.to_csv("testabcd.csv")
#
