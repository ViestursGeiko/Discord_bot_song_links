discord==2.3.2
openpyxl==3.1.2
selenium==4.16.0


Šis projekts ieslēdz  "discorda" kanālā botu, kas reaģē uz komandu "!song "teksts"", kad komanda ir saņemta tas meklē "youtube.com" komandā norādīto tekstu, un iegūst rezultātu, kas tiek izvadīts kā links uzreiz "discorda" čatā un tiek
saglabāts kollonās .xlsx failā kopā ar nosaukumu, kas tika iegūts meklējot linku.

Sākūma tiek izveidots bots izmantojot "https://discord.com/developers/applications" saiti, kur mēs botam nodrošinam tā nosaukumu, attēlu, piekļuves atļaujas utt. No saites, kad bots ir uzstādīts, iegūstam linku
kurš ļauj uzaicināt botu uz discord serveri. No saites arī iegūstam katram botam unikālu kodu, jeb "tokenu" kuru mums vajadzēs, lai pēc tam botu varētu aktivizēt un uzdot tam komandas.
discord_bot.py fails atbild par discord bota palaišanu serverī, kā arī par to, lai iegūtais rezultāts tiktu saglabāts excel failā un parādītu rezultātu discord čata serverī.
Lai to izdarītu mēs izmantojam paredzēto importu "discord". Kodā norādam iegūto "Tokenu", kas nodrošina to, ka mēs uzdodam komandas tieši šim botam.
Kad Bots ir palaists veiksmīgi, tas izvadīs konsolē, ka tas ir ielagojies ar iepriekš(saitē) norādīto bota nosaukumu. Norādam botam "intentus", kas ļauj botam redzēt, saņemt un rakstīt īsziņas čatā.
Norādam simbolu,"prefix" , kas liek atsaukties botam uz komandām. Tas nepieciešam, lai bots nereģē uz vārdiem, kas atbilst komandas vārdiem, bet tikai vārdiem ar simbolu pirms tiem.
Izveidjoam komandu, piešķirot tai nosaukumu ko bots spēs atpazīt un pēc tam veikt darbības attiecībā no komandas. Ja komanda, kas atbilst pieejamajām, tiks ievadīta discord čatā, bots uzsāks "scrape.py" skriptu.

Šis skripts izmanto selenium biblotēku, kas ļauj mums iegūt informāciju no nepieciešamās saites. Kā arī no tās pašas selenium biblotēkas importējam "By" un "Keys", lai nodrošinātu simbolu ievadīšanu, un spētu atrast nepieciešamo vietu mājaslapā.
Kā pirmo lietu mēs definējam funkciju, lai pēc tam mēs spētu izmantot skripta iegūtās vērtības "discord.py".

Šajā skriptā ir norādīta "https://www.youtube.com/" saite, kurā mēs atsakamies no "cookies", un izmantojot NAME un ID elementu metodi atrodam "search bar" un uzspiežam "meklēt" pogu.
Pēc tam izmantojot XPATH atrašanas metodi atrodam primo video, kas atbilst lietotāja ievadītajām kritērijam. Piem. "!song Dancin - kruno remix". Bots atpazīst komandu "song" un "Dancin - kruno remix" tiks izmantots lai ievadītu to "search bar".
Skripts galā iegūst video linku, kā arī video nosaukumu un atgriež vērtības, kā sarakstu "discord.py" failam. Un atgirež lietotājam čatā atbildi: "Requested song: "dziesmas links"". Šo linku un iegūto nosaukumu mēs pēc tam izmantojot "openpyxl"
biblotēku, ievadam "song_list.xlsx" failā. Sākumā mēs atveram .xlsx failu un izmantojam aktīvo lapu kurā tiks ievadīti dati. Pirmajā kollonā tiek ievadīts iegūtais dziesmas nosaukums un otrajā kollonā tiek ievadīts iegūtais dziesmas links,
un fails tiek saglabāts un aiztaisīts.

