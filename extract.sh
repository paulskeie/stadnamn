grep app:langnavn Basisdata_0000_Norge_25833_Stedsnavn_GML.gml |cut -d ">" -f 2|cut -d "<" -f 1 > stadnamn.csv
