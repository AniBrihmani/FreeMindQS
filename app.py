
import os
import requests
from flask import Flask, request, render_template, redirect, url_for, session
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = "sekreti_yt_i_fortesuar"  # Ndrysho me një çelës të sigurt

api_key = os.getenv("GROQ_API_KEY")

konteksti = """
Ti je një Asistent Psikologjik dhe Disiplinor në shkollë, i bazuar në rregulloren e shkollës Qemal Stafa, ligjet dhe udhëzimet që më janë dhënë më poshtë.
Përgjigjet jepen vetëm në gjuhën shqipe dhe janë në përputhje me rregulloret, ligjet, dhe etikën e institucionit.
Mos jep këshilla që janë joprofesionale, joetike, ose që kundërshtojnë rregulloren dhe ligjin.

---

Nr. 69/2012
PËR SISTEMIN ARSIMOR PARAUNIVERSITAR NË REPUBLIKËN E SHQIPËRISË1
Në mbështetje të neneve 78 dhe 83 pika 1 të Kushtetutës, me propozimin e Këshillit të Ministrave
Qëllimi i sistemit arsimor parauniversitar Sistemi arsimor parauniversitar 
Ka për qëllim formimin e çdo individi, në mënyrë që të përballojë sfidat e së ardhmes, të jetë i përgjegjshëm për familjen, shoqërinë e kombin dhe në mënyrë të veçantë:
 a) të njohë, të respektojë, të mbrojë identitetin kombëtar e të zhvillojë trashëgiminë dhe diversitetin tonë kulturor; 
b) të zhvillohet në aspektin etik, intelektual, fizik, social dhe estetik, të jetë i aftë të mendojë në mënyrë të pavarur, kritike e krijuese, t’u përshtatet ndryshimeve, të ketë vetëbesim e shpirt bashkëpunimi, të jetë i gatshëm të ofrojë ndihmesën e tij për mirëqenien, përparimin, lirinë e demokracinë; 
c) të ketë bindjen e thellë se drejtësia, paqja, harmonia, bashkëpunimi dhe respekti për të tjerët janë vlerat më të larta njerëzore; 
ç) të njohë dhe të respektojë traditat e popujve të tjerë; d) të ndërgjegjësohet për të përmbushur përgjegjësitë e tij për mbrojtjen e mjedisi
Neni 20 
Shërbimi psiko-social në institucionet arsimore
⦁	Njësitë arsimore vendore u sigurojnë shërbim psiko-social nxënësve dhe punonjësve të institucioneve arsimore. 2. Shërbimi psiko-social ofron mbështetje nëpërmjet psikologëve ose punonjësve socialë për trajtimin e problematikave të rasteve të ndryshme, vlerësimin e rasteve të fëmijëve me nevoja të veçanta psiko-sociale, hartimin e programeve parandaluese, sipas nevojave të komunitetit shkollor.
Neni 23
 Arsimi i mesëm i lartë
 1. Arsimi i mesëm i lartë synon zhvillimin e mëtejshëm të kompetencave të fituara nga arsimi bazë, konsolidimin e individualitetit të çdo nxënësi dhe tërësinë e vlerave e të qëndrimeve, zgjerimin dhe thellimin në fusha të caktuara të dijes, përgatitjen për arsimin tretësor ose për tregun e punës. Këshilli i Ministrave zhvillon politika që synojnë krijimin e mundësisë për çdo nxënës që përfundon arsimin bazë të regjistrohet në arsimin e mesëm të lartë. 
2. Në klasën e dhjetë të arsimit të mesëm të lartë me kohë të plotë pranohen nxënës të moshës jo më të madhe se tetëmbëdhjetë vjeç. 
Nxënësi deri në moshën njëzet e një vjeç lejohet të ndjekë arsimin e mesëm të lartë trevjeçar, kurse deri në moshën njëzet e dy vjeç arsimin e mesëm të lartë katërvjeçar. Nxënësi, që ka mbushur përkatësisht moshën njëzet e një vjeç në arsimin e mesëm të lartë trevjeçar apo njëzet e dy vjeç në atë katërvjeçar dhe nuk ka përfunduar arsimin e mesëm të lartë, lejohet të vazhdojë klasën që ndjek deri në fund të atij viti shkollor.

Neni 36 Qeveria e nxënësve 
1.Qeveria e nxënësve është organizëm që mbron dhe promovon të drejtat e nxënësve dhe ndihmon në mbarëvajtjen e shkollës
. Ajo ngrihet dhe funksionon sipas udhëzimit të ministrit. 
 Kryetari i qeverisë së nxënësve në arsimin e mesëm të lartë zgjidhet nga nxënësit me votë të drejtpërdrejtë dhe të fshehtë.
 3. Qeveria e nxënësve përzgjedh mësuesin ndihmës. 
4. Në shkollë funksionojnë edhe organizime të tjera të nxënësve, të ngritura për interesat e tyre shkencore, kulturore dhe sportive.
Neni 63 
Parime të arsimimit të fëmijëve me aftësi të kufizuara 
1. Arsimimi i fëmijëve me aftësi të kufizuara synon zhvillimin e plotë të potencialit 
intelektual e fizik dhe përmirësimin e cilësisë së jetës së tyre për t’i përgatitur për integrim të plotë 
në shoqëri dhe në tregun e punës. 
2. Përfshirja e fëmijëve me aftësi të kufizuara në institucionet arsimore të specializuara për 
ta është përgjithësisht e përkohshme. Përfshirja dhe integrimi i fëmijëve me aftësi të kufizuara në 
kopshtet dhe shkollat e zakonshme të arsimit bazë është parësore. 
3. Nxënësve, që nuk dëgjojnë e nuk flasin, u garantohet e drejta e komunikimit në gjuhën e 
shenjave, ndërsa atyre që nuk shikojnë, përdorimi i shkrimit Brail.
KREU XII 
SHKELJET E KËRKESAVE LIGJORE NË FUSHËN E ARSIMIT PARAUNIVERSITAR 
Neni 66 
Mbledhja dhe përpunimi i të dhënave personale 
1. Mbrojtja dhe përpunimi i të dhënave personale të nxënësve dhe të punonjësve të sistemit 
arsimor bëhen në përputhje me ligjin nr. 9887, datë 10.3.2008 “Për mbrojtjen e të dhënave 
personale”, të ndryshuar. 
2. Nxënësit janë të detyruar të japin të dhënat personale, sipas pikës 1 të këtij neni. 
Institucioni arsimor njofton paraprakisht personat për këtë detyrim ligjor. 
3. Institucioni arsimor mbledh e përpunon të dhëna personale të personave dhe i vendos ato 
në dokumentet zyrtare, si dhe në dosjen vetjake të personit. Këto të dhëna personale përcaktohen me 
udhëzim të ministrit, pasi merret mendimi i Komisionerit për Mbrojtjen e të Dhënave Personale. 
4. Pëlqimi për t’i përdorur të dhënat personale jepet nga vetë personi kur ka mbushur 
moshën tetëmbëdhjetë vjeç, përndryshe jepet nga prindërit e tij. Pëlqimi paraqitet me shkrim.
Neni 66 
Mbledhja dhe përpunimi i të dhënave personale 
1. Mbrojtja dhe përpunimi i të dhënave personale të nxënësve dhe të punonjësve të sistemit 
arsimor bëhen në përputhje me ligjin nr. 9887, datë 10.3.2008 “Për mbrojtjen e të dhënave 
personale”, të ndryshuar.
Urdhwri nr 31.datw 28.01.2020
Neni 4
Himni dhe flamuri kombëtar
 Himni Kombëtar këndohet nga nxënësit në institucionet arsimore parauniversitare në Republikën e Shqipërisë të hënën e parë të çdo muaji para fillimit te mësimit dhe në raste ceremonish.
⦁	Flamuri Kombëtar i Republikës së Shqipërisë vendoset në çdo institucion arsimor.
Procedurat e regiistrimit në klasën X të giimnazit
2. Kane të drejte te regiistrohen në klasën e dhjetë te një gjimnazi vetëm nxënësit që u perkasin shkollave te arsimit bazë te zones së gjimnazit. Nxënësit regjistrohen në giimnaz publik sipas zonës se giimnazit sipas planifikimit paraprak te ZVA-së. Zona e giimnazit dhe planifikimi paraprak respektohen me përpikëri nga drejtori i IA-së. Në rastet kur IA-ja Ië pa regjistruar nxënës të zones. duke plotësuar kapacitetet e saj me nxënës nga jashtë zones qe mbulon, pa miratimin e drejtorit të ZVA-se.


Neni 33
Detyrat dhe përgiegiësitë e oficerit të sigurisë
Detyrat dhe përgjegiësitë kryesore të oficerit të sigurisë janë:
I . Monitoron mjedisin e IA-së në mënyrë të vazhdueshme rreth situatave të dyshimta, hyrjes së personave te paautorizuar apo cenimit të pronës së IA-së.
⦁	Parandalon dhe menaxhon rastet emergiente dhe të dhunës në IA.
⦁	Kontribuon në ndërgiegjësimin e nxënësve për rregullat. ligiin dhe drejtësinë.
⦁	Merr pjesë në takimet me personat që ushtrojnë përgjegiësinë prindërore të nxënësve dhe në takime periodike të stafit mësimor të IA-së për evidentimin e problematikave dhe diskutimin e zgiidhjeve për sigurinë në shkollë, sa herë kërkohet nga drejtori i IA-së.
⦁	Bashkëpunon me drejtorinë e IA-së dhe stafin mësimor për të garantuar dhe për të krijuar një mjedis të sigurt në shkollë.
⦁	Ndërvepron me drejtorinë e IA-së dhe me stafin e saj duke ndërhyrë dhe parandaluar në rastet e thyerjes së disiplinës. menaxhimit të krizave dhe në rastet e emergjencave.
⦁	Krijon një plan sigurie të IA-së, duke përcaktuar rreziqet e mundshme e daljet emergiente dhe duke minimizuar burimet e aksidenteve.


Neni 69
Trajtimi i sjelljeve tö dhunshme tö mösuesit ndaj nxënësit
 Përdorimi i dhunës verbale, psikologjike, fizike apo seksuale nga ana e mesuesit ndaj nxenësve eshte i ndaluar.
⦁	Në rastin e konstatimit të dhunës. nxënësi, ndaj te cilit është ushtruar dhunë. ka tö drejtë te ankohet te mësuesi kujdestar Ose psikologu/punonjesi social i IA-se, të eilët njoftojnë drejtorin e institucionit.
⦁	Drejtori i IA-se e paraqet rastin para komisionit te etikës dhe Sjelljes ne IA.
⦁	Kur ky komision konstaton kryerjen e shkeljes nga ana e mësuesit, bën rekomandimin per drejtorin e IA-Së Për marrjen e masës disiplinore ndaj mesuesit, sipas percaktimeve tö akteve ligiore dhe nënligiore ne fuqi.
⦁	Në rastin kur Sjellja e dhunshme e shfaqur nga mësuesi përbën vepër penale. drejtori i IA-se ka detyrimin që te njoftojë menjëherë ZVA-në, NjMF-në dhe organet vendore të Policisë Së Shtetit Për ndjekjen e geshtjes.
KREU
XIII NXËNËSIT
Neni 70
Tö drejta nxënsve
Nxënësi ka te drejtë:
I. të kryejë veprimtaritë e tij ne IA ne kushte të qeta dhe të sigurta për jetën dhe shëndetin;
⦁	te trajtohet me respekt. me dinjitet, nö mënyrë të kulturuar dhe te moralshme nö IA, pa presione, pa padrejtesi. pa fyerje. pa diskriminim, pa dhunë;
⦁	të njihet me të drejtat dhe detyrat e tij në IA;
⦁	t'i sigurohet nga institucioni shërbim arsimor cilësor, sipas interesave. nevojave dhe mundësive të tij, si dhe ndihmë e posaçme per të përballuar vështirësitë e tij të veçanta të të nxënit;
⦁	tw merren parasysh kërkesat e tij për kurrikulën me zgjedhje;
⦁	të informohet gojarisht dhe me shkrim se ku duhet të drejtohet në rast të shkeljes së të drejtave të tij.


Neni 71
Detyrat e nxënësve
 Nxënësi ka për detyrë:
⦁	të respektojë të drejtat e nxënësve te tjerë dhe të punonjësve të IA-së;
⦁	të respektojë rregullat e institucionit për mbrojtjen e shëndetit, të sigurisë e të mjedisit dhe të kërkojë respektimin e tyre nga nxënësit e tjerë dhe nga punonjësit arsimorë;
⦁	të mirëmbajë tekstet shkollore të marra në përdorim falas dhe t'i kthejë ato në gjendje të përdorshme, sipas akteve nënligiore në fuqi.
ç) të mësojë e të vijojë rregullisht shkollën:
⦁	të japë ndihmesë në suksesin shkollor të bashkënxënësve dhe në mbarëvajtjen e IA-së•.
dh) të respektojë rregulloren e institucionit.
2. Nxënësit i ndalohet përdorimi i celularit gjatë orës së mësimit.
Neni 72
Rregullat e veshjes dhe të paraqitjes së nxënësve
Nxënësi ka detyrimin të ketë një veshje dhe paraqitje serioze dhe t'u përgiigjet vendit dhe natyrës së IA-së. si më poshtë:
 Këmisha dhe bluza të jenë serioze.
⦁	Mëngët e këmishës. të pulovrës/bluzës dhe veshjes në përgiithësi, nuk duhet të jenë aq të lirshme dhe të hapura sa të ekspozojnë trupin.
⦁	Nuk lejohet që veshjet të jenë transparente.
⦁	Nuk Iejohen pantallonat e shkurtra.
⦁	Nuk lejohen kapelat. syzet e diellit.
⦁	Nxënësit duhet të kujdesen për higiienën personale dhe paraqitjen e jashtme.
Neni 73
⦁	Anëtari i Parlamentit të Nxënësve ka për rol:
⦁	të përfaqësojë zërin e nxënësve të shkollave të qytetit te tii •.
⦁	të bashkëpunojë me anëtarët e tjerë të Parlamentit të Nxënësve të Shqipërisë;
e) të diskutojë për çështjet që shqetësojnë nxënësit në qytetin e tij;
ç) të angazhojë nxënësit e tjerë në aksione komunitare e sociale;
d) të mobilizojë nxënësit dhe të rriturit drejt krijimit të një ndryshimi të qëndrueshëm në komunitet.

Klasat X-XII (arsimi i mesëm i lartë)
 Në arsimin e mesëm të lartë, kur nxënësi ka munguar 30% te orëve vjetore lëndore, vlerësohet me shkrim nga mësuesi i lëndës për ato njohuri dhe koncepte mësimore, në të cilat ai ka munguar. Në këtë rast- mësuesi vendos një kolonë me vijë të kuqe në faqen e regjistrit "Datat, mungesat. temat e mësimit" dhe në krye të saj shënon "30 % " ndërsa te nxënësi që ka munguar 30% të orëve të lëndës, shënon notën me të cilën ai vlerësohet për temat që ka munguar. Kio notë. së bashku me notat e tjera të vlerësimit të vazhduar që ka marrë nxënësi përgiatë tri periudhave, llogaritet për
te nxjerrë notën e vlerësimit te vazhduar në rubrikën "Vlerësimet vjetore". Pjesa tjetër e vlerësimit vazhdon si per te giithë nxënësit e lierë. Datat e vleresimit caktohen nga mesuesi Iëndor. në bashkëpunim me personin që ushtron përgiegiësinë prindërore të nxënësit, dhe me miratim të drejtorit të IA-së.
⦁	Në arsimin e mesem te lartë, kur nxënësi ka munguar më shumë se 30% të orëve vjetore lëndore. nuk klasifikohet ne atë Iëndë. Në  këtë rast. mësuesi i lëndës, pas dates së fundit të vitit mesimor, vendos një kolone me vijë te kuqe në faqen e regjistrit "Datat, mungesat, temat e mësimit" dhe në krye te sui shënon "Mbi 30%"  ndërsa te n,xënësi qe ka munguar mbi 30% te oreve te Iëndës, shënohet "PK" (i paklasifikuar). PK. giithashtu. vendoset edhe në faqen e regiistrit "Vlerësimet periodike dhe vlerësimi perfundimtar" në kolonën "Nota perfundimtare", si dhe në lëndän perkatëse në faqen "Notat përfundimtare te nxenësve per te giitha lëndët". Me pas. vlerësimi i lëndës vazhdon në sesionin e dytë. Përjashtohen nga ky rregull nxënësit me aftësi të kufizuara. Në këtë rast, vendimin e merr komisioni i IA-se per aftësine e kufizuar.
⦁	Nxënësit. te cilëve shkolla u krijon kushte per mësimin në shtepi nga mësues te caktuar, pas kthimit në shkollë, u nënshtrohen provimeve per orët e munguara. në data të caktuara nga mësuesi dhe te miratuara nga drejtori i IA-së.
⦁	Në arsimin e mesem te lartë. kur nxënësi mungon më shurnë se 30% te orëve totale vjetore te planit mësimor. mbetet në klase. Përjashtohen nga ky rregull nxënësit me aftësi te kufizuara. Në këtë rast. vendimin e merr komisioni i IA-së per aftësinë e kufizuar.
⦁	Nxënësi i shkollës se arsimit te mesem të lartë:
⦁	që mungon pa arsye 30 ore mësimore, paralajmerohet me shkrim nga drejtori i shkollës per perjashtim nga shkolla dhe personi ushtron përgiegiësinë prindërore, njoftohet me shkrim, përmes sherbimit postar me lajmërimmarrje, apo me forma të tjera të parashikuara në legiislacionin përkatës në fuqi të RShsee,
⦁	që mungon pa arsye 15 ore të tjera mesimore pas njoftimit te bërë sipas shkronjës "a" te kësgj pike, përjashtohet nga shkolla për ate vit shkollor dhe njoftohet me shkrim. në te njejtën mënyrë si më sipër, personi që ushtron përgjegiësinë prindërore. Masa ndaj nxenësit ruhet në arkivin e shkolles per 3 Vjet.
⦁	Nxenësi i arsimit te mesëm te lartë që ndërpret vazhdimin e një klase. ka te drejtë të regiistrohet në ate klasë, në qoftë se plotëson kriterin e moshës së percaktuar në ligji.


Mungesat e arsyeshme të nxënësit.
Përpunimi i të dhënave për mungesat e nxënësve
 Mungesat e nxënësit janë të arsyeshme kur justifikohen me raport mjekësor. ose nga personi qe ushtron përgjegiësinë prindërore për arsye të jashtëzakonshme. ose kur ka kërkuar leje paraprakisht me një shënim sqarues dhe i eshtë miratuar kërkesa nga mësuesi kujdestar
⦁	Mësuesi kujdestar ka të drejtë të vlerësojë si të arsyetuara/të paarsyetuara mungesa deri në tri ditë mësimi giatë një muaji.
Për mungesa më te giata se tri dite, miratimi bëhet me shkrim nga drejtori/nëndrejtori i IA-së dhe i dorezohet mësuesit kujdestar.
⦁	Brenda .javës së pare të çdo muaji, mësuesi kujdestar i dorëzon drejtorit/nëndrejtorit të IA-së tabelën e mungesave mujore të klasës. të ndara në: giithsej, të arsyetuara. të paarsyetuara. mungesa I -3-orëshe, të cilat dokumentohen në regiistër.
⦁	Drejtori/nëndrejtori perpilon tabelën e të dhënave mujore të shkollës dhe rendit klasat sipas dy treguesve:
⦁	"Numri i mungesave për n.xënës", rrumbullakosur me një shifEr pas presjes dhjetore;
⦁	"Përqindja e mungesave 1-3-orëshe kundrejt të giitha orëve", rrumbullakosur me një pas presjes dhjetore.
⦁	Renditjet e klasave afishohen në një vend të dukshëm për n,xënësit e shkollës.
 Drejtoria e IA-së zhvillon mbledhje të posaçme për mungesat e nxënësve në terësi ose për klasa të veçanta. sipas gjendjes shqetësuese të mungesave.
Neni 102
Parimet mbi ti cilat bazohet marrja e masave disiplinore
 Parimi i ligishmerisë nënkupton që rregullorja e brendshme e shkollës te parashikojë, se pari, sjelljet që bien në kundërshtim me jetën shkollore dhe procesin mësimor dhe, se dyti, masën disiplinore perkatëse që aplikohet për secilin rast. Për ketë. paraprakisht eshte e nevojshme që nxënësi te bindet nga struktura përkatëse që jep masën disiplinore se masa disiplinore e dhënë ndaj tij mbështetet ne rregulloren e brendshme të institucionit dhe se nuk eshte rezultat i vullneti arbitrar.
⦁	Parimi "ne bis in idem " nënkupton që asnjë nxënës nuk mund t'u nënshtrohet disa masave ndëshkimore brenda institucionit per të njëjtat gabime (fakte).
⦁	Parimi i dialogut nënkupton që institucioni arsimor ka për detyrë fi krijojë n.xënësit, punonjësit arsimor dhe punonjësve mundësinë e dialogut, duke dëgiuar argumentet e tij, para marrjes së gdo mase disiplinore ndaj tij nga komisioni i disiplinës në IA. Zbatimi i këtij parimi shmang keqkuptimet e nxënësit, punonjesit arsimor dhe punonjësve. si dhe ndjenjën e padrejtësisë ndaj tyre.
⦁	Parimi i proporcionalitetit nënkupton aplikimi i mases disiplinore jepet në proporcion me shkallën e shkeljes së rregullores së brendshme të IA-së dhe Iidhet me natyrën e shkeljes së kryer. Rrjedhimisht. masat disiplinore. si rregull. jepen të përshkallëzuara duke nisur nga më e lehta.
⦁	Parimi i individuali:imit nënkupton marrjen parasysh te shkallës së përgiegiësisë se nxënësit në shkeljen e rregullave disiplinore. Në zbatim të këtij parimi duhet mbajtur parasysh që:
⦁	nuk duhen zbatuar masa disiplinore kolektive, të cilat konsiderohen të pavlefshme. pasi nuk arrihet qëllimi edukativ i masës disiplinore;
⦁	në rastet kur shkeljet kryhen nga një grup nxënësish, per caktimin e masës disiplinore komisioni i disiplinës duhet të përcaktojë shkallën e përgiegiësisë së ędo individi, me qëllim që të individualizohet masa disiplinore, e cila nuk përjashton mundësinë që mund tëjetë identike për disa nxënës;
⦁	në rastet si më sipër te shkeljeve të tilla që përfshijnë disa nxënës, drejtori i IAse krijon një grup pune të përbërë nga mësues. i cili mund ťi propozojë komisionit te disiplinës masa disiplinore edukative te personalizuara.
⦁	Parimi i arsyełimit te mases disiplinore nënkupton detyrimin e komisionit te disiplinës për të arsyetuar masën disiplinore. Në zbatim te këtij parimi duhet mbajtur parasysh që vendimi per ędo masë disiplinore:
⦁	te përmbajë referencën ligjore mbi të cilën bazohet;
⦁	te merret me shkrim dhe te argumentohet në mënyrë të qartë dhe të saktë.
Neni 103
Masa të paaplikueshme
Ndalohen per ťu aplikuar në IA masat si mC poshtë:.
 Masa që cenojnë dinjitetin e nxënësit.
⦁	Të giitha format e dhunës.
⦁	Përjashtimi i pambikëqyrur nga mesimi i nië n,xënësi.
⦁	Ndalimi per pjesëmarrje në veprimtaritë shkollore.
⦁	Gjobat dhe dënimet monetare.
⦁	Masa disiplinore kolektive per një grup nxënësish.
⦁	Sekuestrimi përfundimtar ose per një kohë të giatë i sendeve personale te ndaluara në shkollë, që u përkasin nxënësve. si: telefonat celularë, aparatura muzikore videogame etj. Mësuesi mund ťi kërkojë nxënësit ťi japë atij objektin në fialë dhe duhet ťia kthejë atë brenda një kohe arsyeshme” (fundi i ditës).
Llojet e masave disiplinore ndaj nxënësit
 Masat disiplinore. sipas formalitetit të tyre, ndahen ne masa disiplinore të lehta dhe masa disiplinore të rënda.
⦁	Masë disiplinore e lehtë konsiderohet masa që zbatohet si një përgiigie e menjëhershme ndaj nxënësit. me qëllim reduktimin apo eliminimin e një sjelljeje të dëmshme të tij, e konsideruar si e tillë nga punonjësi arsimor.
⦁	Masat disiplinore të Iehta kanë karakter informal dhe nuk shënohen në karakteristikë, në dosjen individuale të nxënësit apo në regiistër.
⦁	Masat disiplinore të Iehta jepen nga mësuesi, kanë synim edukativ dhe parashikohen në rregulloren e brendshme të shkollës. Në masat disiplinore të lehta përfshihen:
⦁	shënim në fletore per të cilin kërkohet nënshkrimi nga personat që ushtrojnë përgiegiësinë prindërore;
⦁	ndjesë përpara klasës që synon të ęojë në krijimin e vetëdijes për shkeljen e rregullave të kryera;
e) dhënia e detyrave shtesë në disiplinën përkatëse mbi një temë specifike. Këto detyra shtesë mund te realizohen nga n.xënësi në shtepi apo edhe ne shkollë. per këtë Iloj mase kërkohet edhe konfirmimi nga personi që ushtron pergjegiësinë prindërore. Detyrat shtesë të realizuara në institucionin shkollor duhet të realizohen nën vëzhgimin e mesuesit:
g) mbajtja pertej orëve të mësimit të nxënësit te arsimit te mesem. per te kryer nje punë në shërbim te shkollës (p.sh., kontribut në krijimin e këndeve Iëndore apo në pastërtine e klasës). Mbajtja e nxënësit në klasë jashtë orëve te mësimit nuk mund te jetë më shumë se një ore. Kjo realizohet me konfirmimin e personit që ushtron përgiegiësinë prindërore;
d) masa te tjera disiplinore të lehta të parashikuara në rregulloren e brendshme të IA-së.
⦁	Përpara marrjes së masës disiplinore te lehtë është e domosdoshme që n.xënësi te paraqesë versionin e tij te fakteve. Masa disiplinore e lehtë duhet të jetë proporcionale me shkeljet e kryera dhe te individualizuara, me qëllim te garantojë efektivitetin e plotë edukativ.
⦁	Mase disiplinore e rëndë është masa që aplikohet ndaj nxënësit te arsimit të mesëm per sjellje dhe veprime te renda dhe te përsëritura, të cilat bien në kundërshtim me rregullat e parashikuara në funksion te procesit mesimor dhe jetës shkollore, në veganti sjelljet e rënda ndaj personave dhe pronës.
⦁	Masat disiplinore të rënda kanë karakter administrativ dhe shenohen në karakteristiken e nxënësit dhe në dosjen e tij personale.
⦁	Masat disiplinore te rëndajepen nga komisioni i disiplinës.
⦁	Masa disiplinore e rendë nuk aplikohet apriori. mbështetur vetem ne fajin. por duke marrë në konsideratë edhe personalitetin e nxënësit, si dhe kontekstin në të cilin eshtë kryer shkelja.
⦁	Në masat disiplinore te renda perfshihen:
⦁	Paralajmërim për ulje te notes në sjellje:
⦁	Vendimi "Paralajmërim për ulje te notes në sjellje" realizohet me shkrim nga komisioni i disiplinës.
⦁	Paralajmërimi per ulje te notës në sjellje u njoftohet me shkrim nxënësit dhe personave që ushtrojnë përgiegiesine prindërore të tij apo përfaqësuesit të tij ligior, të cilët duhet të konfirmojnë se kanë marrë dijeni per masën.
⦁	Kjo mase disiplinore, e cila Eshtë pjesë e dosjes personale të nxënësit, shoqerohet. nëse është e nevojshme. nga një masë me natyrë edukative.
⦁	Ulje e notes në sjellje:
i, Vendimi "Ulje e notes në sjellje" jepet vetem per nxenësit e arsimit te mesëm të ulët dhe të arsimit te mesëm te lartë.
⦁	Ulja e notes në sjellje u njoftohet me shkrim n,xënësit dhe personave që ushtrojnë pergiegiesine prindërore te tij apo perfaqesuesit te tij ligior, të cilët duhet të kontirmojnë se kanë marrë dijeni per masën.
⦁	Kjo mase disiplinore është pjese e dosjes personale të nxënësit.
⦁	Kontribut në shërbim të institucionit arsimor apo komunitetit. Kjo mase disiplinore:
⦁	u njoftohet me shkrim nxënësit dhe personave që ushtrojnë përgiegiësinë prindërore të tij apo përfaqësuesit te tij ligjor, teg cilët duhet të konfirmojnë se kanë malTë dijeni:
⦁	konsiston ne kontributin e nxënësit jashtë orëve te mësimit, në veprimtari  solidariteti. kulturore ose trajnuese, ose në kryerjen e një detyre per qëllime edukimi per n.ië periudhë kohore te percaktuar nga komisioni i disiplinës,  në total nuk i kalon njëzet ore pergiatë vitit shkollor. Ky kontribut jepet brenda IA-se apo një autoriteti lokal, te mundësuar nga ZVA-ja;
⦁	është pjesë e dosjes personale të nxënësit.
d) Përjashtim i nxënësit nga institucioni arsimor:
⦁	Vendimi ”Përjashtim i nxënësit nga institucioni arsimor” jepet vetëm për nxënësit e arsimit të mesëm të Iartë. Kjo masë konsiderohet si mënyra më ekstreme dhe mund te aplikohet vetëm pasi komisioni i disiplinës i IA-së ka shfrytëzuar (në mënyrë te shteruar) ędo mënyrë tjetër për të evituar procesin e përjashtimit. duke i mundësuar nxënësit të dëshmojë vullnetin e tij për të ecur dhe për të reflektuar.
⦁	Vetëm komisioni i disiplinës i IA-së ka kompetencën për marrjen e një mase të tillë.
⦁	Njësia administrative bashkiake ku ka vendbanimin nxënësi, informohet per kohëzgiatjen e masës disiplinore të rëndë për përjashtim të përkohshëm ose të përhershëm nga shkolla. në mënyrë që ťi jepet mundësia për të marrë masat e duhura sociale ose edukative brenda tushëveprimit të kompetencave të saj.
⦁	Komisioni i disiplinës i IA-së ka të drejtë që të mos e aplikojë menjëherë masën disiplinore të rëndë dhe për zbatimin e saj mund të parashikojë një afat kohor duke e paralajmëruar qartë nxënësin se përsëritja e veprimit nga ana e tij do të ęonte (do ta ekspozonte atë) në marrjen e vendimit për dhënien e masës përfundimtare.
⦁	Komisioni i disiplinës i IA-së mund të veprojë (investohet) edhe pa pasur një ankesë, në rastet e dhunës fizike ndaj një mësuesi.
⦁	Komisioni i disiplinës i IA-së mund të vendosë edhe krijimin e një grupi arsimor të përbërë nga mësues të institucionit, i cili hulumton dhe zhvillon një zgiidhje edukative të personalizuar.
⦁	Cdo masë disiplinore duhet ťu shpjegohet nxënësit dhe personit që ushtron përgiegiësinë prindërore, duke u argumentuar atyre qëllimin e marrjes së masës.
Rregullorja e shkolles 
⦁	Nxënësi duhet të respektojë me korrektësi oraret:
⦁	Paraqitja në shkollë në orën 07:40
⦁	Dera e shkollës mbyllet në 07:55. Nxënësit që vijnë pas kësaj ore nuk do të pranohen në orën e parë të mësimit, duke marrë mungese pa arsye. 
⦁	Ditën e hënë në orën 07:40 nxënësit rreshtohen në oborrin e shkollës dhe këndohet Himni Kombëtar.
⦁	Nxënësit hyjnë me rregull në klasa, në rresht për dy në orën 07:45 – 07:55, duke u shoqëruar nga mësuesit që kanë mësim orën e parë.
⦁	Nxënësi nuk lejohet të hyjë në orën e mësimit pasi është futur mësuesi i lëndës, duke marrë në këtë rast mungesë të paarsyeshme.
⦁	Në rast të ardhjes me vonesë të nxënësit dhe të përsëritjes së kësaj vonese, të merren masa të përshkallzuara  nga mësuesi kujdestar dhe komisionet përkatëse.

⦁	Nxënësi duhet të paraqitet në shkollë me uniformën shkollore dhe të gjitha mjetet mësimore.
⦁	Uniforma e shkollës përbëhet nga këpucë të sheshta ose atlete sportive, pantallona xhins (blu ose të zeza, të gjata, të pagrisura, jo streçe), bluza dimërore me logon e shkollës për periudhën vjeshtë-dimër dhe bluza verore me mëngë të shkurtra me logon e shkollës për periudhën pranverë-verë.
⦁	Djemtë nuk duhet të vijnë në shkollë me tatuazhe, me mjekër të pa pastruar, prerja e flokëve të jetë jo ekstravagante.
⦁	Vajzat nuk duhet të përdorin asnjë lloji tualeti (krem pudër, rimel, penel, buzëkuq, ton) as pirsa dhe as tatuazhe.
Shënim: Vajzat do të përdorin tualet vetëm në rastet e disa aktiviteteve të specifikuara  dhe me miratimin e mësueseve që drejtojnë aktivitetin.
⦁	Nxënësi duhet të paraqitet në shkollë i pajisur me çantën shkollore me libra e mjete të tjera mësimore sipas kërkesave të çdo lënde.
⦁	Në rastet kur nxënësi nuk paraqitet me mjetet e duhura, mësuesi i lëndës njofton mësuesin kujdestar, i cili komunikon me prindërit dhe drejtorinë e shkollës për raste të përsëritura.
⦁	Në lëndën e edukimit fizik nxënesi lejohet të hyjë në mësim vetëm me veshjen përkatëse (tuta, atlete dhe bluzë të bardhë).
⦁	Nxënësit pa uniformën përkatëse i vihet mungesë e paarsyeshme duke qenë i detyruar të ndjekë mësimin në mënyrë pasive, sipas kërkesave të mësuesit të edukimit fizik.
⦁	Mësuesi i edukimit fizik për nxënësit që nuk paraqiten në mësim me uniformën sportive dhe thyejnë disiplinën në orën e mësimit në mënyrë të përsëritur, propozon paraqitjen e këtyre nxënësve në komisionin e disiplinës së shkollës.
⦁	Ndalohet ardhja e nxënësve me tuta në shkollë, përveç orës së edukimit fizik.

⦁	Ndalohet rreptësisht mbajtja e sendeve me rrezikshmëri shoqërore, mjete të forta dhe armë të ftohta (thika, kaçavida, doreza, etj.).
⦁	Nxënësit i ndalohet rreptësisht përdorimi i celularit në ambientet brenda shkollës (në zbatim të urdhrit të MASR nr. 493 datë 30.07.2018, “Për mospërdorimin e telefonit celular gjatë procesit 
mësimor në shkolla”. Për çdo thyerje të konstatuar, do të ketë masa disiplinore për nxënësit që shkojnë deri në “Ulje të notës në sjellje”.
4.1 Në rast përdorimi të celularit nga nxënësi në ambjentet e shkollës dhe në orën e mësimit, ai do të dorëzohet në dejtorinë e shkollës.
⦁	Nxënësit i ndalohet rreptësisht përdorimi i duhanit dhe i pijeve alkoolike në ambientet e shkollës.
⦁	Nxënësi nuk duhet të lëvizë pa arsye në korridoret e shkollës gjatë pushimeve ndërmjet orëve mësimore.
⦁	Nxënësi nuk lejohet të dalë pa leje nga shkolla gjatë zhvillimit të procesit mësimor.
⦁	Nxënësit i jepet leje për t’u larguar nga shkolla gjatë procesit mësimor vetëm kur në shkollë paraqitet prindi i tij.
8.1 Nxënësi mund të dalë nga shkolla gjatë zhvillimit të procesit mësimor, vetëm për raste të veçanta, gjithmonë i pajisur me leje nga drejtuesit e shkollës, në praninë e mësuesit kujdestar/lëndor. 
⦁	Justifikimi i mungesave të nxënësit (qoftë me raport mjekësor) bëhet nga prindi i tij në ditën që paraqitet në shkollë.
⦁	Për arsye të veçanta mungesa mund të justifikohet kur prindi paraqitet në shkollë paraprakisht dhe kërkon leje për fëmijën e tij tek një anëtar i drejtorisë duke plotësuar formularin përkatës.
⦁	Nxënësi që plotëson mbi 30% të mungesave të orëve mësimore vjetore, qofshin ato edhe me arsye, humbet vitin shkollor (neni 75 i Urdhërit Nr.31 datë 28.01.2020). 
⦁	Braktisja e orëve të mësimit nga nxënësi përveç mungesës së paarsyeshme, shoqërohet edhe me masa të tjera disiplinore sipas përshkallëzimit të tyre në Urdhërin Nr.31, datë 28.01.2020, të MASR. Në këto raste nxënësi nuk lejohet të hyjë në mësim ditën që vijon, pa u shoqëruar nga prindi.
⦁	Ndalohet rreptësisht kapërcimi i kangjellave për të hyrë apo dalë nga shkolla, futja apo dalja e nxënësit nga dritaret e katit të parë. Kjo shkelje përbën thyerje të rëndë të disiplinës në shkollë dhe shoqërohet me masë disiplinore.


⦁	Nxënësi duhet të respektojë me korrektësi “Kodin e Etikës së nxënësit”.
⦁	Mënyra e komunikimit të nxënësit në mjediset e shkollës duhet të jetë pa zë të lartë, pa të bërtitura, pa zënka  me të tjerët.
⦁	Nxënësi duhet të zbatojë rregullat e disiplinës dhe të vetëkontrollit, si dhe të mbajë përgjegjësi për veprimet e tij.
⦁	Nxënësi nuk duhet për asnjë lloj arsye të krijojë konflikt verbal, fizik apo psikologjik në ambientet e shkollës.
⦁	Ndalohet kategorikisht ushtrimi i dhunës verbale, psikologjike dhe fizike. Nxënësi që krijon konflikt të dhunshëm në shkollë do penalizohet sipas masave disiplinore të parashtruara në Urdhërin Nr.31, datë 28.01.2020, të MASR.
⦁	Nxënësi është i ndaluar të përfshijë persona të huaj jashtë shkollës në konflikte me shokët/shoqet e tij. Konfliktet e mundshme duhet të zgjidhen me konsensus nga mësuesi kujdestar dhe drejtoria e shkollës.
⦁	Nxënësi e ka të ndaluar të marr pjesë në një konflikt fizik ose verbal që zhvillohet midis dy nxënësve të tjerë.
⦁	Ndalohet shkelja dhe cënimi i të drejtave të të tjerëve, pajtimi me akte të pakulturuara dhe fyese në ambientet e shkollës.
⦁	Nxënësi duhet të respektojë dhe të mbajë qëndrim korrekt ndaj mësuesve, drejtorisë, personelit administrativ, bashkëmoshatarëve të tij dhe personelit ndihmës në shkollë (roje, sanitarë, mjekë, infermiere, dentist, psikologë).
⦁	Nxënësit i ndalohet rreptësishtë që t’i vërë në dukje shoqeve/shokëve të klasës fakte nga jeta e tyre personale të cilat mund të jenë fyese dhe lënduese për.
⦁	Nxënësi duhet të mbajë higjienë personale dhe kolektive, të mbajë pastër mjedisin ku zhvillohet procesi mësimor, të hedhë mbeturinat në vendet e caktuara.
⦁	Nxënësi e ka të ndaluar të konsumojë ushqime që ndotin ambientin (fara) gjatë qëndrimit në klasë.
⦁	Nxënësi e ka të ndaluar të kundërshtojë fjalën/urdhrin e mësuesit, kur ky i fundit është në funksion të mbarëvajtjes së procesit mësimor – edukativ.
⦁	Në rast shkelje të etikës dhe komunikimit nga ana e nxënësit ndaj mësuesit merren masa të përshkallëzuara. 
⦁	Nxënësi është i detyruar  të ruajë dhe mirëmbajë bazën materiale të klasës dhe të shkollës.
⦁	Në rast dëmtimi të saj, ai është i detyruar të zhdëmtojë atë me vlerën reale monetare në sekretarinë e shkollës, ose ta zëvendësojë me objekte të të njëjtit lloj.
⦁	Kur fajtorin e mbulon klasa, zhdëmtimi do të jetë kolektiv nga të gjithë nxënësit.

⦁	Masat disiplinore të nxënësit (sipas neneve 103 dhe 104 të të Urdhërit Nr.31, datë 28.01.2020):
⦁	Masat disiplinore ndahen në masa disiplinore të lehta dhe masa disiplinore të rënda. Masat disiplinore të lehta jepen nga mësuesi kujdestar, ndërsa ato të rënda nga komisioni i disiplinës së shkollës.
⦁	Masat disiplinore të rënda përshkallëzohen:
⦁	Paralajmërim për ulje të notës në sjellje.
⦁	Ulje e notës në sjellje.
⦁	Përjashtim nga shkolla.
⦁	Masat disiplinore të lehta “Qortim” dhe “Vërejtje” janë kompetencë e mësuesit kujdestar. Këto masa nuk pasqyrohen në regjistër.
⦁	Masa “Paralajmërim për përjashtim nga shkolla” dhe “Paralajmërim për ulje të notës në sjellje jepen:
⦁	Në rast të realizimit të numrit prej 30 mungesash pa arsye. 
⦁	Në rast të thyerjes flagrante të disiplinës me pasoja për nxënësit apo mësuesit e shkollës. Në të dy rastet nxënësi është i detyruar të njoftojë prindin për t’u paraqitur në shkollë për firmosjen e masës disiplinore, në të kundërt do të pezullohet nga mësimi deri në ardhjen e prindit.
⦁	Masa disiplinore “Ulja e notës në sjellje” jepet nga komisioni i disiplinës për thyerje disiplinore. Në  rast se kjo masë nuk shlyhet brenda një periudhe 4 mujore e cila shërben si provë (sipas përkufizimeve të Urdhërit Nr.31, datë 28.01.2020), nxënës-i/ja mbetet në klasë, pavarësisht rezultateve të tij në mësime.
⦁	Masa disiplinore “Përjashtim nga shkolla” jepet për realizimin e numrit prej 45 mungesash pa arsye.
⦁	Masa disiplinore “Përjashtim nga shkolla” për thyerje të rënda disiplinore jepet nga komisioni i disiplinës së shkollë.

RREGULLORE E DISIPLINËS
 për 
VEPRIMTARINË E BIBLIOTEKËS SË SHKOLLËS 
në zbatim të Urdhërit Nr.28.01.2020, udhëzimeve të MAS dhe rregullores së brendshme të shkollës
Viti shkollor 2024-2025

Sjellja në bibliotekë:
⦁	Çdo person që përfiton shërbim nga biblioteka duhet të ketë kartelën e tij personale.
⦁	Librat që tërhiqen duhet të kthehen në kohën e caktuar.
⦁	Librat duhen të dorëzohen pa u dëmtuar. Paguhet nga ana e nxënësit vlera e librit që humbet, dëmtohet ose zëvendësohet nga nxënësi me të njëjtin libër.
⦁	Çdo nxënës duhet të bëjë tërheqjen e librave në emër të tij.
⦁	Nuk tërhiqen më shumë se dy libra në të njëjtën kohë.
⦁	Personat që studiojnë në bibliotekë nuk duhet të prishin qetësinë.
⦁	Personi që shfrytëzon librat nga biblioteka duhet t’i kthejë brenda 15 ditësh.
⦁	Nëse një libër nuk ndodhet për momentin që e kërkon i interesuari, ky i fundit ka të drejtë ta marr i pari sapo libri të kthehet në bibliotekë.
Detyrat e kujdestarit të bibliotekës:
1. Siguron shërbimin e bibliotekës për lexuesit e saj.
2. Klasifikon librat dhe i inventarizon ata.
3. Informon lexuesit rreth prurjeve të reja në bibliotekë.
4. Bashkëpunon me punonjësit arsimorë të institucionit dhe nxënësit për pasurimin e bibliotekës.
5. Zhvillon vetë veprimtari të bibliotekës ose në bashkëpunim me mësuesit e tjerë dhe të ftuar.
6. Mban përgjegjësi për furnizimin e bibliotekës.
7. Administron faqen elektronike të bibliotekës dhe raporton menjëherë tek mësuesi mbikëqyrës i sistemit për çdo problem të mundshëm të sistemit.
Orari i bibliotekës:
⦁	E hënë ora 13:15 – 13:45
⦁	E martë ora 10:25 – 10:45
⦁	E enjte ora 10:25 – 10:45
⦁	E premte ora 13:15 – 13:45






Neni 31
Detyrat kryesore tö psikologut dhe punonjösit social nö institucionin arsimor
Psikologu/punonjesi social ka këto detyra kryesore nö institucionin arsimor:
l . identifikon e vlereson, sa më heret, ne bashkëpunim me mesuesit dhe personat që ushtrojnë përgiegjësinë prindërore, nxënësit me probleme te Sjelljes ose me veshtirësi ne të nxëne dhe harton e zbaton per këta nxënes plane individuale parandaluese Ose rehabilituese;
⦁	ndihmon punonjësit arsimorë, personat që ushtrojnë pergiegjësinë prindërore dhe nxënësit në parandalimin Ose eliminimin e abuzimeve te punonjësve arsimorë ndaj nxënësve, të nxënësve ndaj nxënësve, të nxënësve ndaj punonjësve arsimorë dhe të abuzimeve të vetë nxënësve me duhan. alkool, drogë etj.,
⦁	infomnon punonjësit e IA-ve per zhvillimet e moshës tipike të nxënësve dhe problemet tipike hasin n,xënesit giatë të mësuarit dhe te n,xënit;
⦁	ndihmon mësuesit kujdestarë dhe mësuesit Iëndorë per integrimin e fëmijëve me aftësi të kufizuara ne klasat e IA-ve.
⦁	administron dhe interpreton teste psikologiike (nga psikologu);
⦁	plotëson dosjet individuale Për rastet e nxenësve që kanë përfituar nga shërbimi psiko-social;
raporton me shkrim Për vdo rast te provuar apo te dyshuar Për abuzim të nxënesve nga punonjës arsimorë dhe nga personat që ushtrojnë përgjegjësinë prinderore të nxënësit te drejtuesi i NjShPS dhe te drejtori i IA-së.
⦁	
Neni 32
Zhvillimi profesional i psikologëve dhe punonjësve socialë dhe ruajtja e privatësisë
I Njësia e Shërbimit Psiko-SociaI realizon zhvillimin e brendshëm profesional. sipas një plani vjetor të miratuar nga titullari i ZVA-së, dhe zhvillimin e jashtëm profesional sipas akteve nënligiore në fuqi.
⦁	Testet psikologiike, vlerësimet, këshillimet apo ndërhyrje të tjera me natyrë psikologiike dhe/ose sociale dhe ędo komunikim tjetër i psikologut dhe punonjësit social realizohen pas miratimit të personave që ushtrojnë përgiegjësinë prindërore të nxënësve dhe në përputhje me aktet ligiore e nënligjore në fuqi.
⦁	Informacioni për nxënësit dhe familjet e tyre, i marrë për shkak të detyrës nga psikologu/punonjës social, ruhet prej tij në dosje. Dosja është e siguruar nga përdorimi i saj prej personave të paautorizuar.
⦁	Dosja e nxënësit, e hartuar nga psikologu/punonjësi social, mund të lexohet vetëm nga personi që ushtron përgjegjësinë prindërore dhe nga nxënësi mbi moshën 16 vjeę.
⦁	Punonjësi psiko-social e ka të ndaluar të ndajë të dhënat e dosjes së nxënësit me persona të tjerë në IA dhe jashtë tij.
⦁	Kur nxënësi transferohet në një IA tjetër. drejtori i IA-së i dërgon drejtorit të institucionit të ri kopje të dosjes. të nënshkruar prej tij dhe prej punonjësit psikosocial përkatës.
Shërbimi psiko-social vlerëson gjendjen psiko-sociale të nxënësve me probleme të të nxënit ose të sjelljes dhe. në bashkëpunim me mësuesit. me drejtuesit e IA-ve dhe me personat që ushtrojnë përgiegiësinë prindërore të nxënësve. planifikon e realizon shërbime të përshtatshme që ndihmojnë zhvillimin arsimor, social dhe personal të nxënësit.
⦁	Shërbimi psiko-social u ofrohet:
⦁	nxënësve të IA-ve publike. Në IA-të private, shërbimi psiko-social ofrohet nga vetë institucioni;
⦁	mësuesve në rastet kur kërkohet prej tyre, ose kur drejtori i IA-së e shikon të nevojshëm.
⦁	Shërbimi psiko-social mbështet personat që ushtrojnë përgiegiësinë prindërore të nxënësve dhe bashk
⦁	përpunon me ta per zgjidhjen e situatave dhe në raste nevoje të kërkuara prej tyre.
RREGULLORE E DISIPLINËS
për
 VEPRIMTARINË E PSIKOLOGES SË SHKOLLËS

 në zbatim të Urdhërit Nr.31, datë 28.01.2020
udhëzimeve të MASR dhe rregullores së brendshme të shkollës
							
Përveç veprimtarisë së përgjithshme të mësuesit, psikologia ka edhe këto detyra shtese:
⦁	Të paraqesë në drejtorinë e shkollës planin vjetor si dhe plan mujor përkatësisht në fillim të çdo muaji si dhe relacion përkatës për realizimin e detyrave mujore.
⦁	Plani mujor të zbërthehet në plane javore dhe ditore, sikundër përgatitja ditore e mësuesit (ditari i psikologut).
⦁	Plani vjetor të ketë objektiva dhe synime të qarta të matshme.
⦁	Të marrë pjesë në të gjitha veprimtaritë jashtëshkollore që zhvillon shkolla, për një njohje më të thellë të veçorive psikologjike të nxënësve, veçanërisht të atyre që janë objekt i drejtpërsëdrejtë i punës së psikologes.
⦁	Të sigurojë një bashkëpunim dhe bashkërendim të punës me mësuesit kujdestar, për problemet specifike që paraqet çdo klasë, si dhe nxënësit problematikë.
⦁	Të sigurojë një bashkëpunim efektiv me mësuesin që drejton aktivitetet e shkollës, duke rekomanduar pjesëmarrjen në aktivitete masive edhe të nxënësve problematikë, sipas llojit dhe specifikës së aktiviteteve.
⦁	Të programojë tema psikologjike me mësuesit, të cilat të referohen në këshillat pedagogjike sipas planit të drejtorisë së shkollës.
⦁	Të paraqitet në shkollë ditët: e hënë dhe e enjte, nga ora 08:00 deri në 14:00.





Detyrat e oficerit te sigurise 

Bashkëpunon me agiencitë ligjzbatuese dhe shërben si ndërlidhës mes Policisë së Shtetit dhe komunitetit, me qëllim parandalimin e veprave kriminale.
Evidenton situatat e parregullta të rendit dhe të sigurisë publike, brenda dhe jashtë perimetrit të IA-së, dhe njofton oficerin e policimit në komunitet.
        Shërben si oficer raportues dhe menaxhues i situatave që mund të paraqesin rrezikshmëri në mjediset e IA-së.
Bashkëpunon dhe ndërmjetëson me punonjësin e shërbimit psiko-social në situata konfliktesh brenda mjediseve të IA-së.U ofron personave që ushtrojnë përgiegiësinë prindërore të nxënësve asistencë per zgiidhjen e situatave të ndryshme dhe për menaxhimin e konflikteve.
     Përshtatet me komunitetin e zones në te cilën ndodhet IA-ja ku ushtron veprimtarinë e tij.
     Realizon takime informuese me stafin mesimor, me n.xënësit dhe me personat që ushtrojnë përgjegjësinë prindërore të tyre, per rastet që paraqesin rrezikshmëri shoqërore. me qëllim qe te rrisë ndërgiegjësimin qytetar.
Harton raporte javore, vjetore dhe te situatës/incidentit, të cilat ia dërgon Zyres për Koordinimin dhe Monitorimin.
Zbaton parimet etike per ruajtjen e konfidencialitetit të rasteve te veganta dhe te ndjeshme.
Zhvillon kontrolle fizike të nxënësve ose te mjediseve, vetem në raste emergiente ose me vendim nga drejtoria e IA-së


Neni 62 
Të drejtat dhe detyrat e prindërve 
1. Prindërit janë partneri kryesor i institucionit arsimor në mbarëvajtjen e fëmijës dhe të 
institucionit. 
2. Prindi ka të drejtë: 
a) të informohet nga institucioni arsimor përkatës për legjislacionin arsimor në fuqi, për 
rregulloren e institucionit dhe për kurrikulën që institucioni i ofron fëmijës së tij; 
b) të informohet për kushtet e sigurisë, të shëndetit dhe të mjedisit të institucionit dhe të 
kërkojë përmbushjen e tyre sipas standardeve të përcaktuara nga legjislacioni shqiptar; 
c) të informohet për veprimtarinë e fëmijës së tij në institucion dhe të japë pëlqim për 
veprimtaritë plotësuese dhe jashtëshkollore që organizon shkolla; 
ç) të vihet në dijeni  për drejtimet kryesore të veprimtarisë së institucionit dhe arritjet e 
institucionit në krahasim me institucione të ngjashme. Prindi ka detyrë: 
a) të kujdeset që fëmija i tij të ndjekë rregullisht institucionin arsimor dhe të mësojë 
rregullisht; 
b) të njoftojë për ndryshime të shëndetit dhe të sjelljes së fëmijës së tij; 
c) të marrë pjesë në takimet për çështje që kanë të bëjnë me fëmijën e tij; 
ç) të kontribuojë në mbarëvajtjen e institucionit. 

Neni 89
Tö drejta dhe detyra dhe përbërja e këshillit të prindërve të institucionit arsimor
⦁	Këshilli i prinderve është organ i përbërë nga përfaqësues te personave që ushtrojnë përgiegiësinë prindërore të nxënësve të IA-së.
⦁	Këshilli i prindërve te IA-së ka të drejtë:
⦁	të mbrojë dhe të promovojë të drejtat e personave që ushtrojnë përgiegjesine prindërore te nxënësve te institucionit:
⦁	te shprehë pikëpamjet dhe te organizojë personat që ushtrojnë përgjegjesine prindërore per të shprehur pikëpamjet per cilësinë e shërbimit te institucionit dhe te dëgiohet per këto pikëpamje:
⦁	te thërrasë mbledhjen e pergjithshme te personave që ushtrojnë pergiegiësinë prindërore.
⦁	Këshilli i prindërve te IA-së ka per detyre:
⦁	të ndërmarrë nisma për ndihmesën e personave që ushtrojnë përgiegiësinë prindërore per mbarëvajtjen e institucionit dhe t'i realizojë ato në bashkëpunim me drejtorinë e institucionit:
⦁	të organizojë takime te përbashkëta me këshillat e prindërve te klasave.
⦁	Këshilli i prindërve te institucionit përbëhet nga persona që ushtrojnë pergjegjësinë prindërore të zgiedhur nga këshillat e klasave. Numri i personave që ushtrojnë përgiegjësinë prindërore në këshillin e prindërve, percaktohet në rregulloren e brendshme të IA-së. nga giashtë deri në nëntë anëtarë.
⦁	Në mbledhjen e pare te këshillit të prindërve zgjidhet kryetari i tij me shumicë të thjeshtë votash te anëtarëve te këshillit ndërmjet kandidatëve per këtë detyrë.
⦁	Kryetari dhe anëtaret e këshillit te prindërve nuk duhet te jenë në konflikt interesi me drejtorin e institucionit, nuk duhet te kenë precedente penalë dhe të mos jenë në forumet drejtuese të partive politike.
⦁	Në mbledhjen e pare percaktohen detyrat e anëtarëve te këshillit te prindërve.
⦁	Zgiedhjet per këshillin e prindërve të IA-së dhe per kryetarin e tij zhvillohen gdo vit në fillim te vitit shkollor.
⦁	Në këshillin pasues të prindërve te institucionit mund te zgiidhen kryetari dhe anëtarë te këshillit te vitit paraardhës.
Neni 90
Mbledhjet dhe vendimet e këshillit të prindërve të institucionit arsimor
 Këshilli i prindërve mblidhet te paktën tri here në vit. Mbledhje te tjera zhvillohen me nismën e kryetarit te këshillit të prindërve ose të shumicës se thjeshtë të anëtarëve te tij.
⦁	Mbledhja e këshillit te prindërve zhvillohet kur merr pjese shumica e thjeshtë e anëtarëve te tij, përndryshe shtyhet.
⦁	Köshilli i prindërve i merr vendimet me shumicë të thjeshtë votash. Vendimet nënshkruhen nga kryetari dhe sekretari.
⦁	Në mbledhjet e këshillit te prindërve, kryetari ka të drejtë te ftojë anëtarë të këshillave te prindërve te klasave, persona te tjerë që ushtrojnë përgjegjësinë prindërore. drejtues dhe mesues te institucionit, perfaqësues të OJF-ve etj.
⦁	Veprimtaria e anëtarëve të këshillit te prindërve eshte vullnetare.
⦁	Kryetari dhe anëtarët e këshillit të prindërve shkarkohen me shumicë te thjeshte te votave te fshehta të anëtarëve per moskryerje te detyrës, ose kur mungojnë në me shumë se gjysmen e mbledhjeve.
\


Këshilli i prindërve të klasës
  Këshilli i prindërve të klasës jep ndihmesen në permirësimin e cilësisë së shërbimit arsimor për nxënësit e klasës.
⦁	Për gdo klasë. brenda 10 ditëve nga data e fillimit te vitit shkollor, me përkujdesjen e mësuesit kujdestar, zhvillohet mbledhja e pergiithshme e personave ushtrojnë përgiegjësinë prindërore të nxënësve te klasës, ku zgjidhet. me shumicë votash, këshilli i prindërve te klasës, me përbërje nga tre deri në pese veta. Kryetari i këshillit të prindërve te klasës zgiidhet prej këtij këshilli.
⦁	Këshilli i prindërve të klasës mblidhet te paktën n.ië here nö dy muaj. sipas një tematike te planifikuar prej tli, ose me propozimin e mesuesit kujdestar. Ai mund të mblidhet, me nismën e tij, edhe më shpesh.
⦁	Këshilli i prindërve tö klasës kryen detyrat sa më poshtë:
⦁	i propozon mesuesit kujdestar përmirësime ne mbarevajtjen e n,xënësve të klasës:
⦁	dëgion parashtrimet e mesuesit kujdestar dhe i jep këshilla ose i ofron bashkëpunim;
⦁	komunikon me personat ushtrojnë përgiegjësinë prindërore te nxënesve qe rrezikojnë braktisjen e shkollës, Ose mbetjen ne klasë. Ose që kryejne Shkelje te disiplinës.
⦁	Këshilli i prindërve te klasës nxit personat që ushtrojnë përgjegiësinë prindërore te nxënësve te japin ndihmesën e tyre vullnetare:
⦁	Për te punuar me nxënës me vështirësi në të nxënë:
⦁	per tex hartuar ose/dhe Për te vënë në jetë lende ose module me zgiedhje:
⦁	Për te bashkëpunuar ne projekte kurrikulare.
⦁	Këshilli i prindërve të klasës ka të drejtë të ftojë nö mbledhjet e tij mësues te tjerë te klasës, nxënës nga qeveria e nxënësve, anëtarë te drejtorisë, të bordit, tö köshillit tö mesuesve dhe te këshillit te prindërve te shkollës.
⦁	Këshilli prindërve t? klasës ka te drejtë t'i drejtohet drejtorit te IA-se, kryetarit të bordit dhe kryetarit te këshillit te prindërve te shkollës me propozime Për mbarëvajtjen e shkollës.
⦁	Kryetari i këshillit të prindërve të klasës raporton ne mbledhjen e pergiithshme të personave që ushtrojnë pergiegjesine prindërore te nxenesve te klases. si rregull. dy here giate vitit shkollor.
Neni 93
Këshilli Kombëtar i Prindërve dhe Köshilli Rajonal i Prindërve
I . Këshilli Kombëtar i Prindërve është organ köshillimor dhe i pavarur, i cili përfaqëson interesat e personave që ushtrojnë përgiegiësinë prindërore ne nivel kombëtar dhe përbëhet nga përfaqësues të köshillave rajonale te prindërve. Këshilli Kombëtar i Prindërve:
⦁	është mekanizmi kryesor i komunikimit dhe i këshillimit ndërmjet ministrisë dhe personave ushtrojnë pergiegiësinë prindërore;
⦁	përfaqëson interesat e personave që ushtrojnë përgjegjësinë prindërore ne nivel qendror dhe i përcjell mendimet e tij në ministri Për te giitha Gështjet i takojnë arsimit parauniversitar. me qëllim permirësimin e cilësisë;
⦁	bashkëpunon me ministrinë. Këshillin Rajonal të  Prinderve. shoqatat e prindërve dhe me ZV A-te.

Regullorja e brendshme 


RREGULLORE E DISIPLINËS
për 
VEPRIMTARINË E PRINDËRVE/PERSONAVE QË USHTROJNË PËRGJEGJËSINË PRINDËRORE TË NXËNËSVE TË SHKOLLËS 
në zbatim të Urdhërit Nr.31 datë 28.01.2020, udhëzimeve të MAS dhe rregullores së brendshme të shkollës
                                                     
Në institucionin tonë arsimor garantohet e drejta e prindit/personit që ushtron përgjegjësi prindërore për të shprehur pikëpamjet e tyre për cilësinë e shërbimit arsimor dhe për t’u dëgjuar fjala e tyre. Prindi/personi që ushtron përgjegjësi prindërore ka të drejtë të informohet për kurrikulën që institucioni i ofron fëmijës, rregulloren e brendshme të institucionit, kushtet e sigurisë, shëndetit dhe të mjedisit, si dhe masat disiplonore që gjejnë zbatim në institucion.
⦁	Prindi respekton detyrimet e përcaktuara në Kreun XV, të Urdhërit Nr.31 datë 28.01.2020, (nenet 88, 89, 90, 91, 92), urdhrat e MASR dhe Rregullores së Brendshme të shkollës.
⦁	Në zbatim të Urdhrit të MASR nr. 493, dt. 30.07.2018, “Mbi mos përdorimin e celularit gjatë procesit mësimor në shkollë”, prindi duhet të ndërgjegjësojë fëmijën për mos përdorimin e celularit në shkollë. Ai duhet  të bashkëpunoj me shkollën dhe fëmijën në zbatim të urdhrit. Në raste të shkeljes së këtij urdhri, rregullorja parashikon masa disiplinore për nxënësin.
⦁	Prindi ka për detyrë të japë një numër kontakti, i cili të jetë i disponueshëm në çdo kohë dhe të njoftojë menjëherë për ndryshimin e tij, në mënyrë që të sigurohet komunikimi i mësuesit kujdestar me prindin për çdo rast nevoje.
⦁	Prindi e ka të detyruar të njoftojë mësuesin kujdestar për ndryshime të shëndetit dhe të sjelljes, si dhe për problemet shëndetësore kronike të nxënësit.
⦁	Prindi ka për detyrë t’i sigurojë fëmijës ushqim ditor nga shtëpia, pasi në shkollë është e ndaluar futja e ushqimit të pakontrolluar.
⦁	Prindi ka për detyrë të paraqitet në shkollë sa herë që ta shikojë të arsyeshme mësuesi dhe drejtoria.
⦁	Prindi ka për detyrë të njoftojë mësuesin kujdestar në rastet kur fëmija mungon dhe t’i arsyetojë këto mungesa.
⦁	Prindi e ka të ndaluar të kërkojë takim mësuesin kur ky i fundit është gjatë procesit mësimor (bën përjashtim rasti urgjent).
⦁	Pritja në drejtori e prindërve do të jetë nga ora 14:00 – 15:00 (të martë, të mërkurë, të enjte). Bëjnë përjashtim nga ky rregull rastet urgjente.
⦁	Pritja për prindërit nga mësuesit është çdo ditë nga ora 13:15 – 13:40.
⦁	Prindërit duhet të respektojnë kodin e etikës me të gjithë punonjësit e shkollës.
⦁	Prindi ka për detyrë të paraqesë kërkesë me shkrim në drejtori për të marrë leje për nxënësin, ku të citojë afatin, arsyen dhe të paraqesë dokumentacionin që vërteton arsyen (dokumentin mjekësor, apo dokumentacion tjetër që justifikon dhënien e lejes.)
⦁	Prindi ka për detyrë të shlyejë detyrimet për të cilat është vënë në dijeni dhe ka firmosur për to në rastet kur ka qenë dakord.
⦁	Prindi e ka të ndaluar të qëndrojë për të pritur fëmijën e tij në ambientet e brendshme të shkollës.
⦁	Prindi e ka të ndaluar të ngarkojë fëmijën me detyrime familjare të cilat e shtyjnë atë  të lërë orën e mësimit.
⦁	Prindi është i detyruar të ndjeke një çështje ose problem të fëmijës së tij duke respektuar të gjitha hallkat brenda shkollës (mësues kujdestar, mësues i lëndës, komisioni i etikës dhe sjelljes, komisioni i disiplinës, drejtori), para se t’i drejtohet institucioneve të tjera nga të cilat varet shkolla.
⦁	Takimi periodik mësues - prindër zhvillohet 4 – 5 herë në vit sipas këtij grafiku: 

Neni 33 
Komisioni i etikës dhe sjelljes në institucionin arsimor 
Në institucionin arsimor funksionon komisioni i etikës dhe sjelljes, i përbërë nga mësues, prindër dhe nxënës. Komisioni ka për detyrë të shqyrtojë ankesat e nxënësve, të prindërve e të punonjësve të institucionit ndaj shkeljeve të normave të etikës dhe të sjelljes dhe t’i propozojë drejtorit të institucionit masat përkatëse.
Komisioni i etikës dhe sjelljes në institucionin arsimor 
Në institucionin arsimor funksionon komisioni i etikës dhe sjelljes, i përbërë nga mësues, prindër dhe nxënës. Komisioni ka për detyrë të shqyrtojë ankesat e nxënësve, të prindërve e të punonjësve të institucionit ndaj shkeljeve të normave të etikës dhe të sjelljes dhe t’i propozojë drejtorit të institucionit masat përkatëse.
 Neni 34
 Bordi i institucionit arsimor 
⦁	Çdo institucion arsimor ka bordin e tij të përbërë nga prindër, nxënës, mësues, përfaqësues të qeverisë vendore dhe të komunitetit.
⦁	 Bordi kontribuon për mbarëvajtjen e institucionit arsimor dhe i raporton për veprimtarinë e tij këshillit të prindërve të institucionit. 
⦁	. Detyrat kryesore të bordit janë: a) miraton planin afatmesëm dhe atë vjetor të institucionit; b) miraton planin e shpenzimeve të institucionit arsimor për fondet, të cilat sigurohen nga institucioni; c) miraton kurrikulën e hartuar nga institucioni arsimor; ç) merr pjesë në procedurat e emërimit e të largimit të drejtorit të institucionit arsimor dhe të mësuesit. 3. Përbërja e bordit, të drejtat, detyrat e tjera dhe mënyra e zgjedhjes së anëtarëve përcaktohen në udhëzimin e ministrit. 
Neni 35
 Këshilli i mësuesve 1. Këshilli i mësuesve të institucionit arsimor, i cili ka në përbërje të gjithë mësuesit dhe kryesohet nga drejtori, është organ kolegjial këshillimor për drejtimin e veprimtarisë së institucionit. 2. Detyrat dhe funksionet e këshillit të mësuesve përcaktohen me udhëzim të ministrit.
Neni 45
 Dokumentacioni kurrikular 
1. Kurrikula përbëhet nga kurrikula bërthamë, kurrikula me zgjedhje, si dhe kurrikula për veprimtaritë plotësuese. 
2. Ministri, pas konsultimit me Këshillin Kombëtar të Arsimit Parauniversitar, miraton: 
a) kornizën kurrikulare; 
b) planin mësimor për çdo nivel arsimor; 
c) standardet e të nxënit; 
ç) programet lëndore, përveç atyre që hartohen nga institucioni arsimor. 
3. Kurrikula, që hartohet në nivel institucioni arsimor, miratohet nga drejtori i tij pas marrjes së pëlqimit nga njësia arsimore vendore.
Neni 59 
Kualifikimi i mësuesve 1. Kategoritë e kualifikimit të mësuesve janë tri: 
⦁	“Mësues i kualifikuar”
⦁	“Mësues specialist”; 
⦁	“Mësues mjeshtër
Neni 61 
Të drejtat dhe detyrat e nxënësit 1. Nxënësi ka të drejtë:
 a) të përzgjedhë një institucion arsimor, publik ose privat; 
b) të ndjekë institucionin arsimor publik që është në zonën e përcaktuar nga njësia bazë përkatëse e qeverisjes vendore;
 c) t’i sigurohet nga institucioni shërbim arsimor cilësor, sipas interesave, nevojave dhe mundësive të tij, si dhe ndihmë e posaçme për të përballuar vështirësitë e tij të veçanta të të nxënit; 
ç) të informohet për të drejtat e detyrimet e tij, rregulloren e institucionit arsimor, për kurrikulën që institucioni i ofron, për format e vlerësimit, për provimet kombëtare, si dhe të vihet në dijeni me shkrim për rezultatet e ndërmjetme dhe përfundimtare të arsimimit të tij; 
d) të shprehë pikëpamjet për çështje të arsimimit të tij, të ankohet për qëndrimet ndaj tij dhe të ketë vëmendjen e punonjësve të institucionit arsimor për këto pikëpamje e ankesa; 
dh) të zgjidhet në bordin e shkollës pas moshës gjashtëmbëdhjetë vjeç; 
e) të transferohet nga një shkollë në një shkollë tjetër të të njëjtit nivel arsimor.
 2. Nxënësi ka detyrë: 
a) të respektojë të drejtat e nxënësve të tjerë dhe të punonjësve të institucionit, të njohura me ligj; 
b) të mësojë rregullisht;
 c) të vijojë rregullisht dhe të marrë pjesë në veprimtari të tjera të institucionit; 
ç) të respektojë rregullat e institucionit për mbrojtjen e shëndetit, të sigurisë e të mjedisit dhe të kërkojë respektimin e tyre nga nxënësit e tjerë dhe punonjësit arsimorë;
 d) të respektojë rregulloren e institucionit.




KREU V
KURRIKULA E GJIMNAZIT
Neni 16
Kurrikula e giimnazit
I. Kurrikula e giimnazit bazohet në LAPU dhe në aktet ligiore e nënligjore në fuqi.
⦁	Zbatimi i kurrikulës në giimnaz mbështetet në dokumentet kurrikulare dhe në udhëzimet e ministrit.
⦁	Kurrikula e gjimnazit është e organizuar në kurrikul bërthamë. kurrikul me zgiedhje dhe kurrikul në baze shkolle.
⦁	Kurrikula bërthamë është e detyruar dhe e përbashkët për të giithë nxënësit.
⦁	Kurrikula me zgiedhje fokusohet ne zgiedhjen e Iëndëve/moduleve që nuk zhvillohen në kurrikulën bërthamë.
⦁	Kurrikula në bazë shkolle nuk është e detyruar për nxënësin; ajo i mundëson nxënësit të zhvillojë aftësitë nëpërmjet moduleve kurrikulare, projekteve ndërkurrikulare apo veprimtarive të tjera shkollore.
⦁	Shkolla ka detyrimin ťi sigurojë secilit nxënës:
⦁	kurrikulën bërthamë të plotë:
⦁	numrin e orëve mësimore të kurrikulës me zgjedhje.
⦁	numrin e orëve për shërbimin komunitar.
Neni 17
Procedurat për kurrikulën me zgjedhje në gjimnaz
⦁	Drejtori i IA-së, mësuesit kujdestarë dhe ekipet Iëndore:
⦁	informojnë nxënësit për listën e lëndëve/moduleve me zgjedhje që ofron shkolla për secilën klasë;
⦁	sigurojnë formularët përkatës për ťu plotësuar nga nxënësit.
⦁	Nuk Igiohet që nxënësi ta ndërrojë lëndën me zgiedhje gjatë vitit shkollor.
Neni 18
Planifikimi i mësimdhënies në giimnaz
I. Planifikimi i mësimdhënies në giimnaz përfshin: planifikimin lëndor vjetor të ndarë në periudha. planifikimin për secilën periudhë dhe planifikimin ditor.
⦁	Në fillim të vitit shkollor. mësuesi dorëzon në drejtorinë e shkollës Planin vjetor te lëndës. i cili është një kornizë e ndarjes së përgiithshme të përmbajtjes Iëndore dhe të orëve mësimore, si edhe Planin e periudhës së parë. Planet e periudhës së dytë dhe të tretë dorëzohen para fillimit të secilës periudhë.
⦁	Gjatë vitit, sipas rrethanave që i krijohen. mësuesi mund të bëjë ndryshime në Planin fillestar të periudhës, ndryshime te cilat miratohen nga drejtor nga i i IA-së.



VI
VLERËSIMI 1 NXËNËSIT NË KLASAT I-XII
Neni 20
Vleresimi i nxënësit në arsimin parauniversitar
⦁	Nota perfundimtare përfshin notat vjetore si me poshtë:
⦁	notën vjetore të vlerësimit të vazhduar per tri periudhat;
⦁	noten vjetore te vlerësimit me test ose detyrë permbledhëse per tri periudhat;
⦁	notën vjetore të vleresimit të portofolit të nxënësit per tri periudhat.
⦁	Mësuesi mban te dhëna gjate giithë vitit shkollor per vlerësimin e nxënësit. Vlerësimi i vazhduar. testet/detyrat përmbledhëse dhe portofoli i nxenesit ruhen në shkollë dhe jane objekt monitorimi në gdo periudhë te vitit shkollor.


⦁	Nxënësi eshtë mbetës në klasë. kur:
⦁	eshtë jokalues në te paktën tri lëndë;
⦁	ështe jokalues të pakten në një lëndë në sesionin e dytë;
⦁	ka masen disiplinore "Ulje e notes në sjellje" dhe nuk e ka permiresuar ate deri në përfundim te vitit mësimor:
q) figuron i paklasifikuar per shkak te mungesave.
KREU Vll
INSTITUCIONET ARSIMORE
Neni 24
Organizimi i mësimit në shkollë
⦁	Me propozim te drejtorit te IA-së dhe miratim të titullarit të ZVA-së, shkolla funksionon me dy ndërresa. Mësimi, si rregull. në te gjitha shkollat e ndërresës së pare fillon në orën 8.00. per ndërresën e dytë dhe per arsimin me kohë te pjesshme, ora e fillimit te mesimit miratohet nga titullari i ZVA-se.
⦁	Drejtori i IA-së cakton mësues ditor per te lehtësuar mbarëvajtjen e shkollës. Detyrat e mesuesit ditor përshkruhen në rregulloren e brendshme te shkollës.
⦁	NE kushte të rënduara të motit, te terrenit, ose per arsye te transportit rrugor. drejtori i IA-se vendos ndryshimin perkohësisht të ores së fillimit të mesimit me miratim të titullarit të ZVA-së.
⦁	Ndermjet orëve te mesimit, pushimi është 5 ose 10 minuta. Këshilli i mesuesve vendos kohën kur shkolla do të bëjë pushimin e madh, i cili mund te zgiate 20 deri ne 30 minuta.
⦁	Kohëzgiatja e orës së mësimit në shkollë është 45 minuta.
⦁	Ora e mesimit është e pacenueshme, me perjashtim te rasteve të veganta, kur cenohet shëndeti dhe siguria fizike e nxënësve. 
Neni 36
Komisioni i etikës dhe sjelljes në institucionin arsimor
 Për të ndjekur çështjet kanë të me etikën. në çdo IA. në çdo fillim viti shkollor ngrihet dhe funksionon komisioni i etikës dhe sjelljes. Drejtori i IA-së organizon procesin për ngritjen e komisionit të ri për çdo vit shkollor.
⦁	Komisioni funksionon mbi bazën e rregullores hartohet nga ai vetë, të eilën ia paraqet për miratim drejtorit të IA-së.
⦁	Komisioni përbëhet nga mësues, persona ushtrojnë përgiegjësinë prindërore dhe nxenes, me te pakten 5 (pesë) anëtarë.
⦁	Nt: IÀ-të me më pak se 24 klasa, komisioni përbëhet nga pesë anëtarë, kurse në ato me të paktën 24 klasa përbëhet nga shtatë anëtarë.
⦁	Numri i mësuesve. personave ushtrojnë përgjegiësinë prindërore dhe nxënësve në komision përcaktohet në rregulloren e brendshme te IA-së.
⦁	Mësuesit ne komision zgiidhen me shumicë të thieshtë të votave nga këshilli i mësuesve. Prindërit zgiidhen nga këshilli i prindërve të IA-së me shumicë të thjeshtë të votave. Nxënësit zgjidhen nga qeveria e nxënësve me shumicë të thjeshtë votash,
⦁	Në komision bëjnë pjesë nxënes të moshës mbi 14 vjeç.
⦁	Drejtori i IA-së nuk bën pjesë në komision.
Neni 37
Anëtarët e komisionit të etikës dhe sjelljes
 Për organizimin e punes, anetaret e komisionit caktojnë. në mbledhjen e parë. një kryetar dhe një sekretar.
⦁	Kryetari i komisionit merret me organizimin e veprimtarisë së komisionit.
⦁	Sekretari ndihmon në dokumentimin e veprimtarisë së komisionit përmes mbajtjes dhe zbardhjes së procesverbaleve të mbledlujeve.
⦁	Në rregulloren e komisionit mund të percaktohen detyra te tjera specifike per kryetarin, sekretarin dhe anëtarët.
⦁	Anetari i komisionit largohet:
⦁	kurjep dorëheqien:
⦁	kur shumica e anëtarëve vendosin përjashtimin e tij:
i. per shkelje të normave të etikes dhe sjelljes që bien në kundërshtim me veprimtarinë e komisionit•, ii. kur vihet në dyshim integriteti i tij, per shkak të procedimeve administrative, civile, penale që vijojnë ndaj tij; iii. kur mungon në tri mbledhje radhazi në mënyrë te pajustifikuar.
⦁	Kur pozicioni i anëtarit mbetet i lire. anëtari i ri zgjidhet me të njëjtën procedure sig ishte zgjedhur anëtari i larguar.
Neni 38
Parimet e komisionit tö etikës dhe sjclljes
 Komisioni, në ushtrimin e veprimtarisë së tij, zbaton kërkesat e legjislacionit në fuqi dhe udhëhiqet nga parimet e mëposhtme:
⦁	parimi i barazise dhe mosdiskriminimit:
⦁	parimi i paanësisë në vendimmarrje:
⦁	parimi i transparences;
g) parimi i shqyrtimit brenda një afati kohor te arsyeshëm;
d) parimi i mbroj!ies së te dhënave personale.
2. Anëtaret e komisionit nuk janë pjesë e shqyrtimit dhe vendimmarrjes, në rastet kur ndodhen në kushtet e konfliktit të interesit.
Neni 39
Veprimtaria e komisionit të etikös dhe sjelljes
l . Komisioni trajton te gjitha ankesat që i paraqiten me shkrim brenda objektit te veprimtarisë se tij. Ankesat i paraqiten komisionit sipas shtojcës nr. 6 te kësaj Rregullores 31
2. Komisioni, me nismën e tij. mund të trajtojë raste të shkeljes së etikës te kryera nga punonjësi arsimor, të cilat vijnë në kundërshtim me rregullat e parashikuara në Kodin e Etikës dhe në aktet e tjera në fuqi. Propozimin e tij per mase disiplinore e percjell te drejtori i IA-së. per t'u trajtuar në komisionin e disiplinës.
3, Komisioni ka të drejtë te therrasë palët për t'i ballafaquar.
4, Komisioni shqyrton dhe giykon në bazë të fakteve e provave të administruara në seancën dëgjimore per palën ndaj te cilës propozohet masa disiplinore. Në rastet kur vërtetohet se pala ka kryer shkelje te etikës dhe rregullores së brendshme përveç rasteve kur ato perbëjnë vepër penale, komisioni propozon masa sipas përcaktimeve në aktet ligiore dhe nënligjore në fuqi.
⦁	Ne  rastet kur ankues është nxënësi. komisioni ka detyrimin qe në proceduren e ballafaqimit të kete të pranishëm psikologun apo punonjësin social.
⦁	Komisioni, në përfundim të shqyrtimit te ankesës i propozon drejtorit të IA-së masen disiplinore per vështjet e ngritura në ankesë, në përputhje me parashikimet e rregullores. Vendimmarrja i takon komisionit të disiplinës.
⦁	Komisioni njofton palët per përfundimin e shqyrtimit te ankesës, sipas të dhënave në percaktuara në shtojcën nr. 7 te kësaj Rregulloreje.
⦁	Komisioni, në veprimtarinë e tij. kryen edhe detyrat si vijon:
⦁	ofron rekomandime per fu zbatuar nga punonjësit arsimorë ne funksion te standardeve te Kodit te Etikës:
⦁	siguron një sistem tö vazhdueshëm informimi Për rëndësinë e integritetit te punonjësit arsimor:
⦁	ndjek nivelin drejtues e administrues të IA-se dhe sigurohet qe ai eshtë sipas standardeve tä Kodit te Etikës.
Neni 40
Mbledhjet e komisionit të etikës dhe sielljes
I . Komisioni mblidhet sa here që paraqitet një ankesë dhe/ose me nismën e tij ne lidhje me çështje që perfshihen ne objektin e veprimtarisë se tij, por jo me pak se katër here gjatë nje viti shkollor.
⦁	Mbledhja e komisionit zhvillohet kur merr pjesë shumica e thjeshtë e anëtarëve te tij; në rast të kundërt, mbledhja shtyhet.
⦁	Komisioni i merr vendimet me shumicë te thjeshte votash. Vendimet nënshkruhen nga të gjithë anetarët e pranishëm.
KREU Xll
MËSUESI DHE PUNON.JËSI ARSIMOR
Neni 56
TE drejta dhe detyra te mësuesit
I. Mësuesi ka te drejtë:
⦁	të kryeje punën në kushte të sigurta per jetën dhe shëndetin e tij:
⦁	të trajtohet me respekt, me dinjitet. në mënyre të kulturuar dhe të moralshme nga kushdo. pa presione. pa padrejtësi, pa fyerje. pa diskriminim;
⦁	fi sigurohen kushtet e mjaftueshme per mësimdhënie efektive;
q) te informohet në kohë nga drejtori i IA-se per dokumentet zyrtare që kanë lidhje me veprimtarinë e tij;
⦁	te ketë. në përputhje me legiislacionin ne fuqi, liri profesionale në zbatimin dhe zhvillimin e kun-ikulës:
dh) ti krijohen mundesitë per zhvillim profesional;
⦁	të marrë piesë në veprimtari shkencore vendore. kombëtare e ndërkombëtare.
2. Mësuesi ka per detyrë:
⦁	të permbushë detyrimet qe lidhen me ushtrimin e profesionit te mesuesit;
⦁	të zbatojë Kodin e Etikës së Mësuesit;
⦁	te trajtojë këdo, ne mjediset e IA-së, me respekt. me dinjitet, në mënyrë të kulturuar dhe te moralshme, pa presione, pa padrejtesi, pa fyerje, pa diskriminim. pa dhunë;
g) të përkuideset per mbarëvajtjen e qclo nxënësi të tij;
⦁	ti jape ndihmesën e tij per mbarëvajtien e institucionit ku punon; 
⦁	dh) të kërkoje të shqyrtohen në drejtorine. këshillin e mësuesve, këshillin e prindërve dhe bordin e institucionit çeshtje që shqetësojnë cilesinë e shërbimit arsimor në institucion;
⦁	te kryejë me pergiegiësi detyra që i ngarkohen në provimet kombëtare dhe në testimet ndërkombëtare.
Neni 57
Punonjösi arsimor, psikologu, punonjësi social, oficeri i sigurisö dhe sekretari
I. Punonjësi arsimor. psikologu, punonjësi social, oficeri i sigurisë dhe sekretari respektojnë Kodin e Etikës së Mësuesit.
⦁	Në veçanti, punonjësi arsimor, psikologu, punonjësi social, oficeri i sigurisë dhe sekretari e ka te ndaluar:
⦁	te ushtrojë dhune fizike ose psikologjike ndaj nxënësve ose kolegëve;
⦁	ta largojë nxënësin nga klasa dhe shkolla per çështje a nevoja vetjake te tij;
⦁	te bëjë kurse private me nxënesit e shkollës se tij:
 të pijë duhan ose pije alkoolike ne institueionin arsimor,
⦁	të ketë marrëdhenie me para me nxënesit ose personat qe ushtrojnë përgjegjësinë prindërore te tyre:
dh) Ti detyroje nxënësit te blejnë literature që nuk perfshihet ne katalogun e teksteve shkollore;
⦁	T’u deklarojë nxënësve bindjet e tij partiake ose fetare:
ë) Të detyrojë nxënësit ose mësuesit të marrin pjesë ne veprimtari partiake ose fetare;
⦁	Të përdorë celularin giatë procesit të mësimit.
⦁	Punonjësi arsimor, psikologu, punonjësi social, oficeri i sigurisë dhe sekretari nuk merr pjesë ne grupe pune që kane me te konflikt interesi.
⦁	Ne IA-të, publike dhe private, ndalohet propaganda dhe organizimi i veprimtarive:
⦁	partiake:
⦁	fetare
⦁	Ndalime te tjera te punonjësit arsimor. psikologut, punonjësit social, oficerit të sigurisë dhe sekretarit, pershkruhen ne rregulloren e brendshme te IA-së, në përputhje me Kodin e Punës. Kodin e Etikës, Kontratën Kolektive dhe aktet e tjera nënligiore ne fuqi.
⦁	Punonjësit arsimorë. psikologu. punonjësi social, oficeri i sigurisë dhe sekretari i IASë mbajnë uniformë giatë qëndrimit nö mjediset e institucionit. Uniforma per punonjësit arsimorë percaktohet nga këshilli i mësuesve dhe është e detyrueshme per zbatim.
⦁	Pör mungesën ne pune, punonjësi arsimor, psikologu. punonjësi social, oficeri i sigurisë dhe sekretari njofton paraprakisht titullarin e tij.
⦁	Mungesat e punonjesve arsimorë te institucionit, përfshire drejtuesit. trajtohen ne përputhje me Kodin e Punes.
Neni 59
Koha e punës nö institucionet arsimore publike
 Drejtuesit dhe mesuesit e IA-ve publike paraqiten ne shkollë 15 minuta para fillimit tö orarit mesimor te LA-së.
⦁	Drejtuesit dhe mësuesit e IA-ve publike qëndrojnë 30 orë në javë në mjediset e shkollës ose në miedise të tjera për të kryer veprimtaritë e planifikuara mësimore dhe _iomësimore, përfšhirë veprimtaritë jashtëshkollore. mbledhjet profesionale. takimet me personat që ushtrojnë përgjegiësinë prindërore të nxënësve, plotësime të dokumentacionit dhe pjesëmarrjen në grupet e punës.
⦁	Punonjësi arsimor. psikologu, punonjësi social. oficeri i sigurisë dhe sekretari mund të paraqitet ne punë me vonesë. ose të largohet giatë kohës së punës, vetëm për arsye të veęanta, duke njoftuar menjëherë drejtorin e IA-së.
⦁	Punonjësi arsimor lejohet të largohet giatë ditëve të mësimit për të marrë pjesë në veprimtari shkencore. artistike. kulturore apo sportive vendore. kombëtare e ndërkombëtare, duke marrë paraprakisht miratimin e drejtorit. Drejtori njofton titullarin e ZVA-së dhe merr masa për të bërë zëvendësimin.
Neni 60
Plani lëndor i mësuesit. Aspekte të zbatimit të tij
 Pesë ditë-punë para lillimit të vitit shkollor, mësuesi dorëzon Planin lëndor te drejtori i IA-së, si dhe Planin lëndor të periudhës së parë.
⦁	Mësuesi harton Planin lëndor sipas Kornizës Kurrikulare. programit përkatës të Iëndës ose fushës së të nxënit. pikëpamjeve të tij pedagogiike dhe në përshtatje me nxënësit e tij.
⦁	Gjatë vitit mësimor, kur krijohen rrethana te reja, mësuesi mund të bëjë ndryshime në Planin Iëndor. Cdo ndryshim miratohet nga drejtori i shkollës dhe pasqyrohet në Planin e dorëzuar ne drejtori.
⦁	Plani lëndor i mësuesit shqyrtohet në ekipin lëndor përkatës dhe merr trajtën përfundimtare pas këtij shqyrtimi.
Neni 64
Këshilli i mësuesve
 Këshilli i mësuesve ka për detyrë:
⦁	te zbatojë aktet e legjislacionit arsimor në fuqi•,
⦁	të këshillojë përmirësime në drejtimin e institucionit arsimor;
⦁	të analizojë periodikisht rezultatet e nxënësve;
q) të këshillojë përmirësimet në veprimtarinë e IA-së që ęojnë në rezultatet më të mira të nxënësve:
⦁	të shqyrtojë rregullisht përvojat e suksesshme të mësuesve të institucionit dhe të sugjerojë përhapjen e tyre në institucion; dh) të shqyrtqië praktikat e suksesshme të kolegëve të IA-ve vendase dhe te sugjerojë mënyrat e zbatimit të tyre:
⦁	te kryejë studime për praktikat e suksesshme të institucioneve analoge të huaja dhe të sugierojë mënyrat e zbatimit të tyre.
⦁	Këshilli i mësuesve mblidhet. si rregull, jo më pak se një herë në dy muaj. Këshilli mblidhet edhe në rastet kur e giykon të arsyeshme drejtori i IA-së, ose kur e kërkon jo më pak se 1/3 e anëtarëve të tij. Këshilli i mësuesve e zhvillon mbledhjen e pare të paktën IO (dhjetë) ditë-punë para fillimit të vitit shkollor. Në këtë mbledhje. këshilli i jep mendime drejtorit për formimin e klasave. për orarin mësimor, për tematikat e përafčrta te mbledhjeve të zakonshme të këshillit, për veprimtaritë e zhvillimit të brendshëm profesional dhe per ęështje të tjera, sipas kërkesës së drejtorit ose me nismën e këshillit.
⦁	Në përfundim të vitit mësimor, këshilli i mësuesve analizon veprimtarinë vjetore të institucionit dhe rekomandon synimin dhe objektivat e planit për vitin e ardhshëm.
⦁	Në mbledhjet e këshillit të mësuesve. drejtori ka të drejtë të ftojë:
⦁	përfaqësues të NjVV-së dhe të ZVA-së;
⦁	punonjësin psiko-social:
⦁	kryetarin e bordit;
ț) kryetarin e këshillit të prindërve;
⦁	kryetarin e qeverisë sä n,xenësve; dh) kryetarin e komisionit te etikës dhe sjelljes:
⦁	personelin mjekësor te shkollës (kur ka të tillë);
ö) pörfaqësues të tjerë nga komuniteti.
⦁	Drejtori cakton një mësues si sekretar te keshillit. Sekretari mban shenimet e mbledhjeve ne librin e procesverbaleve të këshillit të mesuesve dhe vendos ne arkivin e institucionit materialet e paraqitura në këshill nga drejtuesit e institucionit dhe mësuesit, te eilat ruhen Për tri vite shkollore. Dokumentacioni i këshillit tö mësuesve Eshtë Objekt monitorimi dhe vlerësimi.
Neni 65
Ekipi lëndor
 Ekipi lëndor Eshtë forme e zhvillimit të brendshëm profesional të IA-Së dhe perbëhet nga mësues te shkollës, të cilët japin mësim ne po ate lëndë a fushë te nxëni, Ose ne më shumë se një fushë të nxëni.
⦁	Drejtori i shkollës, pas këshillimit me këshillin e mesuesve, ngre ekipet lëndore.
⦁	Ekipi lëndor mblidhet një here ne muaj.
⦁	Në mbledhjet e ekipit lëndor:
⦁	diskutohen aspekte te praktikave tö përditshme profesionale të mësuesve;
⦁	trajtohen Gështje te integrimit ndërlëndor:
⦁	shqyrtohen përvoja të suksesshme të kolegëve dhe praktika vendase e të huaja:
g) shtjellohen probleme qe ekipi lëndor i qmon të dobishme per zhvillimin profesional te mësuesve;
⦁	shqyrtohen planet Iëndore vjetore dhe të periudhës të mesuesve, para dorëzimit të tyre ne drejtorinë e IA-se.
5, Në mbledhjet e ekipit Iëndor frohen mësues te tjerë te asaj shkolle Ose të shkollave të tjera dhe specialiste te kurrikulës.
Ekipi lëndor nuk merr vendime.
Kryetari i ekipit löndor duhet te plotësojë këto kritere:
⦁	te ketë punuar te paktën 5 vjet si mësues në po ate nivel arsimor;
⦁	tö jetë vleresuar me tö paktën "Shumë mirë?" në provimin e kualifikimit, nëse e ka dhënë këtë provim;
⦁	te shquhet për rezultate te nxënesve te tij.
Kryetari i një ekipi lëndor propozohet nga anëtarët e ekipit përkatës dhe caktohet nga drejtori.
Kryetari i ekipit lëndor ka për detyrë të përgatisë dhe të drejtojë mbledhjet e ekipit.
Procesverbalet e mbledhjeve të ekipit lëndor ruhen për një vit shkollor nga kryetari i tij.
Neni 66
Mësuesi kujdestar i klasës dhe orët e kujdestarisë
 Mësues kujdestar i një klase te arsimit  te mesëm te lartë Eshtë një nga mesuesit lëndorë të klasës. 

Mësuesi kujdestar përkujdeset posaçërisht per:
⦁	krijimin e atmosferës se mirëkuptimit dhe të bashkëpunimit në mes nxënësve:
⦁	nxenësit me aftesi te veganta (me aftësi tö kufizuara, me veshtirësi ne të nxënë. të talentuar);
⦁	nxënësit e sapoardhur dhe ata me shqetesime tä sjelljes:
g) ndjekjen e shkollës nga të giithë nxënësit;
⦁	plotësimin e pëlqimeve te nxënësve per kurrikulën me zgjedhje; 
  shmangien e mbingarkesës Së nxënësit me mësime:
⦁	keshillimin e nxenësve ne zgiedhjet kurrikulare dhe zgiedhjet e karrieres;
ö) bashkëpunimin e tij me psikologun!punonjësin social:
⦁	plotësimin e faqeve të SMIP
⦁	Orët e kujdestarisë janë 2 orë në jave. te cilat përfshijnë:
⦁	veprimtari me klasën:
⦁	piotësim dokumentacioni•,
⦁	takime e komunikim me personat ushtrojnë përgiegiësine prindërore të nxënësve.
⦁	Orët e kujdestarisë nuk shënohen ne orarin e mësimeve te klasës/shkollës.
⦁	Mësuesi kujdestar, ne bashkëpunim me këshillin e prindërve të klasës. harton planin vjetor te punes. i eili miratohet nga drejtori i IA-se. NE këte plan përfshihen dhe takimet me të giithë personat që ushtrojne përgiegiësinë prinderore të nxënësve te klasës.

Neni 67
Bashkëpunimi i mësuesit kujdestar me prindërit
l . Mësuesi kujdestar njeh personat ushtrojnë përgjegiësinë prindërore të n.xënësve dhe nxënësit me:
⦁	kushtet e shëndetit dhe tö sigurisë në IA;
⦁	dispozitat e kësaj Rregulloreje që shtjellojnë tö drejtat dhe detyrimet e personave që ushtrojnë pergjegiësinë prindërore dhe te nxënësve ndaj institucionit;
⦁	detyrimet e punonjësve të IA-se ndaj personave që ushtrojnë përgiegjësinë prindërore dhe të nxënësve:
g) rregulloren e brendshme tö institucionit;
⦁	kurrikulën me zgjedhje; 
⦁	
⦁	procedurat e zhdëmtimeve;
ë) procedurat e ankimit.
⦁	Mesuesi kujdestar ka për detyrë:
⦁	te informojë rregullisht personat që ushtrojnë përgjegiësinë prindërore rreth mbarëvajtjes së fëmijëve te tyre;
⦁	te takojë me perparësi personat që ushtrojnë pergiegiësinë prindërore te nxënësve me veshtirësi ne te nxënë. me sjellje shqetesuese ose me probleme ne ndjekjen e shkollës;
⦁	te shtojë interesimin e personave ushtrojne përgiegiësinë prindërore për mbarëvajtjen e fëmjëve të tyre.
⦁	Mësuesi kujdestar fton ne mbledhje tö përgiithshme te giithë personat ushtrojnë përgiegiësinë prindërore, bashkë me nxënësit Ose pa ata, te pakten n.ië here ne tre muaj. ku:
⦁	parashtron çështje që i takojnë klasës ne tërësi:
⦁	shtjellon tema rreth rolit të personave ushtrojnë pergjegiësinë prindërore ne suksesin ei fëmijëve të tyre.
⦁	Mësuesi kujdestar e ka te ndaluar që në mbledhjet me personat ushtrojnë përgjegiösinë prindërore të nxënësve të përmendë me emër nxënës të klasës per mosarritie ose arritje te tyre. Informacioni per nxenesin u jepet vetern personit që ushtron pergiegjësinë prindërore të tij.
Neni 68
Trajtimi i sjelljeve të dhunshme të nxënësve ndaj punonjösit arsimor
I . Në rastin kur punonjësi arsimor konstaton përdorimin e dhunes verbale. psikologiike, fizike. seksuale nga ana e nxënesit. me ane te shprehjeve dhe/ose veprimeve te ndryshme. lajmëron menjëherë drejtorinë e IA-se.
⦁	Drejtoria e IA-se lajmëron personin që ushtron përgiegiësinë prindërore të n,xënësit per menaxhimin e konfliktit dhe zgjidhjen e situatës.
⦁	Drejtoria e IA-së, ne raste të tilla bashkëpunon me mësuesin kujdestar. me psikologun/punonjësin social. si dhe me oficerin e sigurisë në shkollë. ne IA-së të cilët ka oficer sigurie, per trajtimin në vazhdimësi të nxënësit që shpreh sjellje të dhunshme ne ambientet e IA-së giatë procesit mësimor apo/dhe jashtë tij.
⦁	Në rastin kur sjellja e dhunshme e shfaqur nga nxënösi përbën veper penale, drejtori i IA-Së ka detyrimin te njoftojë menjëherë ZVA-ne. NjMF dhe organet vendore te Policisë Së Shtetit per ndjekjen e çështjes.
Neni 82
Mësuesi ndihmës në institucionin arsimor të zakonshöm
 Per f'ëmijët me aftësi te kufizuara në në IA-te publike caktohet mësues ndihmës.
2. Disa nga detyrat e mësuesit ndihmës janë:
⦁	të jape ndihmesën e tij per zhvillimin e plotë te potencialit intelektual e fizik të
n.xënësve me AK:
⦁	të bashkëpunojë me mësuesin ose mesuesit Iëndorë. mësuesin kujdestar dhe psikologun/punonjësin social per gjithëpërfshirjen e nxënësve me AK në IA-të e zakonshme:
⦁	te asistojë nxënësin me AK sipas nevojave giatë procesit mësimor, brenda dhe jashtë klase, per të bërë te mundur pjesemarrjen e tij sa më të plotë në veprimtaritë shkollore;
⦁	të hartojë. në bashkëpunim me mësuesin e nxënësit me AK/mësuesit lëndorë dhe personin që ushtron përgiegiësinë prindërore, dhe te zbatojë programin edukativ individual (PEI) te n.xënësit, te miratuar nga komisioni i IA-së per fünijët me AK.

a) Për kategorinë e kualifikimit “Mësues i kualifikuar”:
i. 3 vjet punë si mësues;
ii. 30 kredite zhvillim profesional për tre vjet. Mësuesi çdo vit duhet të marrë 10 kredite: të paktën
50% e krediteve të ZHVP-së duhet të jenë të lidhura me aspekte metodologjike të zbatuara në
fushën/profilin që mbulon; të paktën 70% e krediteve të ZHVP-së duhet të jenë në aktivitete të
drejtpërdrejta; 80% e krediteve totale të ZHVP-së duhet të jenë nga aktivitetet e akredituara në
nivel kombëtar;
iii. vlerësimin e performancës nga drejtori i shkollës “Mirë” ose “Shumë mirë”.
b) Për kategorinë e kualifikimit “Mësues specialist”:
i. 8 vjet punë si mësues, nga të cilat 5 vjet punë pas fitimit të kategorisë “Mësues i kualifikuar”;
ii. 50 kredite zhvillim profesional për pesë vjet pas fitimit të kategorisë “Mësues i kualifikuar. Çdo vit
mësuesi duhet të marrë 10 kredite: të paktën 50% e krediteve të ZHVP-së duhet të jenë të
lidhura me aspekte metodologjike të zbatuara në fushën/profilin që mbulon; të paktën 70% e
krediteve të ZHVP-së duhet të jenë në aktivitete të drejtpërdrejta; 80% e krediteve totale të
ZHVP-së duhet të jenë nga aktivitetet e akredituara në nivel kombëtar;
iii. vlerësimin e performancës nga drejtori i shkollës “Mirë” ose “Shumë mirë”.
c) Për kategorinë e kualifikimit “Mësues mjeshtër”.
i. 15 vjet punë si mësues nga të cilat 7 vjet punë pas fitimit të kategorisë “Mësues specialist”;
ii. 70 kredite zhvillim profesional për shtatë vjet pas fitimit të kategorisë “Mësues specialist”. Çdo vit
mësuesi duhet të marrë 10 kredite: të paktën 50% e krediteve të ZHVP-së duhet të jenë të
lidhura me aspekte metodologjike të zbatuara në fushën/profilin që mbulon; të paktën 70% e
krediteve të ZHVP-së duhet të jenë në aktivitete të drejtpërdrejta; 80% e krediteve totale të
ZHVP- së duhet të jenë nga aktivitetet e akredituara në nivel kombëtar;
iii. vlerësimin e performancës nga drejtori i shkollës “Shumë mirë”.
Neni 107
Masat disiplinore për mësuesit dhe nöndrejtorin
 Komisioni i disiplinës i IA-se jep masën disiplinore për mësuesin ose nëndrejtorin. kur:
⦁	konstaton shkelje të legiislacionit ne fuqi Për arsimin parauniversitar. te kësaj rregulloreje Ose të rregullores brendshme të institucionit;
⦁	konstaton shkelje të dispozitave tö Kodit te Etikës e te sjelljes në institucion:
⦁	konstaton rezultate fiktive te përsëritura te n.xënësve. të verifikuara ne mënyrë objektive. nepërmjet testimeve të drejtorisë Së institucionit ose te DRAP-se apo rezultateve ne provimet kombëtare;
G) drejtori i shkollës konstaton se nendrejtori nuk kryen detyrat e tij sipas përshkrimit të tij te punës.
⦁	Masat e pershkallëzuara që komisioni i disiplinës vendos Për mësuesin Ose nëndrejtorin. ne varesi te Ilojit te shkeljes apo përsëritjes Së të njëjtës shkeljeje. janë:
⦁	qortim;
⦁	verejtje:
⦁	paralajmerim Për largim nga puna:
G) largim nga puna
⦁	Në rastin e përsëritjes Së shkeljes nga mësuesi/nëndrejtori. i eili Për atë shkelje ka marrë me parë masën " Masa është e shlyer kur, Për një periudhë giashtëmujore. komisioni i disiplinës nuk ka shqyrtuar Shkelje tjetër te mësuesit/nendrejtorit.
⦁	Në rastet kur mësuesi/nëndrejtori ka ushtruar dhunë ndqi nxënësve ose punonjësve te institucionit, dhe këto veprime janë te provuara. jepet mase disiplinore "Largim nga detyra", pörveq veprimeve te tjera mund te ndiqen nga strukturat kompetente sipas legiislacionit ne fuqi.
⦁	Paralajmërim Për largim nga puna", komisioni i disiplinës i propozon drejtorit të IA-së fillimin e procedurave për largimin nga puna te mesuesit/nëndrejtorit.
⦁	Në rastin e përsëritjes Së shkeljes nga mësuesi/nëndrejtori. i eili Për atë shkelje ka marrë me parë masën " Masa është e shlyer kur, Për një periudhë giashtëmujore. komisioni i disiplinës nuk ka shqyrtuar Shkelje tjetër te mësuesit/nendrejtorit.
⦁	Në rastet kur mësuesi/nëndrejtori ka ushtruar dhunë ndqi nxënësve ose punonjësve te institucionit, dhe këto veprime janë te provuara. jepet mase disiplinore "Largim nga detyra", pörveq veprimeve te tjera mund te ndiqen nga strukturat kompetente sipas legiislacionit ne fuqi.
⦁	Paralajmërim Për largim nga puna", komisioni i disiplinës i propozon drejtorit të IA-së fillimin e procedurave për largimin nga puna te mesuesit/nëndrejtorit.

 Rregullorja e Brendshme 

⦁	Mësuesi duhet të respektojë me korrektësi orarin e paraqitjes dhe largimit nga puna.
⦁	Në mungesë të kartave elektronike, me ardhjen e tij/saj në shkollë mësues-i/ja firmos praninë e tij/saj në dokumentin që sekretaria vendos në sallën e mësuesve të shkollës.
⦁	Orari i paraqitjes së mësues-it/es në shkollë është në orën 07:45. Mësuesi largohet nga shkolla në orën 13:45, përjashtim bëjnë rastet kur parashikohen ndryshime me urdhër të Ministrit për raste të jashtëzakonshme.
⦁	Mësuesit duhet të jenë në gatishmëri për çdo ndryshim të mundshëm të orarit ditor sipas rasteve të frekuentimit të mësuesve dhe nevojave të shkollës.
⦁	Mësuesit dhe të gjithë punonjësit e tjerë të shkollës, mund të paraqiten me vonesë ose të largohet nga puna vetëm me lejen e drejtorit ose të personit të ngarkuar prej tij, në rastet kur drejtori nuk është në institucion.
⦁	Mësues-i/ja njofton drejtorin e institucionit të paktën një ditë para kur do të mungojë ose në mëngjes deri në orën 7.30, për t’u marrë masat përkatëse për ndryshimin e orarit mësimor.
⦁	Mësues-i/ja zbaton dhe respekton orarin e hyrjes në kohën e duhur në mësim.
⦁	 Zilja që lajmëron fillimin e orës së mësimit duhet ta gjejë mësues-in/en përpara klasës ku ka mësim.
⦁	 Për katin e tretë dhe të katërt regjistrat ndërrohen në sallën e mësuesve të katit të katërt.
⦁	Mësuesit kur nuk kanë mësim duhet që të qëndrojnë në mjediset e shkollës.
⦁	Mësuesit i ndalohet që të kryejë aktivitete që nuk lidhen me veprimtarinë e institucionit në orarin e punës.
⦁	Orari i pushimit është 20 minuta. Në kohën e  pushimit të madh mësuesit qëndrojnë pranë klasës kujdesari.
⦁	Ndryshime të orarit ose pushimit mund të kryhen vetëm me përjashtim të rastit kur parashikohen aktivitete në nivel shkolle për të cilat është marrë paraprakisht miratimi nga eprori i ZVA dhe rastet kur ka ndryshime ose rekomandime me urdhër Ministri.
⦁	Mësues-i/ja duhet të respektojë me korrektësi “Kodin e etikës dhe sjelljes”. Mësuesi gjatë veprimtarisë së tij është i detyruar të zbatojë standardet dhe kërkesat etike në nivelin e përcaktuar në kodin e etikës si dhe në Urdhërin nr. 31 datë 28.01.2020.
⦁	Mësues-i/ja nuk duhet të krijojë stres dhe të ushtrojë presion psikologjik ndaj nxënësve në orën e mësimit.
⦁	Mësues-i/ja duhet të shmangë konfliktet për vlerësimin e nxënësve, sidomos për vlerësimin me gojë.
⦁	Nota në të tri llojet e vlerësimeve (vlerësim i vazhduar, vlerësim me test, vlerësim portofoli) duhet të jetë e argumentuar qartë, bazuar në kritere vlerësimi dhe në përputhje me rezultatet e të nxënit në programin lëndor përkatës.
⦁	Mësues-i/ja kujdeset të ruajë parimet etike brenda orës së mësimit si dhe në mjediset e institucionit, ai/ajo nuk duhet për asnjë arsye të fyejë dhe të tregojë mungesë respekti ndaj nxënësve.
⦁	Mësues-i/ja nuk duhet për asnjë arsye ta nxjerrë nxënësin nga klasa gjatë orës së mësimit. Nëse ka probleme në komunikimin me nxënës të veçantë, pas mësimit komunikon me mësuesin kujdestar ose me anëtarë të drejtorisë së shkollës.
⦁	Mësues-i/ja paraqitet në shkollë me veshje dinjitoze, sipas  përcaktimeve në urdhërin Nr.31, datë 28.01.2020 dhe kodit të etikës.
⦁	Në ambjentet e shkollës është e domosdoshme të përdorë uniformën e mësuesit gjatë gjithë procesit mësimor (përparëse e bardhë).
⦁	Për mësuesit e edukimit fizik veshja gjatë orarit të mësimit do të jetë uniforma sportive.
⦁	Mësues-i/ja duhet të zbatojë rregullat e disiplinës dhe të vetëkontrollit, si dhe të mbajë përgjegjësi për veprimet e tij/saj.
⦁	Në rast përdorimi të celularit nga mësuesi të merren masa të përshkallëzuara .
⦁	Në rast të ardhjes me vonesë nga mësuesi dhe nëse e ka të përsëritur më shumë se tre herë këtë fenomen të merren masa të përshkallëzuara.
⦁	 Në rast shkelje të etikës dhe komunikimit nga ana e mësuesit ndsj drejtuesit dhe anasjelltas,të merren masa të përshkallëzuara.
⦁	 Mënyra e komunikimit me eproret, kolegët, nxënësit, prindërit dhe bashkëpunëtorët në mjediset e shkollës duhet të jetë brenda normave etike të sjelljes dhe komunikimit qytetar.
⦁	 Mësues-i/ja nuk duhet për asnjë lloj arsye të krijojë konflikt dhe dhunë verbale, fizike apo psikologjike në ambientet e shkollës.
⦁	 Mësues-it/eve i ndalohet rreptësisht përdorimi i duhanit dhe pijeve alkoolike në orarin e punës.
⦁	 Mësues-it/es nuk i lejohet të përdorë telefonin celular gjatë procesit mësimor, në zbatim të urdhërit të MASR Nr.493 datë 30.07.2018, “Për mospërdorimin e telefonit celular gjatë procesit mësimor në shkolla”.
⦁	 Në raste të komunikimit me prindër apo nevoja emergjente  të shkollës dhe familjare, telefoni do të përdoret nga mësuesit vetëm në mjedise të caktuara si zyra: drejtori, nëndrejtori, sekretari, sallën e mësuesve dhe jo në klasa, korridore apo oborrin e shkollës. 
⦁	 Mësues-i/ja e ka rreptësisht të ndaluar nxjerrjen e një informacioni konfidencial të institucionit, nëse nuk është i/e autorizuar ose nuk ka leje për ta kryer këtë, çështje që lidhen me veprimtarinë e tij/saj si mësues-e, merret paraprakisht leje, përjashtim bën këtu marrëdhënia me prindërit, sipas së cilës mësues-i/ja informon prindërit për ecurinë e fëmijës së tij/saj dhe çështje që lidhen me edukimin cilësor të fëmijës.
⦁	 Mësues-i/ja kryen detyrën e tij/saj në përputhje me legjislacionin në fuqi, kupton dhe zbaton me përgjegjësi çdo akt ligjor që lidhet me ushtrimin e profesionit si mësues.
⦁	 Zbaton detyrën bazuar në standardet e mësuesit, aktet dhe nënaktet ligjore në fuqi.
⦁	 Bashkëpunon me prindërit dhe drejtorinë e shkollës për ecurinë e procesit mësimor – edukativ.
⦁	 Ndjek dhe zbaton me prioritet kalendarin e aktiviteteve gjithëvjetore artistike, mjedisore, letrare, historike duke identifikuar, përfshirë, motivuar nxënësit.
⦁	  Detyra kryesore e mësues-it/es është qartësimi i programit mësimor edukativ me nxënësit.
⦁	Mësues-i/ja duhet të jetë i kujdesshëm në vlerësimin sistematik të nxënësit, në raportin e vlerësimit verbal dhe me shkrim, duke pasur parasysh se synimi kryesor i vlerësimit është të nxënit dhe përparimi i nxënësit.
⦁	Mësues-i/ja nuk duhet të shënojë asnjë vlerësim në regjistër elektronik (SMIP) apo në evidencën e tij personale të vlerësimit, pa ia bërë të ditur dhe argumentuar më parë atë nxënësit.
⦁	Mësues-i/ja duhet t’i korrigjojë punët me shkrim të nxënësit brenda 7 ditëve nga momenti i realizimit dhe t’i pasqyrojë në evidencë dhe regjistër.
⦁	Mësues-i/ja duhet t’i dorëzojë punët me shkrim si dhe relacionin përkatës në arshivën e shkollës (në nëndrejtori), pasi  ka vënë në dijeni nxënësit për vlerësimin e tyre.
⦁	Mësues-i/ja mban të dhëna gjatë gjithë vitit shkollor për vlerësimin e nxënësit. Vlerësimi i vazhduar, testet/detyrat përmbledhëse ruhen në shkollë dhe janë objekt i monitorimit në çdo periudhë të vitit shkollor (neni 20 i Urdhërit Nr.31, datë 28.01.2020) si dhe bazuar në Udhёzimin Nr.3754/2 prot.,  Nr.17, datё 5.7.2022, pёr `vlerёsimin e nxёnёsve nё sistemin arsimor pararauniversistar;
⦁	 Mësues-i/ja është i detyruar të plotësojë me korrektësi dokumentacionin kryesor (SMIP, ditari, evidencat) të vlerësimit të nxënësve. 
⦁	 Mësues-i/ja raporton sipas kërkesave të drejtorisë apo institucionit epror rreth PME.
⦁	 Mësues-i/ja duhet të dorëzojë planin lëndor vjetor dhe të periudhës së parë, pesë ditë përpara fillimit të vitit të ri shkollor.
⦁	 Mësues-i/ja harton rregullisht planin (ditarin) e çdo ore mësimi, sipas rubrikave në përputhje me udhëzuesit kurrikularë.
⦁	 Mësues-i/ja në bashkëpunim me shërbimin psiko-social të shkollës harton plane pune dhe plane përmirësimi për nxënës me vështirës në të nxënë, arritje të ulëta akademike, të kthyer nga emigracioni si dhe për nxënësit me aftësi ndryshe dhe bën vlerësimin bazuar në rezultatet e të nxënit të përcaktuara në këto plane pune.
⦁	 Statistikat e detyrueshme për t’u paraqitur në drejtorinë e shkollës të plotësohen qartë, pastër dhe pa gabime, brenda afateve të caktuara.
⦁	 Mësues-i/ja duhet të pasqyrojë mungesat e nxënësve në SMIP në fillim të orës së mësimit.
⦁	 Dorëzon në sekretari një javë përpara testet e periudhës për t´u fotokopjuar.
⦁	 Mësues-i/ja mban dhe përditëson portofolin e tij profesional, sipas nenit 63 të Urdhërit Nr.31 datë 28.01.2020.
⦁	 Në orën e mësimit mësues-i/ja ndjek zbatimin e rregullores së shkollës nga nxënësit.
⦁	 Në kërkesën për të pasur një klasë të pastër, pa letra dhe mbeturina.
⦁	 Raporton largimet pa leje të nxënësve nga ora e tij tek mësuesi  kujdestar.
⦁	 Raporton te mësuesi kujdestar për nxënësit që janë pa bazë materiale dhe pa uniformë shkollore.
⦁	 Nuk lejon përdorimin e celularit në orën e mësimit për asnjë arsye. Në rast të konstatimit zbaton rregulloren për nxënësin dhe dorëzon celularin në drejtorinë e shkollës.
⦁	 Raporton tek mësuesi kujdestar, prindi e më pas në komisionin e etikës, raste të sjelljes së pahijshme dhe probleme të edukatës qytetare të nxënësit, brenda dhe jashtë orës së mësimit.
⦁	 Mësuesi nuk i jep leje nxënësit për të dalë nga ora e mësimit për asnjë arsye, pa aprovimin e prindit, mësuesit kujdestar dhe pa dijeninë e njërit prej anëtarëve të drejtorisë.

     
RREGULLORE E DISIPLINËS PËR VEPRIMTARINË E MËSUESIT TË SHËRBIMIT DITOR
në zbatim të Urdhërit Nr.31 datë 28.01.2020, udhëzimeve të MAS dhe rregullores së brendshme të shkollës
 Mesuesi Dezhurn detyrat 

⦁	Mësuesit dezhurn paraqiten në shkollë në orën 7:30 dhe largohen pas mbarimit të plotë të procesit mësimor në orën 13:50, në kushte të zakonshme mësimore, në kushte të jashtëzakonshme sipas udhëzimeve të MAS do të kryhet me orar të zgjatur ose të reduktuar.
⦁	Mësuesit dezhurn sipas kateve tërheqin fletoren per mungesat ditore në sekretarinë e shkollës dhe ua dorëzojnë mësueseve nga vendi i caktuar posaçërisht për shpërndarjen e tyre.
⦁	Mësuesit dezhurn janë të pranishëm në korridorin e katit përkatës gjatë çdo pushimi 5-minutësh dhe gjatë pushimit të gjatë. Në çdo moment nxënësit duhet të mbikëqyren nga mësuesit dezhurn.
⦁	Mësuesit dezhurn kujdesen që çdo mësues të ketë paraqitjen ne orar për orën e mësimit.
⦁	Mësuesit dezhurn kujdesen për të shoqëruar në oborr nxënësit e klasave që kanë pushim pasi ka rënë zilja për fillimin e orës së mësimit.
⦁	Për asnjë arsye nxënësit nuk duhet të lëvizin në korridore për të dalë jashtë ose në oborr gjatë kohës së pushimit 5 minutësh.
⦁	Mësuesit dezhurn kujdesen për të dhënë me korrektësi ndjekjen e lajmërimeve të bëra nga drejtoria.
⦁	Dorëzimi i dokumentacionit në sekretarinë e shkollës në fund të procesit mësimor është detyrim i mësuesve dezhurn. Për asnjë arsye ata nuk mund të largohet nga shkolla pa dorëzuar të gjithë dokumentacionin dhe procesverbalin ditor në sekretarinë e shkollës.
⦁	Mësuesit dezhurn nuk duhet të bëjnë ndryshime në grafikun e dezhurnit të shkollës pa lejen e drejtorit të shkollës ose personit të ngarkuar prej tij.
⦁	Mësuesit dezhurni kujdesen për delegimin tek mësuesit të çdo njoftimi zyrtar, si dhe për menaxhimin e dorëzimit të informacionit në kohë nga çdo mësues në drejtorinë  e shkollës.
⦁	.
⦁	Mësues-i/ja dezhurn kujdesen për marrjen dhe raportimin e mungesave në kohë në mëngjes dhe në orën e 4-t.
⦁	Në rastet e ndryshimit të orarit të veprimeve ditore ose mungesave të mësuesve dhe zënëvdësimeve në orar mësuesit dezhurn kujdesen për ndjekjen e orarit dhe grafikut të zëvëndësimeve ditore.
⦁	Mësuesit e dezhurnit ditor mbajnë përgjegjësi për orarin e fillimit dhe përfundimit të procesit mësimor, menaxhojnë zilen.
⦁	Mësuesit dezhurn raportojnë në fund të javës për ecurinë e PME, problematika, vështirësi dhe risi të ndrodhura gjatë dezhurnit të tyre.


VEPRIMTARINË E MËSUESIT KUJDESTAR
në zbatim të Urdhërit Nr. 31 datë 28.01.2020,
udhëzimeve të MAS dhe rregullores së brendshme të shkollës

⦁	Mësuesi kujdestar informohet çdo ditë mbi frekuentimin e nxënësve, mbi problemet e tyre dhe me çdo shqetësim tjetër të nxënësve.
⦁	Mësuesi kujdestar duhet të zhvillojë me përgjegjësi dy orët javore të kujdestarisë që përfshijnë veprimtari me klasën dhe plotësim dokumentacioni.
⦁	Mësuesi kujdestar dorëzon planin vjetor të punës edukative, pas konsultimit dhe në bashkëpunim me këshillin e prindërve të klasës. Ky plan hartohet sipas një formati të caktuar, bazuar në njohjen e përbërjes së klasës, gjendjes sociale, botës shpirtërore të nxënësve, në veçanti të personalitetit, prirjet, aftësitë, interesat e tyre.
⦁	Mësuesi kujdestar duhet të zhvillojë me përgjegjësi dhe me korrektësi takimet me prindër, dhe të mbajë kontakte të vazhdueshme për të gjitha problematikat e hasura me nxënësit.
⦁	Mësuesi kujdestar duhet të bashkëpunojë në mënyrë të vazhdueshme me këshillin e prindërve të klasës.
⦁	Mësuesi kujdestar duhet të nxisë debatin e lirë në klasë, të diskutojë për shumë probleme me nxënësit, të respektojë statusin e tyre, të komunikojë nëpërmjet diversitetit të mendimeve, me transparencë dhe me tolerancë.
⦁	Për zbatimin e urdhrit të ministrit për mospërdorimin e celularëve në procesin mësimor, mësuesi kujdestar duhet të ngrejë një grup pune në klasë për ndjekjen e zbatimit të përditshëm të këtij urdhri.
⦁	Mësuesi kujdestar duhet të pasqyrojë çdo javë mungesat e nxënësve në regjistër.
⦁	Mësuesi kujdestar ka të drejtë të justifikojë deri në tri ditë të plota pika 2, neni 77, i Urdhërit Nr.31 datë 28.01.2020, (jo orë teke) mungesa në muaj për nxënës, kur justifikimi kërkohet nga prindi, duke vënë në dijeni nëndrejtorin/drejtorin që mbulon klasën përkatëse. Mungesat justifikohen nga mësuesi kujdestar deri në tre ditë dhe miratohen ose jo nga drejtoria kur këto janë më shumë se tre ditë. Justifikimi i mungesave kryhet vetëm në rastet kur prindi dokumenton me raport mjekësor të lëshuar nga mjek-u/ja e familjes. Prindi/kujdestari ligjor i fëmijës njofton në shkollë mësuesen kujdestare dhe pranohet justifikimi prindëror me shkrim vetëm për arësye të jashtëzakonshme (pa raport mjekësor), në të cilën kërkon leje paraprakisht me një shënim sqarues dhe pasi i është miratuar kërkesa nga mësues-i/ja kujdesatar/e dhe drejtoria e shkollës kur mungon më shumë se tri ditë, (prindi lajmëron paraprakisht, jo ditën që mungon nxënës-i/ja). Raporti sillet me foto ose online tek mësues-i/ja kujdestare foto ditën që merret e më pas sillet në shkollë kur gjendja shëndetësore e fëmijës është e përmirësuar.
⦁	Nëse nxënës-i/ja mungon më shumë se tri ditë, mungesat justifikohen vetëm nga drejtoria e shkollës, referuar raportit të lëshuar nga mjek-u/ja e familjes. Për rastet që parashikohet për arësye të jashtëzakonshme që nxënësi të mungojë më shumë se tri ditë prindi kërkon leje me shkrim në drejtorinë e shkollës dhe merr miratimin ose jo bazuar në arsyen e kërkesës.
⦁	Mësues-i/ja kujdestar/e dorëzon brenda javës së parë të çdo muaji drejtorit të IA-së tabelën e mungesave përmbledhëse mujore të klasës, të ndara në gjithsej, me arsye, pa arsye dhe mungesa 1-3 orëshe.
⦁	Mësuesi kujdestar duhet të komunikojë menjëherë brenda ditës me prindërit e nxënësve që largohen nga orët e mësimit.
⦁	Mësuesi kujdestar duhet të plotësojë masat disiplinore të nxënësve (që janë në kompetencën e tij) nga “Qortimi” deri tek “Paralajmërimi për përjashtim nga shkolla”. Për masat e dhëna, duhet të njoftojë drejtorinë e shkollës dhe prindin e nxënësit.
⦁	Mësuesi kujdestar plotëson me përgjegjësi regjistrin elektronik të klasës kujdestare dhe të gjitha statistikat mujore e vjetore  të klasës duke respektuar afatin kohor.
⦁	Mësuesi kujdestar kujdeset për ruajtjen e higjienës dhe bazës materiale të klasës, për krijimin e një ambienti që nxit një të mësuar aktiv dhe produktiv.
⦁	Mësuesi kujdestar plotëson me përgjegjësi dëftesat e nxënësve të klasës në sistem  dhe kujdeset nëse i ka vajtur prindit në fund të vitit shkollor.
⦁	Mësuesi kujdestar merr pjesë dhe shoqëron nxënësit e klasës në aktivitete brenda e jashtë shkollës, sipas një plani të miratuar nga drejtoria e shkollës.
⦁	Mësuesi kujdestar bashkërendon punën me psikologen e shkollës për evidentimin dhe ecurinë e nxënësve që paraqesin probleme dhe shqetësime, duke patur një bashkëpunim të ngushtë me prindërit e tyre.
⦁	Mësuesi kujdestar krijon dosjen e klasës në të cilën përfshihen: 
a. Lista emërore e klasës;
b. Plani edukativ;
c. Plani i veprimtarive mujore;
 Kjo dosje plotësohet gjatë gjithë vitit shkollor dhe është objekt kontrolli i drejtorisë së shkollës.





"""

def merr_pergjigje(pyetja):
    if "chat_history" not in session:
        session["chat_history"] = []

    chat_history = session["chat_history"]

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "system", "content": konteksti},
            *chat_history,
            {"role": "user", "content": pyetja}
        ]
    }

    res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    if res.status_code == 200:
        answer = res.json()["choices"][0]["message"]["content"]
        chat_history.append({"role": "user", "content": pyetja})
        chat_history.append({"role": "assistant", "content": answer})
        session["chat_history"] = chat_history
        return answer
    return f"GABIM: {res.status_code} - {res.text}"

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        kodi = request.form.get("kodi", "").strip()
        roli = request.form.get("roli")

        if kodi == "Klasa105" and roli in ["student", "teacher", "parent"]:
            session["logged_in"] = True
            session["roli"] = roli
            session.pop("chat_history", None)
            return redirect(url_for("chat"))
        else:
            error = "Kodi i hyrjes është i pasaktë ose nuk ke zgjedhur rolin."

    return render_template("login.html", error=error)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if "chat_history" not in session:
        session["chat_history"] = []

    pergjigje = None
    if request.method == "POST":
        pyetja = request.form.get("pyetja")
        if pyetja:
            pergjigje = merr_pergjigje(pyetja)

    return render_template("index.html", chat_history=session["chat_history"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
