import requests
import json
from onem2m import *
from datetime import datetime
from datetime import timedelta
from basics import db,data
# from_zone = tz.gettz('UTC')
# to_zone = tz.gettz('America/New_York')

final_reading = []
oe_temp = []
time = []
def get_data_grp(group_name):
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
    }

    group_uri = group_name
    print(group_uri)
    response = requests.get(group_uri, headers=headers)
    # print('Return code : {}'.format(response.status-code))
    #print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    print("Get " + group_name)
    oe_temp.append([_resp['m2m:cin']['ct'], _resp['m2m:cin']['con']])
    # spliced-string = output-string.split()
    # for con in spliced-string:
        # if spliced-string.index(con) == 2:
            # data.append(con)
        # if spliced-string.index(con) == 7:
            # meow.append(con)

    # data.append(loli)
    # print(oe_temp)
    # print("==========================")
    return response.status_code, _resp

def convert_to_time(ctime):
	date = ctime[0:8]
	time = ctime[9:15]
	datetime_object = datetime.strptime(ctime, '%Y%m%dT%H%M%S')
	return datetime_object + timedelta(hours=5,minutes=30)
	# print(datetime_object)
	# return datetime_object

def lolzzmax():
    # server = "http://onem2m.iiit.ac.in/~/in-cse/in-name/Team22-Water-Level-Monitoring-in-Overhead-Tanks/node-1/"
    # lolmax = ["cin-163911679","cin-197346638","cin-987210096","cin-291250657","cin-748523646","cin-625205997","cin-516244186","cin-531719764","cin-134070750","cin-825901307","cin-960594054","cin-128714720","cin-481087682","cin-765029315","cin-688584719","cin-979314682","cin-799679709","cin-371935880","cin-970322429","cin-942204590","cin-760193537","cin-591504543","cin-282680047","cin-715253669","cin-584736631","cin-357765366","cin-302806456","cin-214535893","cin-328126435","cin-719444815","cin-225181935","cin-743724136","cin-147662591","cin-271083887","cin-184955853","cin-114790997","cin-553697373","cin-112211627","cin-357445205","cin-944999561","cin-642945514","cin-246003016","cin-94887859","cin-25588155","cin-887429428","cin-563196453","cin-511906753"]
    # lolmax = ["cin-880500811","cin-559332468","cin-451625473","cin-924096586","cin-419182737","cin-976264976","cin-701505002","cin-950958302","cin-785982523","cin-712282471","cin-576987439","cin-99663505","cin-231573221","cin-139472512","cin-226824741","cin-2202235","cin-235004777","cin-27278935","cin-378338633","cin-948773834","cin-707992410","cin-832666415","cin-991440174","cin-960411457","cin-213678277","cin-21025465","cin-51525791","cin-584569768","cin-155638142","cin-204204015","cin-74448822","cin-328903900","cin-274490665","cin-597965266","cin-533066112","cin-938246272","cin-780574015","cin-852491422","cin-653373576","cin-469601388","cin-575531233","cin-972001868","cin-856071318","cin-263300926","cin-311169209","cin-58519092","cin-98923012","cin-756096018","cin-921980810","cin-3059079","cin-848382239","cin-488170862","cin-398353475","cin-757990562","cin-620281799","cin-648021480","cin-739388528","cin-19309734","cin-633415267","cin-761736979","cin-151487245","cin-474602985","cin-19135785","cin-874017155","cin-55473917","cin-511294825","cin-262145679","cin-185298152","cin-3914852","cin-195480793","cin-182119203","cin-787531143","cin-137820480","cin-869143900","cin-673282482","cin-451843957","cin-748188389","cin-968044802","cin-680292158","cin-166873433","cin-260481836","cin-599604664","cin-524152584","cin-400468493","cin-308365841","cin-624017342","cin-6370674","cin-803693093","cin-672831683","cin-875097695","cin-607669203","cin-104077975","cin-691437861","cin-573848587","cin-819163145","cin-197826104","cin-781786223","cin-544048589","cin-661610623","cin-251236410","cin-259443584","cin-106804116","cin-952148454","cin-613466608","cin-756873367","cin-946241913","cin-819121785","cin-846799933","cin-116797003","cin-742756808","cin-761438758","cin-731658303","cin-504187390","cin-344664197","cin-79286266","cin-402049434","cin-687231459","cin-899751189","cin-656499089","cin-951059216","cin-778355233","cin-482674008","cin-261565714","cin-721046359","cin-369414899","cin-366267278","cin-467030120","cin-570513780","cin-755026897","cin-328055916","cin-61556456","cin-301462849","cin-771778118","cin-953175604","cin-197076724","cin-63381225","cin-554494382","cin-460956724","cin-458877414","cin-702010219","cin-748502676","cin-977670735","cin-743971849","cin-941415425","cin-320428255","cin-790582705","cin-556931210","cin-397203097","cin-899971219","cin-704322859","cin-261486592","cin-424631532","cin-576203003","cin-930443042","cin-372486178","cin-178846611","cin-688812849","cin-596311543","cin-291667587","cin-38423893","cin-248935342","cin-985580242","cin-488625360","cin-478122844","cin-169681521","cin-647388950","cin-394916758","cin-507332577","cin-106960824","cin-899629715","cin-835816046","cin-356075872","cin-702496403","cin-688620110","cin-974785297","cin-81268866","cin-635693907","cin-565378362","cin-916110804","cin-532398353","cin-446380345","cin-38737865","cin-858234081","cin-190210362","cin-441931510","cin-957530055","cin-406369398","cin-790717962","cin-66997429","cin-435954531","cin-869517","cin-395574551","cin-610845572","cin-279021899","cin-50689429","cin-94233536","cin-440713186","cin-52151685","cin-100327074","cin-448289778","cin-874177993","cin-273182267","cin-936154554","cin-183760392","cin-379012264","cin-455504234","cin-512552844","cin-188459791","cin-369305606","cin-919857254","cin-87670525","cin-389069097","cin-562378256","cin-209768104","cin-392189107","cin-953030633","cin-614346057","cin-285274787","cin-408868559","cin-960047694","cin-308237409","cin-923971724","cin-551632498","cin-452531583","cin-752470486","cin-750070638","cin-73286010","cin-188955320","cin-919306055","cin-129087458","cin-107001313","cin-553530259","cin-87449892","cin-882418732","cin-398866763","cin-129006564","cin-327351194","cin-711288185","cin-224830177","cin-824974730","cin-724938593","cin-886075036","cin-957024002","cin-862117851","cin-983623801","cin-933329622","cin-730480117","cin-132440085","cin-328700785","cin-966415892","cin-253289249","cin-376128322","cin-536125716","cin-696650884","cin-831620197","cin-494575144","cin-535084698","cin-118586915","cin-234087084","cin-573995359","cin-748553825","cin-461255722","cin-342239742","cin-156161115","cin-343343738","cin-652003032","cin-830004822","cin-766331312","cin-485769183","cin-749438277","cin-15057310","cin-896456774","cin-838603219","cin-359578455","cin-281771922","cin-349475736","cin-85708374","cin-529543078","cin-570461864","cin-969621571","cin-970381411","cin-677272092","cin-610751682","cin-305177328","cin-382047665","cin-120072185","cin-260101799","cin-377335020","cin-45370497","cin-945878740","cin-415171773","cin-675638220","cin-530614133","cin-873872209","cin-491800206","cin-628906866","cin-537768191","cin-97752753","cin-209020177","cin-848843149","cin-637735265","cin-57820201","cin-155711480","cin-914482552","cin-220053513","cin-220849293","cin-66741188","cin-159300747","cin-554892928","cin-503075384","cin-940746872","cin-579961426","cin-575303704","cin-83584209","cin-589892269","cin-576655159","cin-803143662","cin-687484443","cin-800452552","cin-685171783"]
    # lolmax = ["cin-229194911","cin-579827981","cin-673596909","cin-908656360","cin-135702940","cin-194036731","cin-224337796","cin-663036154","cin-607168659","cin-300626290","cin-437808807","cin-206555887","cin-694033785","cin-929807794","cin-523436562","cin-326722888","cin-926523147","cin-893147305","cin-743052870","cin-619630128","cin-845549682","cin-352092827","cin-573000","cin-760647355","cin-496254588","cin-985865973","cin-596239741","cin-387678041","cin-966246806","cin-68365922","cin-139873022","cin-58893555","cin-82604358","cin-890319430","cin-663204530","cin-308935905","cin-52948287","cin-621225097","cin-36919482","cin-652596662","cin-702325456","cin-526532606","cin-533182969","cin-836927878","cin-468499223","cin-713411091","cin-296203462","cin-116994105","cin-376560133","cin-424255739","cin-369943044","cin-872613922","cin-532464376","cin-442864255","cin-298542321","cin-168510522","cin-987148555","cin-578906895","cin-567258119","cin-658633709","cin-262093831","cin-419570667","cin-49467491","cin-894716859","cin-975363990"]
    # lolmax = ["cin-7846594","cin-129428309","cin-425308612","cin-681769326","cin-180660987","cin-615797706","cin-711011732","cin-646448748","cin-446046008","cin-489916439","cin-662253036","cin-356438620","cin-873801687","cin-350570148","cin-753283241","cin-943057276","cin-149311142","cin-682385221","cin-874355247","cin-122089710","cin-404395344","cin-458940845","cin-499597201","cin-821282516","cin-891362873","cin-783263396","cin-370064075","cin-664600770","cin-403818736","cin-120098323","cin-172371465","cin-242244400","cin-777043774","cin-907862434","cin-125062589","cin-753121620","cin-651243518","cin-782216644","cin-672998652","cin-544628971","cin-912457708","cin-471067406","cin-708312563","cin-268132789","cin-210285581","cin-848628726","cin-100228340","cin-393098626","cin-501916894","cin-6812277","cin-109677905","cin-376582043","cin-339498506","cin-973825337","cin-162685921","cin-556008366","cin-216795330","cin-392115296","cin-278665838","cin-533526866","cin-693916787","cin-216349643","cin-362985247","cin-852528017","cin-411531797","cin-789158054","cin-724781856","cin-678800763","cin-570048874","cin-807290482","cin-833636051","cin-341975138","cin-594302398","cin-301252346","cin-905489472","cin-740408027","cin-329085972","cin-676729801","cin-270336081","cin-580827857","cin-536470090","cin-339782867","cin-541116498","cin-960955003","cin-835317130","cin-157220454","cin-643591395","cin-847277511","cin-810198326","cin-8716144","cin-828833460","cin-386594874","cin-636888493","cin-542120208","cin-274252450","cin-706406075","cin-892787621","cin-327979604","cin-961004342","cin-937522115","cin-950698852","cin-673528713","cin-93339823","cin-756251912","cin-753846001","cin-778080234","cin-764687624","cin-981455337","cin-193675857","cin-461176171","cin-815482094","cin-894731128","cin-842921332","cin-286676178","cin-550670942","cin-786604726","cin-693213549","cin-671788416","cin-378647313","cin-101932338","cin-160241095","cin-912426100","cin-3130823","cin-677866876","cin-419978766","cin-320449493","cin-759178445","cin-992638337","cin-362827981","cin-531315598","cin-503231473","cin-222144426","cin-939216524","cin-500387365","cin-709558002","cin-148511070","cin-334114225","cin-557599737","cin-402731526","cin-322532190","cin-186488967","cin-495413370","cin-659144118","cin-423069182","cin-515474368","cin-802840475","cin-284983724","cin-735346993","cin-244069092","cin-227605452","cin-832083756","cin-780819235","cin-793459664","cin-224203376","cin-980378523","cin-31597220","cin-18623306","cin-967271447","cin-524273991","cin-560960694","cin-366619623","cin-675142309","cin-192533461","cin-68749410","cin-773266655","cin-582333064","cin-885998238","cin-896397976","cin-849429575","cin-225189643","cin-555972400","cin-553084390","cin-238427402","cin-740364486","cin-574025349","cin-472425225","cin-228518176","cin-621018206","cin-297150207","cin-616577770","cin-687997570","cin-208182441","cin-280718578","cin-560482817","cin-365396872","cin-682314099","cin-851970256","cin-147423642","cin-216396384","cin-698001593","cin-654913552","cin-893485681","cin-31319317","cin-377182187","cin-38601012","cin-997670546","cin-556685297","cin-359854133","cin-606592439","cin-850029068","cin-455393036","cin-772174183","cin-115981435","cin-952224939","cin-474631836","cin-45771226","cin-243202128","cin-294595522","cin-106980226","cin-765154199","cin-988123221","cin-365270953","cin-109774151","cin-940288691","cin-178057492","cin-244351785","cin-44481287","cin-127162385","cin-185239155","cin-852479870","cin-724079613","cin-733389947","cin-864439956","cin-790743356","cin-269501231","cin-906007833","cin-638096102","cin-621814833","cin-604781869","cin-390647148","cin-748771238","cin-721063273","cin-907851984","cin-831501139","cin-122200944","cin-115939922","cin-196004215","cin-461287690","cin-435999260","cin-768939520","cin-535166338","cin-184102624","cin-307986578","cin-839143760","cin-668777701","cin-162069367","cin-273306831","cin-215866201","cin-250267800","cin-978044356","cin-26737090","cin-162947604","cin-913233290","cin-780440585","cin-560714597","cin-173230197","cin-336237621","cin-588658898","cin-69013817","cin-928269366","cin-407516848","cin-122768831","cin-885159787","cin-671347804","cin-870116702","cin-404054567","cin-336138618","cin-995657692","cin-654063549","cin-914944395","cin-177662818","cin-265726649","cin-826601935","cin-555941948","cin-938289429","cin-188031081","cin-616429282","cin-512795237","cin-474890266"]
    # lolmax = ["cin-775866088","cin-813645806","cin-575428497","cin-719890287","cin-233643401","cin-181453534","cin-532599151","cin-698614347","cin-324710110","cin-536671261","cin-576974178","cin-81974221","cin-357661807","cin-43488307","cin-452428200","cin-538279862","cin-766448777","cin-125584409","cin-830134968","cin-548951553","cin-465630767","cin-21097377","cin-352674984","cin-181864393","cin-273086800","cin-298338695","cin-982547861","cin-612272763","cin-836728257","cin-271232259","cin-291190729","cin-645295783","cin-282950043","cin-350156771","cin-310864093","cin-469155480","cin-102695825","cin-405262614","cin-250364351","cin-484848336","cin-386443603","cin-862927234","cin-944138208","cin-502582245","cin-1116510","cin-69579727","cin-775229322","cin-731499018","cin-448174662","cin-657672226","cin-125301650","cin-934677843","cin-267685555","cin-209537677","cin-483127342","cin-195963938","cin-860602924","cin-52664787","cin-378122457","cin-511930532","cin-693552","cin-947746164","cin-15768630","cin-926146342","cin-417775217","cin-311638922","cin-427627501","cin-947429009","cin-306463493","cin-77528767","cin-33476018","cin-646273973","cin-344845106","cin-515413316","cin-735587647","cin-332088197","cin-209901157","cin-304376078","cin-165713827","cin-822110547","cin-580397266","cin-425876984","cin-426262204","cin-309803320","cin-358378326","cin-465691002","cin-480884221","cin-393886586","cin-983503602","cin-519708442","cin-857437283","cin-667191628","cin-844747233","cin-825030290","cin-850599472","cin-994518901","cin-36820721","cin-655133777","cin-942008807","cin-738388514","cin-324449345","cin-90428489","cin-229068674","cin-124099474","cin-587250735","cin-109151975","cin-298837682","cin-364152838","cin-766422689","cin-209299720","cin-221947657","cin-536563087","cin-722064681","cin-564059949","cin-180993672","cin-705769812","cin-604400045","cin-624062513","cin-663754228","cin-197861389","cin-629385182","cin-336296702","cin-955295676","cin-806339865","cin-501513679","cin-244588207","cin-368115882","cin-771098485","cin-276664658","cin-639453623","cin-48492299","cin-384214897"]
    lolmax = discovery("http://onem2m.iiit.ac.in:443/~/in-cse/cnt-902636175")[1];

    # get-data-group("cin-511906753")
    # get_data_group("http://onem2m.iiit.ac.in:443/~/in-cse/cin-775866088");
    for i in lolmax:
        print(i)
        if(i[8:11] == "cnt"):
            continue
        get_data_grp("http://onem2m.iiit.ac.in:443/~" + i)
    # for j in 
    comp = convert_to_time("20191106T000000")
    oe_temp.sort()
    oe_temp1 = []
    for j in oe_temp:
        if convert_to_time(j[0]) > comp:
            oe_temp1.append([convert_to_time(j[0]), j[1]])

    oe_temp.clear()
    lolmax = discovery("http://onem2m.iiit.ac.in:443/~/in-cse/cnt-256133761")[1];

    # get-data-group("cin-511906753")
    # get_data_group("http://onem2m.iiit.ac.in:443/~/in-cse/cin-775866088");
    for i in lolmax:
        print(i)
        if(i[8:11] == "cnt"):
            continue
        get_data_grp("http://onem2m.iiit.ac.in:443/~" + i)
    # for j in 
    comp = convert_to_time("20191106T000000")
    oe_temp.sort()
    oe_temp2 = []
    for j in oe_temp:
        if convert_to_time(j[0]) > comp:
            oe_temp2.append(j[1]) 
            

    oe_temp.clear()
    lolmax = discovery("http://onem2m.iiit.ac.in:443/~/in-cse/cnt-331059742")[1];

    # get-data-group("cin-511906753")
    # get_data_group("http://onem2m.iiit.ac.in:443/~/in-cse/cin-775866088");
    for i in lolmax:
        print(i)
        if(i[8:11] == "cnt"):
            continue
        get_data_grp("http://onem2m.iiit.ac.in:443/~" + i)
    # for j in 
    comp = convert_to_time("20191106T000000")
    oe_temp.sort()
    oe_temp3 = []
    for j in oe_temp:
        if convert_to_time(j[0]) > comp:
            oe_temp3.append(j[1])

    oe_temp.clear()
    lolmax = discovery("http://onem2m.iiit.ac.in:443/~/in-cse/cnt-244479154")[1];

    # get-data-group("cin-511906753")
    # get_data_group("http://onem2m.iiit.ac.in:443/~/in-cse/cin-775866088");
    for i in lolmax:
        print(i)
        if(i[8:11] == "cnt"):
            continue
        get_data_grp("http://onem2m.iiit.ac.in:443/~" + i)
    # for j in 
    comp = convert_to_time("20191106T000000")
    oe_temp.sort()
    oe_temp4 = []
    for j in oe_temp:
        if convert_to_time(j[0]) > comp:
            oe_temp4.append(j[1])

    oe_temp.clear()
    lolmax = discovery("http://onem2m.iiit.ac.in:443/~/in-cse/cnt-236279470")[1];

    # get-data-group("cin-511906753")
    # get_data_group("http://onem2m.iiit.ac.in:443/~/in-cse/cin-775866088");
    for i in lolmax:
        print(i)
        if(i[8:11] == "cnt"):
            continue
        get_data_grp("http://onem2m.iiit.ac.in:443/~" + i)
    # for j in 
    comp = convert_to_time("20191106T000000")
    oe_temp.sort()
    oe_temp5 = []
    for j in oe_temp:
        if convert_to_time(j[0]) > comp:
            oe_temp5.append(j[1])       

    oe_temp.clear()
    lolmax = discovery("http://onem2m.iiit.ac.in:443/~/in-cse/cnt-305446869")[1];

    # get-data-group("cin-511906753")
    # get_data_group("http://onem2m.iiit.ac.in:443/~/in-cse/cin-775866088");
    for i in lolmax:
        print(i)
        if(i[8:11] == "cnt"):
            continue
        get_data_grp("http://onem2m.iiit.ac.in:443/~" + i)
    # for j in 
    comp = convert_to_time("20191106T000000")
    oe_temp.sort()
    oe_temp6 = []
    for j in oe_temp:
        if convert_to_time(j[0]) > comp:
            oe_temp6.append(j[1])


    final_reading = []
    i = 0
    while i < min(len(oe_temp1), len(oe_temp2), len(oe_temp3), len(oe_temp4), len(oe_temp5), len(oe_temp6)):
        loli = []
        loli.append(oe_temp1[i][0])
        loli.append(oe_temp1[i][1])
        loli.append(oe_temp2[i])
        loli.append(oe_temp3[i])
        if oe_temp4[i] == "" or oe_temp4[i] == "NULL-Value":
            oe_temp4[i] = oe_temp4[i-1]

        loli.append(oe_temp4[i])
        loli.append(oe_temp5[i])
        loli.append(oe_temp6[i])
        
        if oe_temp5[i] == "" or oe_temp5[i] == "NULL-Value":
            i = i + 1
            continue
        if oe_temp6[i] == "" or oe_temp6[i] == "NULL-Value":
            i = i + 1
            continue
        
        final_reading.append(loli)
        i = i + 1
    
    return final_reading

final = lolzzmax()
# 0 is date time 
for i in final:
    print((float(i[3])*20*60)/(367*float(i[6])))
    data1 = data(temperature = float(i[1]), humidity = float(i[2]), flow = float(i[3]), voltage = float(i[4]), current = float(i[5]), power=float(i[6]), efficiency = (float(i[3])*20*60)/(367*float(i[6])), Time = i[0])
    db.session.add(data1)
    db.session.commit()


#Q*h*sg/(hp*3960)
#Q = flow
#H = 10
#sg = 1
#hp = 5







