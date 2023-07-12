import matplotlib.pyplot as plt
from wordcloud import WordCloud
text = '''Hong Kong's HSBC Allows Customers to Trade Bitcoin, Ether ETFs but That's Not Really News https://coindesk.com/business/2023/06/26/hong-kongs-hsbc-allows-customers-to-trade-bitcoin-ether-etfs-but-thats-not-really-news/… via        @coindesk $NIO in HKEX closed up over 8%. Now let's see what NYSE will do! #NIO @NIOGlobal
HSBC Hong Kong telah memulai menyediakan pelanggan membeli dan menjual bitcoin dan ethereum exchange-traded funds (ETF) yang terdaftar di bursa saham Hong Kong (HKEX).
KPMG’s Pat Woo and Irene Chu discussed the impact on the Real Estate sector of the ISSB standards S1 and S2 during an exclusive roundtable. They explored ESG reporting, the implementation of the standards after a HKEX consultation and their impact starting in 2024.

#Realestate
Don't delay - late deadline 7th July! In-house teams & professionals can enter the APACD Awards, which recognise in-house comms excellence now. Previous winners of the In-House Communications Team of the Year award include Lenovo, LinkedIn and HKEX.
Beijing Stock Exchange (#BSE) and Hong Kong Exchanges and Clearing Limited (#HKEX) inked a memorandum of understanding (#MOU) to support dual listing of stocks of each other's qualified listed companies in #Beijing on Thursday.#Xinhuasilkroadnews
https://en.imsilkroad.com/p/334839.html
Everyone is talking about chip restrictions on China forming a choke hold, no one s talking about capital market restrictions

Take a look at HKex trading volumes, that’s having much larger impact on china’s competitiveness in the future than any chip sanctions..
Crypto ETFs debuted on the HKEX with the listing of the CSOP Bitcoin Futures ETF (3066) and CSOP Ether Futures ETF (3068).

Hong Kong's HSBC Allows Customers to Trade Bitcoin, Ether ETFs but That's Not Really News https://coindesk.com/business/2023/06/26/hong-kongs-hsbc-allows-customers-to-trade-bitcoin-ether-etfs-but-thats-not-really-news/… via        
@coindesk
$NIO in HKEX closed up over 8%. Now let's see what NYSE will do! 

#NIO
@NIOGlobal
HSBC Hong Kong telah memulai menyediakan pelanggan membeli dan menjual bitcoin dan ethereum exchange-traded funds (ETF) yang terdaftar di bursa saham Hong Kong (HKEX).
KPMG’s Pat Woo and Irene Chu discussed the impact on the Real Estate sector of the ISSB standards S1 and S2 during an exclusive roundtable. They explored ESG reporting, the implementation of the standards after a HKEX consultation and their impact starting in 2024.

#Realestate
Don't delay - late deadline 7th July! In-house teams & professionals can enter the APACD Awards, which recognise in-house comms excellence now. Previous winners of the In-House Communications Team of the Year award include Lenovo, LinkedIn and HKEX.
Beijing Stock Exchange (#BSE) and Hong Kong Exchanges and Clearing Limited (#HKEX) inked a memorandum of understanding (#MOU) to support dual listing of stocks of each other's qualified listed companies in #Beijing on Thursday.#Xinhuasilkroadnews
https://en.imsilkroad.com/p/334839.html
Everyone is talking about chip restrictions on China forming a choke hold, no one s talking about capital market restrictions

Take a look at HKex trading volumes, that’s having much larger impact on china’s competitiveness in the future than any chip sanctions..
Crypto ETFs debuted on the HKEX with the listing of the CSOP Bitcoin Futures ETF (3066) and CSOP Ether Futures ETF (3068).

Hong Kong's HSBC Allows Customers to Trade Bitcoin, Ether ETFs but That's Not Really News https://coindesk.com/business/2023/06/26/hong-kongs-hsbc-allows-customers-to-trade-bitcoin-ether-etfs-but-thats-not-really-news/… via        
@coindesk
#PetroChina is breaking to the new highs. Our advice buying Energy Giant PetroChina from blue box area was correct. Read for targets: https://elliottwave-forecast.com/stock-market/petrochina-acceleration-higher/… #elliottwave #trading #stocks $PCCYF #investment #hkex #oil #gas $CL_F
You forgot Henry (Xuejun) Zhao aka WhatsApp guy. State Energy HK acquired LC Group Holdings in 2016 (there was bribery involved to even list that co on HKex). They were advised in the transaction by Huarong, a subsidiary of which Zhao had almost 30% stake in until May 31, 2023.
KPMG’s Pat Woo and Irene Chu discussed the impact on the Real Estate sector of the ISSB standards S1 and S2 during an exclusive roundtable. They explored ESG reporting, the implementation of the standards after a HKEX consultation and their impact starting in 2024.

#Realestate
Don't delay - late deadline 7th July! In-house teams & professionals can enter the APACD Awards, which recognise in-house comms excellence now. Previous winners of the In-House Communications Team of the Year award include Lenovo, LinkedIn and HKEX.
Beijing Stock Exchange (#BSE) and Hong Kong Exchanges and Clearing Limited (#HKEX) inked a memorandum of understanding (#MOU) to support dual listing of stocks of each other's qualified listed companies in #Beijing on Thursday.#Xinhuasilkroadnews
https://en.imsilkroad.com/p/334839.html
Everyone is talking about chip restrictions on China forming a choke hold, no one s talking about capital market restrictions

Take a look at HKex trading volumes, that’s having much larger impact on china’s competitiveness in the future than any chip sanctions..
Crypto ETFs debuted on the HKEX with the listing of the CSOP Bitcoin Futures ETF (3066) and CSOP Ether Futures ETF (3068).

Hong Kong's HSBC Allows Customers to Trade Bitcoin, Ether ETFs but That's Not Really News https://coindesk.com/business/2023/06/26/hong-kongs-hsbc-allows-customers-to-trade-bitcoin-ether-etfs-but-thats-not-really-news/… via        
@coindesk
#PetroChina is breaking to the new highs. Our advice buying Energy Giant PetroChina from blue box area was correct. Read for targets: https://elliottwave-forecast.com/stock-market/petrochina-acceleration-higher/… #elliottwave #trading #stocks $PCCYF #investment #hkex #oil #gas $CL_F
You forgot Henry (Xuejun) Zhao aka WhatsApp guy. State Energy HK acquired LC Group Holdings in 2016 (there was bribery involved to even list that co on HKex). They were advised in the transaction by Huarong, a subsidiary of which Zhao had almost 30% stake in until May 31, 2023.
Nasdaq posts best start to a year in 4 decades: 
#WallStreet #StockMarkets #GlobalMarkets #Nikkei #DAX #NYSE #NYC #SP500 #NASDAQ #CAC #FTSE #HKEX #JPX #Bitcoin #OilPrices #Crypto #FTX #SEC #Inflation #Ukraine #Russia
快来快来'''

# my_list = ["a","b","a","c",'a']
# convert list to string and generate
unique_string=(" ").join(text.split())
wordcloud = WordCloud(max_font_size=50, max_words=100, width = 1000, height = 500,  background_color="white").generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
