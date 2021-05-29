from crypto import encrypt, decrypt
import sys

# for lists
pk1 = 19540560569202587528885818607946719567533686490219720937100551728859893697779370551998931877312345843544224620427771659480920345623899842212458273970857680966361784198158578388701277770399334763814182715893563415016392423667795231492963695511385390711672057691954677589539851987840135861169478590956806230773178907509276568375514047711691587726977535566376972408118974449940441954233680902747048905270523196120068255404322286430237915665015540570631835141496109624098071974449011858147126769178932652985707386674814691726363085179262813926579729508975195343002685751365028949953615532445763008970620439044263028642539, 53268083464928996237499501514930696091481882304426958063368158069708279942791651115909601882400326960728371852158399053680726827569955751930056461064439127672422448343714860557855405598421024776197228696905253350836445395735937391590166013441899353373708858644322149771515424650869101948910110341551788219937781392830385987124262981244948804038192026238679235883973560217026331958960232084061907191785411206392350348866732759730712930496329430747961333910666283089829188627535206292062248847927215231429503447979834393036409896936663212722393797937523655842495272486182217672712542371572046944319600696324504109425423275486309189864479355780847087846220081049718490949144896200499064493278759613369394835669904584780720476502289048023907606100680262714819836728287835789667349517351686876327913250671710498699561360186598238044962836776070070298048757268079642804283003402607389396839840244002860530308328949598618257600348148379929475990159062505771247512354044568625125618386979755865808510930871399708470139001295541221292471287309845694844539168647347515843694213165708545086661458555691985009142618913267512801545297428449292829028835612932624517379263444068015773283583013002782055708393709671554270795183951181710433020190202
sk1= (9770280284601293764442909303973359783766843245109860468550275864429946848889685275999465938656172921772112310213885829740460172811949921106229136985428840483180892099079289194350638885199667381907091357946781707508196211833897615746481847755692695355836028845977338794769925993920067930584739295478403115386449152391800815392345709072312950499156697543797687815278851634604475960489537784222667679500600566514599577213341872681400078712415868879973486767236679336893721022172777734347919105684517095104242796986477895884580062986851224943766737826292784398624604206599296557544786647550988001832256247276772577286020, 12330901809993023424346069305890755745236189094537990406999794662920874037939492258639046628993295757204762644144352089491191247964714092467835928706620235561316670562707877509293361675829425740057986426614169414759287830665240519216857121565345626196137492510044005082563256150657351893454919945608377188908006418088220153866230885480174795524406679275433499570942787996661403600932105422218913772622415859187975958975004476774046168939648117276937319003050201220619159707665038597018053700104952213705517323487195149522692032554347198728441291558554930142975201826571261137737184633629761825885277469087456210075414)

# for candidates
pk2 = 24991282198634143292856967222353153632016778548891469848591344947889915953262467018783700635168949255976600810924461472583196516037680514437042951775363922460669337706904960941917874545376160803417839167362877623340565129682563254745234305490197495357381643396931058560632326393600874296138704573551657349131716925332918157886299681219654134347305177793350103442009551777144668188293837914694719174003618090441579446935952471530465906379870734123178829897042635504548482653515968620211599925254576099853092865216613291128970363998805331234981326494259179476285547631745493955825696013562699276369779561710288668129383
sk2= (12495641099317071646428483611176576816008389274445734924295672473944957976631233509391850317584474627988300405462230736291598258018840257218521475887681961230334668853452480470958937272688080401708919583681438811670282564841281627372617152745098747678690821698465529280316163196800437148069352286775828674565699115445194275318288584744025510467716360663556488757599099056450962957143923993987595631165545645733872782681407362194524453666404871127099228018116446175595612878458408030671990280948137754795337389437389882602756519313296795573431880203336212432522604819388480871216817043653785060611362562581235766249900, 12493059452547732954379786876933508060841966333279634822462767409479528956824066779734502639697198022925902784626823360527300151779132035159846254623219721253520239810573692891878222269542647850736118679949227126976341482004846559723889598690864031100191397603942745603449013886797428417357393719385576071115870660159843999765181274670043996047070311273375643434068719361719920732391560001366227289306568691566426517910427116007910532642781159615937445966209253284083911370204481334403394414687197585629869123944990002420389245775229664939254671016855139203656406528667060454925302996304994099469582491210225840847708)

del sys.argv[0]

encrypted_lists = sys.argv[0]
encrypted_candidates = sys.argv[1]

decrypted_values = {}

for index, list in enumerate(encrypted_lists):
    voter_index = "voter" + index + 1
    decrypted_values[voter_index]["list"] = index

for index, list in enumerate(encrypted_candidates):
    voter_index = "voter" + index + 1
    decrypted_values[voter_index]["candidate"] = index
    
print(decrypted_values)